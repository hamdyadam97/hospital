import './App.css';
import { BrowserRouter,Route,Switch } from 'react-router-dom';
import NavBar from './component/NavBar';
import Home from './pages/Home';
import DoctorProfile from './pages/doctorprofile'
import Profile from './pages/profile';
import NoteFound from './pages/NoteFound';
import HistoryOfDoctors from './pages/History1';
import DoctorForm from './pages/doctorform';
function App() {
  return (
    <>
     <BrowserRouter>
     {/* <NavBar/> */}
     <Switch>
      <Route exact path={"/"} component={Home}/>
      <Route exact path={"/doctorprofile"} component={DoctorProfile}/>
      <Route exact path={"/profile"} component={Profile}/>
      <Route exact path={"/history"} component={HistoryOfDoctors}/>
      <Route exact path={"/doctorform"} component={DoctorForm}/>
      <Route exact path={"*"} component={NoteFound}/>
</Switch>
    {/* <DoctorProfile/> */}
     </BrowserRouter>
    
    </>
  
  );
}

export default App;
