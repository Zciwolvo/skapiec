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
    await fetch(`http://127.0.0.1:5000/scrape?phrase=${search}`); //to jest zepsute, zmienilem na potrzeby testow

    const response = await fetch(
      `http://127.0.0.1:5000/get_data?phrase=${search}`
    ); //to jest zepsute, zmienilem na potrzeby testow
    const data = await response.json();

    setItems(data);
    console.log(search);
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
