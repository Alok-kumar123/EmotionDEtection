
import './App.css';
import Navbar from './Components/Navbar';
import Image from './Components/Image';
import {Routes,Route,BrowserRouter} from 'react-router-dom'
import About from './Components/About';

function App() {
  return (
    <BrowserRouter>
     <div>
      <Navbar/>
      
       <Routes>
        <Route path='/about' element={<About/>}/>
        <Route path='/' element={<Image/>}/>
       </Routes>
      
      
     </div>
     </BrowserRouter>
  );
}

export default App;
