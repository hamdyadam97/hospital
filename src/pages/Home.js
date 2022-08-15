// import React, { useEffect } from 'react';
// import axios from "axios";

// function Home() {
//     let user = localStorage.getItem('user')
//     useEffect(() => {

//         window.paypal.Buttons({
//             createOrder: (data,actions) =>{
//                 return actions.order.create({

//                     purchase_units: [{
//                         amount: {
//                             value : 100.00
//                         }
//                     }]
//                 });
//             },
//             onApprove : (data,actions) =>{
//                 return actions.order.capture().then(details =>{
//                     axios
//                     .post("http://127.0.0.1:8000/appointment/appointment/", {
//                         doctor: 'ayatkhaled',
//                         patient:user
//                     })
//                     .then((res) => {
//                         console.log(res.data)
            
//                     })
//                     .catch((err) => {
//                         console.log(err.response.data)
//                     });
                       
//                     // alert ('Thanks For Paying dear ' + details.payer.name.given_name);
//                 });
//             }

//         }).render('#paypal-button-container')

//     },[])


//     return (
//         <div id="paypal-button-container">

//         </div>
//     );  

// }  
// export default Home;