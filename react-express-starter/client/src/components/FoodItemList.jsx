import React from 'react';
import FoodItem from './FoodItem.jsx';
import { connect } from 'react-redux';


const FoodItemList = ({foodItems}) =>{
    console.log(foodItems);
    return (
    
        <div className="list-wrapper">
        {foodItems.map(foodItem => <FoodItem foodItem={foodItem} key={foodItem.id} />)}
        </div>
    )
} 
// const mapStateToProps = state => ({
//     foodItems: state.foodItems,
// })


// export default connect(mapStateToProps)(FoodItemList);
export default FoodItemList;

