import React from "react";

class Nav extends React.Component{
    render(){
        return(
        <>
         <link rel="stylesheet" href="assets/css/normalize.css" />
      <link rel="stylesheet" href="assets/css/Care.css" />
      <link rel="stylesheet" href="assets/css/all.min.css" />
      <link rel="preconnect" href="https://fonts.googleapis.com" />
      <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
      <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;700&display=swap" rel="stylesheet" />
 <div class="nav">
<ul >
<a href="#" class="logo"> <img src="assets/imgs/logo.png" alt="" className="logo1"/></a>
  <li><a href="/Covied19">Covied19</a></li>
  <li> <a href="/signup">Ambluens</a></li>
  <li><a href="/patientform">Top Doctors</a></li>
  <li><a>More</a></li>
</ul>
</div>
        </>)
    }
}

export default Nav;