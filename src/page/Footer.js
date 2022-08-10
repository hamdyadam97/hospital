import React from "react";

class Footer extends React.Component{
    render(){
        return(
        <>
           {/* <!-- Start Footer --> */}
    <div class="footer">
      <div class="container">
        <div class="box">
          <h3>Cure Sup</h3>
          <ul class="social">
       
          </ul>
          <p class="text">
          We are pioneering the shift to automated physician, clinic and hospital bookings making healthcare easily accessible in the region.
          </p>
        </div>
        <div class="box">
          <ul class="links">
            <li><a href="#">Join CareSup Doctors</a></li>
            <li><a href="#">Covid-19</a></li>
            <li><a href="#">Ambulance</a></li>
          </ul>
        </div>
        <div class="map">
        <iframe width="405" height="335" src="https://maps.google.com/maps?q=Assiut%20University&t=&z=13&ie=UTF8&iwloc=&output=embed" frameborder="0" scrolling="no" marginheight="0" marginwidth="0"></iframe>
        </div>

      </div>
      <p class="copyright"> &copy; All Rights Reserved To ITI Team</p>
    </div>
    {/* <!-- End Footer --> */}
        </>)
    }
}

export default Footer;