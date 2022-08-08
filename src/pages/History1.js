import Card from 'react-bootstrap/Card';
import ListGroup from 'react-bootstrap/ListGroup';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import Container from 'react-bootstrap/Container';
import '../styling/History.css'
function HistoryOfDoctors() {
    const status = ['Done', 'cancel']
    const del='block'
    function remove(){
        
            del='none'
        
        
    }
    return (
        <div >
            <Navbar bg="light" variant="light">
        <Container>
          <Navbar.Brand href="#home">Navbar</Navbar.Brand>
          <Nav className="me-auto">
            <Nav.Link href="#home">Home</Nav.Link>
            <Nav.Link href="#features">Features</Nav.Link>
            <Nav.Link href="#pricing">Pricing</Nav.Link>
          </Nav>
        </Container>
      </Navbar>


            <Card style={{ backgroundColor: '#ececec' ,width: '100%', height: 'auto', display: 'inline-block' }}>

                <ListGroup >
                    <ListGroup.Item className='item'>
                        <h6>Dr.Mohamed Kamal</h6>
                        <p>Dermatology</p>
                        <p>20-9-2022</p>
                        {status[0] === 'cancel' ?
                            <h6 className='text-danger'>cancel</h6> :
                            <h6 className='text-success'>Done</h6>
                        }
                        <button className='btn btn-danger' >Delete</button>
                    </ListGroup.Item>
                    <ListGroup.Item className='item'>
                        <h6>Dr.Mohamed Kamal</h6>
                        <p>Dermatology</p>
                        <p>20-9-2022</p>
                        {status[0] === 'cancel' ?
                            <h6 className='text-danger'>cancel</h6> :
                            <h6 className='text-success'>Done</h6>
                        }
                        <button className='btn btn-danger' >Delete</button>
                    </ListGroup.Item>
                    <ListGroup.Item className='item'>
                        <h6>Dr.Mohamed Kamal</h6>
                        <p>Dermatology</p>
                        <p>20-9-2022</p>
                        {status[1] === 'cancel' ?
                            <h6 className='text-danger'>cancel</h6> :
                            <h6 className='text-success'>Done</h6>
                        }
                        <button className='btn btn-danger' >Delete</button>
                    </ListGroup.Item>
                    <ListGroup.Item className='item'>
                        <h6>Dr.Mohamed Kamal</h6>
                        <p>Dermatology</p>
                        <p>20-9-2022</p>
                        {status[0] === 'cancel' ?
                            <h6 className='text-danger'>cancel</h6> :
                            <h6 className='text-success'>Done</h6>
                        }
                        <button className='btn btn-danger' >Delete</button>
                    </ListGroup.Item>
                    <ListGroup.Item className='item' style={{display:del=='block'?'block':'none'}}>
                        <h6>Dr.Mostafa Ahmed</h6>
                        <p>Dermatology</p>
                        <p>20-9-2022</p>
                        {status[1] === 'cancel' ?
                            <h6 className='text-danger'>cancel</h6> :
                            <h6 className='text-success'>Done</h6>
                        }
                        <button className='btn btn-danger'>Delete</button>
                    </ListGroup.Item>
                    <ListGroup.Item className='item'>
                        <h6>Dr.Rania Mohamed</h6>
                        <p>Dermatology</p>
                        <p>20-9-2022</p>
                        {status[1] === 'cancel' ?
                            <h6 className='text-danger'>cancel</h6> :
                            <h6 className='text-success'>Done</h6>
                        }
                        <button className='btn btn-danger' >Delete</button>
                    </ListGroup.Item>
                    <ListGroup.Item className='item'>Vestibulum at eros</ListGroup.Item>
                    <ListGroup.Item className='item'>
                        <h6>Dr.Mohamed Kamal</h6>
                        <p>Dermatology</p>
                        <p>20-9-2022</p>
                        {status[0] === 'cancel' ?
                            <h6 className='text-danger'>cancel</h6> :
                            <h6 className='text-success'>Done</h6>
                        }
                        <button className='btn btn-danger' >Delete</button>
                    </ListGroup.Item>



                </ListGroup>

            </Card>


        </div >
    )
}
export default HistoryOfDoctors