import './App.css';
import { BrowserRouter,Route,Switch } from 'react-router-dom';
import NavBar from './component/NavBar';
import Home from './pages/Home';
import DoctorProfile from './pages/doctorprofile'
import Profile from './pages/profile';
import NoteFound from './pages/NoteFound';
import HistoryOfDoctors from './pages/History1';
import DoctorForm from './pages/doctorform';
import Login from './pages/Login';
import SignUp from './pages/SignUp';
import PatientForm from './pages/patientform';
import Nav from './pages/Nav';
import Footer from './pages/Footer';
import Covied19 from './pages/Covied19';
import Tips from './pages/Tips';
import PatientProfile from './pages/patientprofile'
function App() {
  return (
    <>
    <Nav/>
     <BrowserRouter>
     {/* <NavBar/> */}
     <Switch>

      <Route exact path={"/"} component={Home}/>
      <Route exact path={"/covied19"} component={Covied19}/>
      <Route exact path={"/tips"} component={Tips}/>
      <Route exact path={"/profile"} component={Profile}/>
      <Route exact path={"/history"} component={HistoryOfDoctors}/>
      <Route exact path={"/doctorform/:name"} component={DoctorForm}/>
       <Route exact path={"/doctorprofile/:name"} component={DoctorProfile}/>
      <Route exact path={"/login"} component={Login} />
      <Route exact path={"/signup"} component={SignUp} />
      <Route exact path={"/patientform"} component={PatientForm}/>
      <Route exact path={"/patientprofile/:name"} component={PatientProfile} />
      <Route exact path={"*"} component={NoteFound}/>
      
</Switch>
    {/* <DoctorProfile/> */}
     </BrowserRouter>
    <Footer/>
    </>
  
  );
}

export default App;
