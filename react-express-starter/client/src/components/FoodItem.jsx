import React from 'react';

const FoodItem = ({foodItem}) => {
    console.log(foodItem);
    return (
    <div className="food-item-container">
    <img src={foodItem.image} alt={foodItem.name+' image'} width="150" height="150"></img>
    <h3>{foodItem.name}</h3>
    <p>
        {foodItem.description}
    </p>
    <div>
        Price: {foodItem.price}
    </div>
    </div>
    )
}

export default FoodItem;