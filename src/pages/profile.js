import 'bootstrap/dist/css/bootstrap.min.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
// import { faLocationPin } from '@fortawesome/free-solid-svg-icons'
import { faArrowDown } from '@fortawesome/free-solid-svg-icons';
import { useState } from 'react';
// import chat from '../image/toppng.com-live-chat-png-1024x1024.png';
import '../styling/DoctorProfile.css'
import { useParams } from 'react-router-dom';
import axios from 'axios';
import { useEffect } from 'react';
import Form from 'react-bootstrap/Form';
function Profile() {
    
    let user = localStorage.getItem('user')
    const [doctorinfo, setdoctorinfo] = useState(false);
    const [workAddress, setworkAddress] = useState(false);
    const [rate_doc, setrate_doc] = useState(false);

    const params = useParams();
    var doc_name = params.name
    const [doc_data, setdoc_data] = useState([]);
    useEffect(() => async () => {
      await axios.get(`http://127.0.0.1:8000/doctordata/${doc_name}`)
 
             .then((res) => setdoc_data(res.data))
             .catch((err) => console.log(err))
    }, [])
    console.log(doc_data.price)
  
    useEffect(() =>  {

        if(doc_data.price){
         window.paypal.Buttons({  
            createOrder: (data, actions) => { 
                
                return actions.order.create({

                    purchase_units: [{
                        amount: {
                            value: doc_data.price
                        }
                    }] 
                });
            },
            onApprove: (data, actions) => {
                return actions.order.capture().then(details => {
                    axios
                        .post("http://127.0.0.1:8000/appointment/appointment/", {
                            doctor: doc_name,
                            patient: user
                        })
                        .then((res) => {
                            console.log(res.data)

                        })
                        .catch((err) => {
                            console.log(err.response.data)
                        });

                    // alert ('Thanks For Paying dear ' + details.payer.name.given_name);
                });
            }
        
        }).render('#paypal-button-container')
        }
    },[doc_data.price])   


    const imagepath = `http://127.0.0.1:8000${doc_data.image}`

    return (

        <>
            <section className="vh-100" style={{ backgroundColor: '#01446E' }}>
                <div className="container py-5 h-100">
                    <div className="row d-flex justify-content-center align-items-center h-100">
                        <div className="col-md-12 col-xl-4">

                            <div className="card" style={{ borderRadius: '15px' }}>
                                <div className="card-body text-center">
                                    <div className="mt-3 mb-4">
                                        <img src={imagepath}
                                            className="rounded-circle img-fluid" style={{ width: '100px' }} />
                                    </div>


                                    <h2 className="mb-2">Dr.{doc_name}</h2>
                                    <p className="text-muted mb-4" style={{ fontSize: '30px' }}>{doc_data.specialist_doctor}<span className="mx-2">|</span> {doc_data.address}</p>


                                    <div id="paypal-button-container" className="btn btn-primary btn-rounded btn-lg" >

                                    </div>

                                    {/* <button  type="button" className="btn btn-primary btn-rounded btn-lg" onClick={BookApointment}>
                                        Booking Now
                                    </button> */}

                                    <div classNameName="d-flex justify-content-between text-center mt-5 mb-2">
                                        <div>
                                            <h5 classNameName='prsone' style={{ color: '#01446E' }}>Person Information</h5>
                                            <button onClick={() => setdoctorinfo(!doctorinfo)} className='Arrow' >
                                                <FontAwesomeIcon icon={faArrowDown} />
                                            </button>

                                            {
                                                doctorinfo ? <div className='doctorinfo'>
                                                    {doc_data.bio}</div>

                                                    : null
                                            }
                                        </div>
                                        <div className="px-1">
                                            <h5 classNameName='prsone' style={{ color: '#01446E' }}>Working Address</h5>
                                            <button onClick={() => setworkAddress(!workAddress)} className='Arrow' >
                                                <FontAwesomeIcon icon={faArrowDown} />
                                            </button>
                                            {
                                                workAddress ? <div className='doctorinfo' >
                                                    {doc_data.address_detail}</div>

                                                    : null
                                            }
                                        </div>


                                    </div>
                                    <button className='btn btn-primary' onClick={() => setrate_doc(!rate_doc)}  >
                                        <FontAwesomeIcon />
                                        Rate
                                    </button>

                                    {
                                        rate_doc ?

                                            <Form.Group className="mb-3">
                                                <br />
                                                <Form.Label htmlFor="rate">Giv Rate</Form.Label>
                                                <Form.Control
                                                    type="number"
                                                    id="rate"
                                                    min='1' max='5'
                                                    placeholder='give rate from 1 to 5'
                                                />


                                                <Form.Label htmlFor="rate">Comment</Form.Label>
                                                <Form.Control
                                                    type="textarea"
                                                    id="rate"
                                                    placeholder='write your comment'
                                                />
                                            </Form.Group>



                                            : null
                                    }

                                    <br />


                                </div>
                            </div>


                        </div>
                    </div>
                </div>
            </section>
        </>
    )

} export default Profile;