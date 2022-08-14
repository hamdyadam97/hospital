import React from "react";
import MessengerCustomerChat from 'react-messenger-customer-chat';
import{useEffect , useState} from "react"
import axios from "axios";






function Home (){
   


      const [doc_data, setdoc_data] = useState([]);

      useEffect(() => {
        axios.get(`http://127.0.0.1:8000/api/`)

            .then((res) => setdoc_data(res.data))
            // .then((res) => console.log(res.data))
            .catch((err) => console.log(err))
    }, [])




    // const imagepath = `http://127.0.0.1:8000${doc_data.image}`

        return(
        <>
         <link rel="stylesheet" href="assets/css/normalize.css" />
          <link rel="stylesheet" href="assets/css/Care.css" />
          <link rel="stylesheet" href="assets/css/all.min.css" />
          <link rel="preconnect" href="https://fonts.googleapis.com" />
          <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
          <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;700&display=swap" rel="stylesheet" />
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
        {
          doc_data.map((docs)=>{
            const imagepath = `http://127.0.0.1:8000${docs.image}`
            return(
              <>
              <div class="box">
              <div class="data">
                <img src={imagepath} width="270px" alt="imge" />
              </div>
              <div class="info">
                <h3>DR.{docs.user}</h3>
                <p>{docs.doctor}</p>
              </div>
            </div>
         
            </>
           
            )
          })
        }

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


export default Home;