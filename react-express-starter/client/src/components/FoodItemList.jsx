import React from 'react';
import FoodItem from './FoodItem.jsx';

const FoodItemList = ({foodItems}) =>{
    console.log(foodItems);
    return (
    
        <div className="list-wrapper">
        {foodItems.map(foodItem => <FoodItem foodItem={foodItem} />)}
        </div>
    )
} 

export default FoodItemList;

