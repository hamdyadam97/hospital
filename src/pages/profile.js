import Container from 'react-bootstrap/Container';
import Navbar from 'react-bootstrap/Navbar';
import 'bootstrap/dist/css/bootstrap.min.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faLocationPin } from '@fortawesome/free-solid-svg-icons'
import { faArrowDown } from '@fortawesome/free-solid-svg-icons';
import { faArrowLeft } from '@fortawesome/free-solid-svg-icons';
import { useState } from 'react';
import { Link } from 'react-router-dom';
import chat from '../image/toppng.com-live-chat-png-1024x1024.png';
import doctor from '../image/toppng.com-edmonton-male-family-doctors-600x698.png';
import Card from 'react-bootstrap/Card';

function Profile() {

    const [doctorinfo, setdoctorinfo] = useState(false);
    const [workAddress, setworkAddress] = useState(false);
    function BookApointment() {
        return (
            <a href='https://play.anghami.com/home'></a>
        )
    }
    return (
        <>
            <div style={{ height: '100vh', backgroundColor:'#ececec' }}>
            <Card className='cardDoctor'>
                <table className='table'>
                    <tr>
                    
                        <td>
                            
                            <img className='doctorimg' src="https://bearskinwellnesscenter.com/wp-content/uploads/2017/03/doctor-smiling-with-stethoscope_1154-36.jpg" />
                        </td>
                        
                        <td>
                        <h1 className='infotext1'>Dr.Mohamed Mostafa</h1>
                            <p className='doctorlocation'>Dermatology</p>
                            <p className='doctorlocation' >Cairo,Egypt</p>



                            {/* <a href=''><img className='infoimg' src={chat} />
                        </a>
                        <h6 className='infotext2'>Chat</h6> */}
                            <td>
                                <div >
                                <h2 className='prsone'style={{marginBottom:doctorinfo?'0px':'108px',color:'#01446E'}}>Person Information</h2>
                                    <button onClick={() => setdoctorinfo(!doctorinfo)} className='Arrow' >
                                        <FontAwesomeIcon className='Arrow' icon={faArrowDown} />
                                    </button>

                                    {
                                        doctorinfo ? <div className='doctorinfo'>
                                            Hello <br /> my name is doctor mohamed <br/>
                                            I am a Dermatologyjdsgfi<br />;sdgdugsa;uidg</div>

                                            : null
                                    }
                                </div>
                                </td>
                             <td>
                                <span>
                                    <h2 className='prsone'style={{marginBottom:workAddress?'0px':'108px',color:'#01446E'}}>Working Address</h2>
                                    <button onClick={() => setworkAddress(!workAddress)} className='Arrow' >
                                        <FontAwesomeIcon className='Arrow' icon={faArrowDown} />
                                    </button>
                                    {
                                        workAddress ? <div className='doctorinfo' >
                                            Hello <br /> my name is doctor mohamed <br />
                                            I am a Dermatologyjdsgfi<br />;sdgdugsa;uidg</div>

                                            : null
                                    }
                                    
                                </span>
                                
                            </td>
                            
                                    <br/>
                            
                                <button className='btn btn-primary'>
                                    <a href='https://play.anghami.com/home' className='bookLink'>Book Appointment</a>


                                </button>
                            

                        </td>

                    </tr>
                    
                </table>
                </Card>  
            </div>
            
        </>
    )


} export default Profile;