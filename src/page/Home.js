import React from "react";
import MessengerCustomerChat from 'react-messenger-customer-chat';
class Home extends React.Component{
    render(){
        return(
        <>
         {/* <!-- Start Landing --> */}
    <div class="landing">
      <div class="container">
        <div class="text">
          <h1>Care Yourself EvryDay</h1>
          <p>Better Healthcare for a Better Life</p>
          <a href="/tips" class="main-button"> Show More </a>
          
        </div>
        <div class="image">
          <img src="assets/imgs/4990223.png" alt="" />
        </div>
      </div>
      <a href="#Top_Doctors" class="go-down">
        <i class="fas fa-angle-double-down fa-2x"></i>
      </a>
    </div>
    {/* <!-- End Landing --> */}
    {/* <!-- Start Doctors --> */}
    <div class="team" id="Top_Doctors">
      <h2 class="main-title">Top Doctors</h2>
      <div class="container">
        <div class="box">
          <div class="data">
            <img src="assets/imgs/team-01.png" alt="" />
            <div class="social">
              <a href="#">
                <i class="fab fa-facebook-f"></i>
              </a>
              <a href="#">
                <i class="fab fa-twitter"></i>
              </a>
              <a href="#">
                <i class="fab fa-linkedin-in"></i>
              </a>
              <a href="#">
                <i class="fab fa-youtube"></i>
              </a>
            </div>
          </div>
          <div class="info">
            <h3>Name</h3>
            <p>Simple Short Description</p>
          </div>
        </div>
        <div class="box">
          <div class="data">
            <img src="assets/imgs/team-01.png" alt="" />
            <div class="social">
              <a href="#">
                <i class="fab fa-facebook-f"></i>
              </a>
              <a href="#">
                <i class="fab fa-twitter"></i>
              </a>
              <a href="#">
                <i class="fab fa-linkedin-in"></i>
              </a>
              <a href="#">
                <i class="fab fa-youtube"></i>
              </a>
            </div>
          </div>
          <div class="info">
            <h3>Name</h3>
            <p>Simple Short Description</p>
          </div>
        </div>
        <div class="box">
          <div class="data">
            <img src="assets/imgs/team-01.png" alt="" />
            <div class="social">
              <a href="#">
                <i class="fab fa-facebook-f"></i>
              </a>
              <a href="#">
                <i class="fab fa-twitter"></i>
              </a>
              <a href="#">
                <i class="fab fa-linkedin-in"></i>
              </a>
              <a href="#">
                <i class="fab fa-youtube"></i>
              </a>
            </div>
          </div>
          <div class="info">
            <h3>Name</h3>
            <p>Simple Short Description</p>
          </div>
        </div>
        <div class="box">
          <div class="data">
            <img src="assets/imgs/team-01.png" alt="" />
            <div class="social">
              <a href="#">
                <i class="fab fa-facebook-f"></i>
              </a>
              <a href="#">
                <i class="fab fa-twitter"></i>
              </a>
              <a href="#">
                <i class="fab fa-linkedin-in"></i>
              </a>
              <a href="#">
                <i class="fab fa-youtube"></i>
              </a>
            </div>
          </div>
          <div class="info">
            <h3>Name</h3>
            <p>Simple Short Description</p>
          </div>
        </div>
        <div class="box">
          <div class="data">
            <img src="assets/imgs/team-01.png" alt="" />
            <div class="social">
              <a href="#">
                <i class="fab fa-facebook-f"></i>
              </a>
              <a href="#">
                <i class="fab fa-twitter"></i>
              </a>
              <a href="#">
                <i class="fab fa-linkedin-in"></i>
              </a>
              <a href="#">
                <i class="fab fa-youtube"></i>
              </a>
            </div>
          </div>
          <div class="info">
            <h3>Name</h3>
            <p>Simple Short Description</p>
          </div>
        </div>
        <div class="box">
          <div class="data">
            <img src="assets/imgs/team-01.png" alt="" />
            <div class="social">
              <a href="#">
                <i class="fab fa-facebook-f"></i>
              </a>
              <a href="#">
                <i class="fab fa-twitter"></i>
              </a>
              <a href="#">
                <i class="fab fa-linkedin-in"></i>
              </a>
              <a href="#">
                <i class="fab fa-youtube"></i>
              </a>
            </div>
          </div>
          <div class="info">
            <h3>Name</h3>
            <p>Simple Short Description</p>
          </div>
        </div>
      </div>
    </div>
    <div class="spikes">
        <MessengerCustomerChat
        pageId="100512945834708"  appId="758513578527305"
      />
    </div>
    {/* <!-- End Doctors --> */}
        </>)
    }
}

export default Home;