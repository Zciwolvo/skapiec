import "./App.css";
import SearchIcon from "./search.svg";
import React, { useState, useEffect } from "react";

const App = () => {
  //fetching data
  const [searchItem, setSearchItem] = useState("");
  const [items, setItems] = useState([]);
  const [cachedData, setCachedData] = useState(null);
  useEffect(() => {
    const cachedItems = JSON.parse(localStorage.getItem("items"));
    if (cachedItems) {
      setItems(cachedItems);
      setCachedData(cachedItems);
    } else {
      searchItems("");
    }
  }, []);

  const searchItems = async (search) => {
    if (!cachedData || (cachedData && !cachedData.some(item => item.name.includes(search)))) {
      await fetch(`https://www.igorgawlowicz.pl/skapiec/scrape?phrase=${search}`);
      const response = await fetch(`https://www.igorgawlowicz.pl/skapiec/get_data?phrase=${search}`);
      const data = await response.json();
      localStorage.setItem("items", JSON.stringify(data));
      setItems(data);
      setCachedData(data);
    } else {
      const filteredItems = cachedData.filter(item => item.name.includes(search));
      setItems(filteredItems);
    }
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
