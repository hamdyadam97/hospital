// import 'bootstrap/dist/css/bootstrap.min.css';
// import Card from 'react-bootstrap/Card';
// import '../styling/History.css'
// import Button from 'react-bootstrap/Button';
// import { useParams } from 'react-router-dom';
// import axios from 'axios';
// import { useEffect } from 'react';
// import { useState } from 'react';
// function DoctorProfile2() {
//     const params = useParams();
//     var k = params.id
//     const [doc_data, setdoc_data] = useState([]);
//     useEffect(() => {

//         axios
//             .get(" http://127.0.0.1:8000/createprofiledoctor/")
        
//             .then((res) => setdoc_data(res.data))
//             .catch((err) => console.log(err))

//     })
// console.log(params.name)
//     return (


//         <div className='page'>

//             <Card className='card1'>
//                 <Card.Img className='docimg' src="https://thumbs.dreamstime.com/b/young-doctor-16088825.jpg" />
//                 <Card.Body>
//                     <Card.Title className='data'>Dr.Mohamed Ahmed</Card.Title>
//                     <Card.Text className='data'>
//                         Dermatology
//                     </Card.Text>
//                     <Button className='btn btn-primary' style={{ marginLeft: '130px' }} >Edit ProfilePic</Button>
//                 </Card.Body>

//             </Card>

//             <Card className='card2'>
//                 <Card.Body classNa>
//                     <table style={{width:'100%'}}>
//                         <tr>
//                             <th>
//                                FullName
//                             </th>
//                             <td>
                                
//                                Mohamed Ahmed
//                             </td>
                            
//                         </tr>
//                         <hr style={{width:'400%'}}/>
//                         <tr>
//                             <th>
//                                 Address
//                             </th>
//                             <td>
                                
//                                Cairo,Egypt
//                             </td>
//                         </tr>
//                         <hr style={{width:'400%'}}/>
//                         <tr>
//                             <th>
//                                 Email
//                             </th>
//                             <td>
                                
//                                mohamedAhmed@gmail.com
//                             </td>
//                         </tr>
//                         <hr style={{width:'400%'}}/>
//                         <tr>
//                             <th>
//                                Specialist
//                             </th>
//                             <td>
                                
//                                Dermatology
//                             </td>
//                         </tr>
//                         <hr style={{width:'400%'}}/>
//                         <tr>
//                             <th>
//                                Mobile
//                             </th>
//                             <td>
                                
//                                01002366772
//                             </td>
//                         </tr>
//                         <hr style={{width:'400%'}}/>
//                         <tr>
//                             <th>
//                                Phone
//                             </th>
//                             <td>
                                
//                                0882627709
//                             </td>
//                         </tr>
//                         <hr style={{width:'400%'}}/>
//                     </table>
//                     <Button className='btn btn-info' style={{color:'white'}}>Edit Data</Button>

//                 </Card.Body>

//             </Card>
//             <Card className='card1'>
//                 <Card.Body>
//                 <table style={{width:'100%'}}>
//                         <tr>
//                             <th>
//                                BirthDate
//                             </th>
//                             <td>
                                
//                                20-1-1989
//                             </td>
                            
//                         </tr>
//                         <hr style={{width:'300%'}}/>
//                         <tr>
//                             <th>
//                                 Gender
//                             </th>
//                             <td>
                                
//                                Male
//                             </td>
//                         </tr>
//                         <hr style={{width:'300%'}}/>
//                         <tr>
//                             <th>
//                                 FaceBook
//                             </th>
//                             <td>
                                
//                               www.facebook.com
//                             </td>
//                         </tr>
//                         <hr style={{width:'300%'}}/>
//                         <tr>
//                             <th>
//                                Gmail
//                             </th>
//                             <td>
                                
//                                mohamedAhmed@gmail
//                             </td>
//                         </tr>
//                         <hr style={{width:'300%'}}/>
//                         <tr>
//                             <th>
//                                Twitter
//                             </th>
//                             <td>
                                
//                                www.Twitter.com
//                             </td>
//                         </tr>
//                         <hr style={{width:'300%'}}/>
                        
                        
//                     </table>
//                 </Card.Body>

//             </Card>
//             <Card className='card2'>
//                 <Card.Body>
//                 <table style={{width:'100%'}}>
//                     <h3 style={{color:'#3B9AE1'}}>Booking Details</h3>
//                         <tr>
//                             <th>
//                                Price
//                             </th>
//                             <td>
                                
//                                200EGP
//                             </td>
                            
//                         </tr>
//                         <hr style={{width:'140%'}}/>
                        
                        
//                         <tr>
//                             <th>
//                                 Hour OF Work
//                             </th>
//                             <td>
                                
//                               2pm-8pm
//                             </td>
//                         </tr>
//                         <hr style={{width:'140%'}}/>
//                         <tr>
//                             <th>
//                                Day1
//                             </th>
//                             <td>
                                
//                                SaturDay
//                             </td>
//                         </tr>
//                         <hr style={{width:'140%'}}/>
//                         <tr>
//                             <th>
//                                Day2
//                             </th>
//                             <td>
                                
//                                MonDay
//                             </td>
//                         </tr>
//                         <hr style={{width:'140%'}}/>
//                         <tr>
//                             <th>
//                                Day3
//                             </th>
//                             <td>
                                
//                             Wednesday
//                             </td>
//                         </tr>
//                         <hr style={{width:'140%'}}/>
                        
                        
//                     </table>
//                 </Card.Body>

//             </Card>


//         </div>





//     )
// } export default DoctorProfile2;

