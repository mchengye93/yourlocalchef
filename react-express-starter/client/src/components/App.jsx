import React, { Component } from 'react';
import SearchFoodForm from './SearchFoodForm.jsx';
import FoodItemList from './FoodItemList.jsx';

class App extends Component {
  
  render() {
    return (
      <div>
        <SearchFoodForm/>
        <FoodItemList  foodItems={[{name:'Pineapple Bun', description:'Pineaple', price:1.90}]}/>
      </div>
    );
  }
}

export default App;