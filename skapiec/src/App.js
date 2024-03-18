import "./App.css";
import SearchIcon from "./search.svg";
import React, { useState, useEffect } from "react";

const App = () => {
  //fetching data
  const [searchItem, setSearchItem] = useState("");
  const [items, setItems] = useState([]);
      useEffect(() => {
      searchItems("");
  }, []);

  const searchItems = async (search) => {

      await fetch(`https://www.igorgawlowicz.pl/skapiec/scrape?phrase=${search}`);
      const response = await fetch(`https://www.igorgawlowicz.pl/skapiec/get_data?phrase=${search}&pages=${1}`);
      const data = await response.json();
      setItems(data);
      
      if (data && Array.isArray(data) && data.length > 0) {
        data.forEach((item, index) => {
          if (item.photo) {
            localStorage.setItem(`photoURL_${index}`, item.photo);
          }
        });
        console.log('Photos URLs saved to local storage:', data.map(item => item.photo));
      }
      //piotrek to cipa JEBANA I MNIE WKURWIA
  };

  const handleKeyPress = (e) => {
    if (e.key === "Enter") {
      searchItems(searchItem);
    }
  };

  return (
    <div className="app">
      <h1>Skrapiec</h1>
      <div className="search">
        <input
          value={searchItem}
          onChange={(e) => setSearchItem(e.target.value)}
          placeholder="Search for items"
          onKeyDown={handleKeyPress}
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
            <div className="top"></div>

            <a
              href={item.external_url}
              target="_blank"
              rel="noopener noreferrer"
            >
              <div
                className="img"
                style={{ backgroundImage: `url('${item.photo}')` }}
              >
                {" "}
              </div>
            </a>

            <div className="Text-container">
              <h3>{item.name && item.name.split(" ").slice(0, 6).join(" ")}</h3>
              <span>{item.price}</span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default App;
