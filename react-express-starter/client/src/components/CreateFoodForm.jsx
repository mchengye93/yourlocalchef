import React from 'react';
import axios from 'axios';

class CreateFoodForm extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
            user: '1',
            name:'',
            description:'',
            // image:'',
            price: '',
    };
  
      this.handleChange = this.handleChange.bind(this);
      this.handleSubmit = this.handleSubmit.bind(this);
    }
  
    handleChange(e) {
      this.setState({[e.target.name]: e.target.value});
    }
  
    handleSubmit(event) {
      axios.post('http://127.0.0.1:8000/api/v1/fooditems/new',this.state)
      .then((res) => {
          console.log("Response status: " + res.status);    
      }).catch((error) => {
          console.log("Error:" + error)
      });

      event.preventDefault();
    }
  
    render() {
      return (
        <form onSubmit={this.handleSubmit}>
          <label>
            Name:
            <input type="text" name="name" value={this.state.value} onChange={this.handleChange} />
          </label>
          <label>
            Description:
            <input type="text" name="description" value={this.state.value} onChange={this.handleChange} />
          </label>
          <label>
            Price:
            <input type="text" name="price" value={this.state.value} onChange={this.handleChange} />
          </label>
          {/* <input type="file"
        name="image"
       accept="image/png, image/jpeg"></input>*/}
          <input type="submit" value="Submit" /> 
        </form>
      );
    }
  }

  export default CreateFoodForm;