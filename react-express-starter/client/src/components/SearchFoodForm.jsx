import React, {useState} from 'react';
import { connect } from 'react-redux';
import { searchFoodItem } from '../action.js';


const SearchFoodForm = ({onSearchPressed}) => {
    
    const [inputValue,setInputValue] = useState('');
    return (
    
    <div className="search-food-form">
        <form>
            <input 
            type="text"
            placeholder="Search food"
            value={inputValue}
            onChange={e => setInputValue(e.target.value)}/>
            <button onClick={()=> {
                onSearchPressed(inputValue);
                setInputValue('');
            }}>Search</button>
        </form>
    </div>
    )
}


// const mapDispatchToProps = dispatch => ({
//     onSearchPressed:() => dispatch(searchFoodItem())
// });
    
// export default connect(null,mapDispatchToProps)(SearchFoodForm);
export default SearchFoodForm;