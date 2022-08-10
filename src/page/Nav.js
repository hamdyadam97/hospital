import React from "react";

class Nav extends React.Component{
    render(){
        return(
        <>
 <div class="nav">
<ul >
<a href="#" class="logo"> <img src="assets/imgs/logo.png" alt="" className="logo1"/></a>
  <li><a href="/Covied19">Covied19</a></li>
  <li> <a>Ambluens</a></li>
  <li><a>Top Doctors</a></li>
  <li><a>More</a></li>
</ul>
</div>
        </>)
    }
}

export default Nav;