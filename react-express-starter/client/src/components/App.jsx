import React, { Component } from 'react';
import SearchFoodForm from './SearchFoodForm.jsx';
import FoodItemList from './FoodItemList.jsx';
import axios from 'axios';
import CreateFoodForm from './CreateFoodForm.jsx';

class App extends Component {
  
  constructor(props) {
    super(props);
    this.state = {
      foodItems: []
    };
  }

  componentDidMount() {
    axios.get("http://127.0.0.1:8000/api/v1/fooditems/")
    .then(res => {
      console.log(res);
      this.setState({
      foodItems: res.data.results
      });
    })
    .catch(error => {
      // handle error
      console.log(error);
    })
    
    
  }

  render() {
    return (
      <div>
        <CreateFoodForm/>
        <SearchFoodForm/>
        <FoodItemList  foodItems={this.state.foodItems}/>
      </div>
    );
  }
}

export default App;