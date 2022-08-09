import Home from './page/Home';
import Nav from './page/Nav';
import Footer from './page/Footer';
import Covied19 from './page/Covied19';
import Tips from './page/Tips';
import './App.css';
import {BrowserRouter , Route , Switch} from "react-router-dom"

function App() {
  return (
    <>
    <Nav/>
    <BrowserRouter>
     <Switch>
       <Route exact path={"/"} component={Home} />
       <Route exact path={"/Covied19"} component={Covied19} />
       <Route exact path={"/tips"} component={Tips} />
     </Switch>
    </BrowserRouter>
    <Footer/>

    </>
 );
}

export default App;
