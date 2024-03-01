import './App.css';
import SearchIcon from './search.svg';


const App = () => {
  return (
      <div className="app">
        <h1>Skapiec</h1>

        <div className="search">
          <input
           placeholder="Wyszukaj"
           //value="rower"
           onChange={()=> {}}
           />

           <img
            src={SearchIcon}
            alt="search"
            onClick={() => {}} //jeszcze nic nie robi
            />
        </div>

        <div className="container">

        </div>
      </div>
  );
}

export default App;
