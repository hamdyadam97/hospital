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
import DoctorProfile2 from './pages/doctorprofile2';

function App() {
  return (
    <>
     <BrowserRouter>
     {/* <NavBar/> */}
     <Switch>
      <Route exact path={"/"} component={Home}/>
      <Route exact path={"/doctorprofile"} component={DoctorProfile}/>
      {/* <Route exact path={`/doctorprofile/doctor/2`} component={DoctorProfile2}/> */}

      <Route exact path={"/profile"} component={Profile}/>
      <Route exact path={"/history"} component={HistoryOfDoctors}/>
      <Route exact path={"/doctorform"} component={DoctorForm}/>
      <Route exact path={"/login"} component={Login} />
       <Route exact path={"/signup"} component={SignUp} />

      <Route exact path={"*"} component={NoteFound}/>
</Switch>
    {/* <DoctorProfile/> */}
     </BrowserRouter>
    
    </>
  
  );
}

export default App;
