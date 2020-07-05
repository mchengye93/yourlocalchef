import React from 'react';

const FoodItem = ({foodItem}) => {
    console.log(foodItem);
    return (
    <div className="food-item-container">
    <h2>{foodItem.name}</h2>
    <div>
        {foodItem.description}
    </div>
    <div>
        Price: {foodItem.price}
    </div>
    </div>
    
    )
}
export default FoodItem;