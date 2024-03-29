import "./App.css";
import React, { useState, useEffect } from "react";

const App = () => {
  //fetching data
  const [selectedPage, setSelectedPage] = useState("1");
  const [searchItem, setSearchItem] = useState("");
  const [items, setItems] = useState([]);
  useEffect(() => {
    searchItems("");
  }, []);

  const searchItems = async (search) => {
    await fetch(
      `https://www.igorgawlowicz.pl/skapiec/scrape?phrase=${search}&page=${selectedPage}`
    );
    const response = await fetch(
      `https://www.igorgawlowicz.pl/skapiec/get_data?phrase=${search}`
    ); // Concatenate selectedPage to the URL
    const data = await response.json();
    setItems(data);
  };

  const handleKeyPress = (e) => {
    if (e.key === "Enter") {
      searchItems(searchItem);
    }
  };

  return (
    <div className="app">
      <h1>Skrapiec</h1>

      <div className="input-group">
        <input
          type="text"
          className="form-control"
          aria-label="Text input with segmented dropdown button"
          value={searchItem}
          onChange={(e) => setSearchItem(e.target.value)}
          placeholder="Search for items"
          onKeyDown={handleKeyPress}
        />

        <div className="input-group-append">
          <button
            type="button"
            className="btn btn-outline-secondary"
            onClick={() => searchItems(searchItem)}
          >
            Search
          </button>
          <button
            type="button"
            className="btn btn-outline-secondary dropdown-toggle dropdown-toggle-split"
            data-bs-toggle="dropdown"
            aria-haspopup="true"
            aria-expanded="false"
          >
            <span className="sr-only">{selectedPage}</span>
          </button>
          <div className="dropdown-menu">
            {[1, 2, 3, 4, 5].map((page) => (
              <p
                key={page}
                className="dropdown-item"
                onClick={() => setSelectedPage(page)}
              >
                {page}
              </p>
            ))}
          </div>
        </div>
      </div>

      <div className="container">
        {items.map((item) => (
          <div className="item" key={item.id}>
            <a
              href={item.external_url}
              target="_blank"
              rel="noopener noreferrer"
            >
              <img className="img" src={item.photo} alt="an item" />
            </a>

            <div className="text-container">
              <h3>{item.name && item.name.split(" ").slice(0, 6).join(" ")}</h3>
              <span className="price">{item.price}</span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default App;
