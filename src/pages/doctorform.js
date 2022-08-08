import Card from 'react-bootstrap/Card';
import '../styling/History.css'
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import { useState } from 'react';
function DoctorForm() {
    // const [userData, setUserData] = useState({
    //     name: "",
    //     birthdate: "",
    //     bio: "",
    //     address: "",
    //     mobile: "",
    //     gender: "",
    // })
        return (
        <div className='page'>
            <Card style={{height:'100%'}}>
                <table>
                    <tr>
                        <span>
                            <img className='formimg' src='https://static.vecteezy.com/system/resources/previews/004/797/842/non_2x/illustration-of-cute-male-doctor-with-pointing-hand-kawaii-cartoon-character-design-vector.jpg' />
                        </span>
                        <td style={{ width: '60%', marginRight: '20px' }}>
                            <Form className='formcard'>

                                <Form.Label htmlFor="username">Name</Form.Label>
                                <Form.Control type="text" name='name'id="username" placeholder="Enter Name" />
                            
                                <Form.Label htmlfor="dirth">BirthDate:</Form.Label>

                                <Form.Control type="date" id="dirth" name="birthdate"
                    
                                    max="1999-12-31"/>
                                    <Form.Label htmlFor="bio">Bio</Form.Label>
                                <Form.Control type="text" id="bio" placeholder="Enter bio" name="bio"/>

                                    <Form.Label htmlFor="address">Address</Form.Label>
                                    <Form.Control type="text" placeholder="Address" name="address"/>

                                    <Form.Label htmlFor="tele">Mobile</Form.Label>
                                <Form.Control type="tel" id="tele" placeholder="Enter mobile Number" name=" mobile" />
                                    <br />
                                    <Form.Select name='gender'>
                                        <option>Gender</option>
                                        <option value="1">Male</option>
                                        <option value="2">Female</option>

                                    </Form.Select>
                                    <br />
                                    <Form.Control type="file" placeholder="upload Image" name="image" />
                                    <br />

                                    <Form.Select>
                                        <option>Specialist</option>
                                        <option value="1">Dermatology</option>
                                        <option value="2">dentist</option>
                                        <option value="3">Gynecologist</option>
                                        <option value="4">Ophthalmologist</option>
                                        <option value="5">cardiologist</option>

                                    </Form.Select>
                                    <br/>
                                    <Form.Label htmlFor="gmail">Gmail</Form.Label>
                                <Form.Control type="email" id="gmail" placeholder="Enter Gmail" />
                                <br/>
                                    <Form.Select>
                                        <option>Day1</option>
                                        <option value="1">sunday</option>
                                        <option value="2">MonDay</option>
                                        <option value="3">Tuesday</option>
                                        <option value="4">Wednesday</option>
                                        <option value="5">Thursday</option>
                                        <option value="6">Friday</option>
                                        <option value="7">Saturday</option>

                                    </Form.Select>
                                    <br/>
                                    <Form.Select>
                                        <option>Day2</option>
                                        <option value="1">sunday</option>
                                        <option value="2">MonDay</option>
                                        <option value="3">Tuesday</option>
                                        <option value="4">Wednesday</option>
                                        <option value="5">Thursday</option>
                                        <option value="6">Friday</option>
                                        <option value="7">Saturday</option>

                                    </Form.Select>
                                    <br/>
                                    <Form.Select>
                                        <option>Day3</option>
                                        <option value="1">sunday</option>
                                        <option value="2">MonDay</option>
                                        <option value="3">Tuesday</option>
                                        <option value="4">Wednesday</option>
                                        <option value="5">Thursday</option>
                                        <option value="6">Friday</option>
                                        <option value="7">Saturday</option>

                                    </Form.Select>
                                    
                                    <Form.Label htmlFor="price">price</Form.Label>
                                <Form.Control type="number" id="price" placeholder="Enter price" />

                                <br />
                                    {/* <Form.Group className="mb-3" controlId="formBasicPassword">
                                    <Form.Label>Password</Form.Label>
                                    <Form.Control type="password" placeholder="Password" />
                                </Form.Group>
                                <Form.Group className="mb-3" controlId="formBasicCheckbox">
                                    <Form.Check type="checkbox" label="Check me out" />
                                </Form.Group> */}

                                    <br />
                                    <Button variant="primary" type="submit">
                                        Submit
                                    </Button>
                            </Form>
                        </td>
                    </tr>

                </table>

            </Card>

        </div>
    )
}
export default DoctorForm