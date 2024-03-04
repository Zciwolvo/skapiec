import React from 'react';

const jsonItem = ({ item }) => {
  return (
    <div className="item" key={item.id}>
      <div>
        <p>{item.price}</p>
      </div>

      <div>
        <img src={item.photo} alt={item.name} />
      </div>

      <div>
        <span>{item.price}</span>
        <h3>{item.name}</h3>
      </div>
    </div>
  );
}

export default jsonItem;