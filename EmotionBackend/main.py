from fastapi import FastAPI, File, UploadFile
import uvicorn
import tensorflow as tf
import keras
from PIL import Image
import io
import numpy as np
from fastapi.responses import JSONResponse
from keras.layers import Layer, Conv2D, BatchNormalization, Activation, Add, Dense, GlobalAveragePooling2D, MaxPooling2D
from keras.models import Model
from keras.losses import CategoricalCrossentropy
from keras.metrics import TopKCategoricalAccuracy, CategoricalAccuracy
from keras.optimizers import Adam
from fastapi.middleware.cors import CORSMiddleware



app=FastAPI()

class CustomConv2D(Layer):
  def __init__(self, n_filters, kernel_size, n_strides, padding = 'valid'):
    super(CustomConv2D, self).__init__(name = 'custom_conv2d')

    self.conv = Conv2D(
        filters = n_filters,
        kernel_size = kernel_size,
        activation = 'relu',
        strides = n_strides,
        padding = padding)

    self.batch_norm = BatchNormalization()

  def call(self, x, training = True):

    x = self.conv(x)
    x = self.batch_norm(x, training=training)

    return x

   
class ResidualBlock(Layer):
  def __init__(self, n_channels, n_strides = 1):
    super(ResidualBlock, self).__init__(name = 'res_block')

    self.dotted = (n_strides != 1)

    self.custom_conv_1 = CustomConv2D(n_channels, 3, n_strides, padding = "same")
    self.custom_conv_2 = CustomConv2D(n_channels, 3, 1, padding = "same")

    self.activation = Activation('relu')

    if self.dotted:
      self.custom_conv_3 = CustomConv2D(n_channels, 1, n_strides)

  def call(self, input, training):

    x = self.custom_conv_1(input, training=training)
    x = self.custom_conv_2(x, training=training)

    if self.dotted:
      x_add = self.custom_conv_3(input, training=training)
      x_add = Add()([x, x_add])
    else:
      x_add = Add()([x, input])

    return self.activation(x_add)

class ResNet34(Model):
  def __init__(self,):
    super(ResNet34, self).__init__(name = 'resnet_34')

    self.conv_1 = CustomConv2D(64, 7, 2, padding = 'same')
    self.max_pool = MaxPooling2D(3,2)

    self.conv_2_1 = ResidualBlock(64)
    self.conv_2_2 = ResidualBlock(64)
    self.conv_2_3 = ResidualBlock(64)

    self.conv_3_1 = ResidualBlock(128, 2)
    self.conv_3_2 = ResidualBlock(128)
    self.conv_3_3 = ResidualBlock(128)
    self.conv_3_4 = ResidualBlock(128)

    self.conv_4_1 = ResidualBlock(256, 2)
    self.conv_4_2 = ResidualBlock(256)
    self.conv_4_3 = ResidualBlock(256)
    self.conv_4_4 = ResidualBlock(256)
    self.conv_4_5 = ResidualBlock(256)
    self.conv_4_6 = ResidualBlock(256)

    self.conv_5_1 = ResidualBlock(512, 2)
    self.conv_5_2 = ResidualBlock(512)
    self.conv_5_3 = ResidualBlock(512)

    self.global_pool = GlobalAveragePooling2D()

    self.fc_3 = Dense(3, activation = 'softmax')

  def call(self, x, training = True):
    x = self.conv_1(x)
    x = self.max_pool(x)

    x = self.conv_2_1(x, training=training)
    x = self.conv_2_2(x, training=training)
    x = self.conv_2_3(x, training=training)

    x = self.conv_3_1(x, training=training)
    x = self.conv_3_2(x, training=training)
    x = self.conv_3_3(x, training=training)
    x = self.conv_3_4(x, training=training)

    x = self.conv_4_1(x, training=training)
    x = self.conv_4_2(x, training=training)
    x = self.conv_4_3(x, training=training)
    x = self.conv_4_4(x, training=training)
    x = self.conv_4_5(x, training=training)
    x = self.conv_4_6(x, training=training)

    x = self.conv_5_1(x, training=training)
    x = self.conv_5_2(x, training=training)
    x = self.conv_5_3(x, training=training)

    x = self.global_pool(x)

    return self.fc_3(x)

model=ResNet34()
model(tf.zeros([1,256,256,3]),training=False)
model.summary()

model.load_weights("C:\\Users\\alok\\Downloads\\ResModel4.keras")

origins = [
    "http://localhost",
    "http://localhost:3000",
]
app.add_middleware( 
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/predict")
async def EmotionPred(file: UploadFile=File(...)):
    try:

        image_data=await file.read()
        image=Image.open(io.BytesIO(image_data))
         
        image=image.resize((256,256))
        image=np.array(image)

        if image.ndim==2:
           image=np.stack((image,)*3,axis=-1)

        image=image.astype('float32')
        image=np.expand_dims(image,0)

        print(f"Image shape before prediction: {image.shape}")

        predictions=model.predict(image)
        predictions=predictions.tolist()
        class_names=["Angry","Happy","Sad"]
        emotion=class_names[np.argmax(predictions[0])]
        confidence=np.max(predictions[0])

        return JSONResponse({"Emotion":emotion,"confidence":confidence,"pred":predictions})
    except Exception as e:
        return JSONResponse(content={"error":str(e)},status_code=400)
    

if __name__=="__main__":
    uvicorn.run(app,host='0.0.0.0',port=8000)

