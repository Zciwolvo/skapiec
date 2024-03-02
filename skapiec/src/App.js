import './App.css';
import SearchIcon from './search.svg';
import React, { useState, useEffect } from 'react';


const App = () => {
  //fetching data
    const [data, setData] = useState([]);
    useEffect(() => {
      const fetchData = async () => {
        try {
          const response = await fetch('http://127.0.0.1:5000/get_data');
          const jsonData = await response.json();
          setData(jsonData);
        } catch (error) {
          console.error('Error fetching data: ', error);
        }
      };
      
      fetchData();
    }, []);

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
        <h1>JSON Data:</h1>
      <ul>
        {data.map((item, index) => ( //change the whole think only use for testing
          <li key={index}>
            <p>Name: {item.name}</p>
            <p>Price: {item.price}</p>
          </li>
        ))}
      </ul>
        </div>
      </div>
  );
}

export default App;
