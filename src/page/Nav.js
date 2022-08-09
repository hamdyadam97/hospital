import React from "react";

class Nav extends React.Component{
    render(){
        return(
        <>
           {/* <!-- Start Header --> */}
    <div class="header" id="header">
      <div class="container">
        <a href="#" class="logo"> <img src="assets/imgs/logo.png" alt="" class="logo" /></a>
       
        <ul class="main-nav">
          <li><a href="/covied19">Covid-19</a></li>
          <li><a href="#">Ambulance</a></li>
          <li><a href="#Top_Doctors">Top Doctor</a></li>
          <li>
            <a href="#">Other Links</a>
            {/* <!-- Start Megamenu --> */}
            <div class="mega-menu">
              <div class="image">
                <img src="assets/imgs/megamenu.png" alt="" />
              </div>
              <ul class="links">
                <li>
                  <a href="#"><i class="far fa-comments fa-fw"></i> About Us</a>
                </li>
                <li>
                  <a href="#"><i class="far fa-user fa-fw"></i> Team Members</a>
                </li>
                <li>
                  <a href="#"><i class="far fa-building fa-fw"></i> Services</a>
                </li>
                <li>
                  <a href="#"><i class="far fa-check-circle fa-fw"></i> Our Skills</a>
                </li>
                <li>
                  <a href="#"><i class="far fa-clipboard fa-fw"></i> How It Works</a>
                </li>
              </ul>
              <ul class="links">
                <li>
                  <a href="#"><i class="far fa-calendar-alt fa-fw"></i> Events</a>
                </li>
                <li>
                  <a href="#"><i class="fas fa-server fa-fw"></i> Careers </a>
                </li>
                <li>
                  <a href="#"><i class="fa-solid fa-user"></i>Join CareSup Doctors </a>
                </li>
              
              </ul>
            </div>
            {/* <!-- End Megamenu --> */}
          </li>
        </ul>
      </div>
    </div>
    {/* <!-- End Header --> */}
        </>)
    }
}

export default Nav;