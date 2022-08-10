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
        <div class="">
          <img src="assets/imgs/4990223.png" alt=""  width="600px"/>
        </div>
      </div>
    
    </div>
    {/* <!-- End Landing --> */}
    {/* <!-- Start Doctors --> */}
    <div class="team" id="Top_Doctors">
      <h2 class="main-title">Top Doctors</h2>
      <div class="container">
        <div class="box">
          <div class="data">
            <img src="https://st.focusedcollection.com/14026668/i/1800/focused_164883806-stock-photo-portrait-of-smiling-doctor.jpg" width="270px" alt="" />
           
          </div>
          <div class="info">
            <h3>Name</h3>
            <p>dermatologist
</p>
          </div>
        </div>
        <div class="box">
          <div class="data">
            <img src="https://venugramhospitals.com/wp-content/uploads/2016/09/doctor-2.jpg" width="270px" alt="" />
           
          </div>
          <div class="info">
            <h3>Name</h3>
            <p>dentist
</p>
          </div>
        </div>
        <div class="box">
          <div class="data">
            <img src="https://img.freepik.com/free-photo/doctor-with-his-arms-crossed-white-background_1368-5790.jpg?w=2000" alt="" width="270px" />
            
          </div>
          <div class="info">
            <h3>Name</h3>
            <p>Ophthalmologist
</p>
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