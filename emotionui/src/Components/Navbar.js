import React from 'react'
import './Navbar.css'
import {Link} from 'react-router-dom'
const Navbar = () => {
  return (
     <nav className='navbar'>
      <div className='navbar-brand'>YourEmotion</div>
      <ul className='nav-links'>
        <li><Link to='/'>Home</Link></li>
        <li><Link to='about'>About</Link></li>
        <li><a href='#contacts'>ContactUs</a></li>
      </ul>
     </nav>
  )
}

export default Navbar
