import './App.css';
import { BrowserRouter,Route,Switch } from 'react-router-dom';
import Home from './pages/Home';
import DoctorProfile from './pages/doctorprofile'
import Profile from './pages/profile';
import NoteFound from './pages/NoteFound';
import HistoryOfDoctors from './pages/History1';
import DoctorForm from './pages/doctorform';
import Login from './pages/Login';
import SignUp from './pages/SignUp';
import  Nav from './pages/Nav';
import  Covied19 from './pages/Covied19';
import  Footer from './pages/Footer';
import  Tips from './pages/Tips';

function App() {
  return (
    <>
     <BrowserRouter>
      <Nav/> 
     <Switch>
      <Route exact path={"/"} component={Home}/>
      <Route exact path={"/doctorprofile/:name"} component={DoctorProfile}/>
      <Route exact path={"/profile"} component={Profile}/>
      <Route exact path={"/history"} component={HistoryOfDoctors}/>
      <Route exact path={"/doctorform/:name"} component={DoctorForm}/>
      <Route exact path={"/login"} component={Login} />
       <Route exact path={"/Covied19"} component={Covied19} />
       <Route exact path={"/Tips"} component={Tips} />

      <Route exact path={"*"} component={NoteFound}/>
    </Switch> 
      <Footer/> 
     </BrowserRouter>
    
    </>
  
  );
}

export default App;
