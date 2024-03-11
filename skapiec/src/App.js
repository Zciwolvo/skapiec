import './App.css';
import SearchIcon from './search.svg';
import React, { useState, useEffect } from 'react';


const App = () => {
  //fetching data
  const [searchItem, setSearchItem] = useState("");
  const [items, setItems] = useState([]);
    useEffect(() => {
      searchItems("");
    }, []);
  
    const searchItems = async (search) => {
      
      await fetch(`https://igorgawlowicz.pythonanywhere.com/skapiec/scrape?phrase=${search}`);

      const response = await fetch(`https://igorgawlowicz.pythonanywhere.com/skapiec/get_data?phrase=${search}`);
      const data = await response.json(); 
      
      setItems(data);
      console.log(search)
    };



    
    return (
      <div className="app">
          <h1>Skrapiec</h1>
          <div className="search">
            <input
              value={searchItem}
              onChange={(e) => setSearchItem(e.target.value)}
              placeholder="Search for items"
            />
          <img
            src={SearchIcon}
            alt="search"
            onClick={() => searchItems(searchItem)}
          />
        </div>
  
          <div className="container">
              {items.map((item) => (
                  <div className="item" key={item}>
                    <div className="top">
                    </div>
                      
                    <a href={item.external_url} target="_blank" rel="noopener noreferrer"> {/* Added anchor tag */}
                    <div className="img" style={{ backgroundImage: `url('${item.photo}')` }}>
                    </div>
                      </a>

                    <div className="Text-container">
                      <h3>{item.name}</h3>
                      <span>{item.price}</span>
                    </div>
                </div>                        
            ))}
          </div>
      </div>
    );
  };
  
  export default App;
