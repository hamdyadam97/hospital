import 'bootstrap/dist/css/bootstrap.min.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faLocationPin } from '@fortawesome/free-solid-svg-icons'
import { faArrowDown } from '@fortawesome/free-solid-svg-icons';
import { useState } from 'react';
import chat from '../image/toppng.com-live-chat-png-1024x1024.png';
import '../styling/DoctorProfile.css'
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
            <section class="vh-100" style={{ backgroundColor: '#eee' }}>
                <div class="container py-5 h-100">
                    <div class="row d-flex justify-content-center align-items-center h-100">
                        <div class="col-md-12 col-xl-4">

                            <div class="card" style={{ borderRadius: '15px' }}>
                                <div class="card-body text-center">
                                    <div class="mt-3 mb-4">
                                        <img src="https://bearskinwellnesscenter.com/wp-content/uploads/2017/03/doctor-smiling-with-stethoscope_1154-36.jpg"
                                            class="rounded-circle img-fluid" style={{ width: '100px' }} />
                                    </div>


                                    <h4 class="mb-2">Dr.Mohamed Mostafa</h4>
                                    <p class="text-muted mb-4">Dermatology<span class="mx-2">|</span> Cairo,Egypt</p>



                                    <div class="mb-4 pb-2">
                                        {/* <button type="button" class="btn btn-outline-primary btn-floating">
                                            chat icon
                                        </button> */}
                                    </div>
                                    <button type="button" class="btn btn-primary btn-rounded btn-lg">
                                        Message now
                                    </button>

                                    <div class="d-flex justify-content-between text-center mt-5 mb-2">
              <div>
              <h5 className='prsone'style={{color:'#01446E'}}>Person Information</h5>
                                <button onClick={() => setdoctorinfo(!doctorinfo)} className='Arrow' >
                                    <FontAwesomeIcon  icon={faArrowDown} />
                                </button>

                                {
                                    doctorinfo ? <div className='doctorinfo'>
                                        Hello <br /> my name is doctor mohamed <br/>
                                        I am a Dermatologyjdsgfi<br />;sdgdugsa;uidg</div>

                                        : null
                                }
              </div>
              <div class="px-1">
              <h5 className='prsone'style={{color:'#01446E'}}>Working Address</h5>
                                <button onClick={() => setworkAddress(!workAddress)} className='Arrow' >
                                    <FontAwesomeIcon  icon={faArrowDown} />
                                </button>
                                {
                                    workAddress ? <div className='doctorinfo' >
                                        Hello <br /> my name is doctor mohamed <br />
                                        I am a Dermatologyjdsgfi<br />;sdgdugsa;uidg</div>

                                        : null
                                }
              </div>
</div>
                                </div>
                            </div>


                        </div>
                    </div>
                </div>
            </section>
        </>
    )

} export default Profile;