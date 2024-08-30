import React, {useState,useRef} from 'react';
import Webcam from 'react-webcam';
import './Image.css';



const Image = () => {

    const [imageSrc, setImageSrc]=useState(null);
    const [classification,setClassification]=useState(null);
    const [cameraOn, setCameraOn]=useState(false);
    const webcamRef=useRef(null);

    const videoConstraint={
        width:640,
        height:480,
        facingMode: 'user',
    };

    const capture=()=>{
        const imageSrc=webcamRef.current.getScreenshot();
        setImageSrc(imageSrc);
        setCameraOn(false);
    };

    const handleImUpload=(e)=>{
        const file=e.target.files[0];
        const reader=new FileReader();
        reader.onloadend=()=>{
            setImageSrc(reader.result);
        };
        reader.readAsDataURL(file);
    };

    const classifyImage=async()=>{
        const formData=new FormData();
        const blob=await fetch(imageSrc).then(res=>res.blob());
        formData.append('file',blob,'image.jpg');
        const response=await fetch('http://localhost:8000/predict',{
            method:'POST',
            body: formData
        });

        const result=await response.json();
        console.log(result);
        setClassification([result.Emotion, result.confidence]);
    };

  return (
    <div className='image-container'>
        <h2>Capture or Upload an Image</h2>
        <span style={{color:'red'}}>Note: **the maximum area of image should be covered with face</span>
        <div className='webcam-container'>
             {cameraOn && !imageSrc && (
                <Webcam
                audio={false}
                ref={webcamRef}
                screenshotFormat='image/jpeg'
                className='webcam'
                videoConstraints={videoConstraint}
                />
             )}
             {imageSrc && (
                <img src={imageSrc} alt='Captured' className='captured-image'/>
             )}
        </div>
        <div className='button-container'>
            {!cameraOn && !imageSrc && (
                <button onClick={()=>setCameraOn(true)} className='capture-button'>
                    Turn On Camera
                </button>
            )}
            {!imageSrc && cameraOn && (
                <button onClick={capture} className='capture-button'>
                    Capture Photo
                </button>
            )}
            <input
            type='file'
            accept='image/*'
            onChange={handleImUpload}
            className='upload-input'
            />
            {imageSrc && (
               <>  
                <button onClick={classifyImage} className='classify-button'>
                    classify Image
                    </button>              
               <button onClick={()=>{setImageSrc(null); setClassification(null);}} className='reset-button'>
                    Reset
                </button>
                </>

            )}
        </div>
        {classification && (
            <div className='classification-result'>
                <h3>Classification Result: {classification[0]} </h3>
                <h3>Confidence: {classification[1]*100} % </h3>
            </div>
        )}
    </div>
  )
}

export default Image