import React, {useState} from 'react';

const SearchFoodForm = () => {
    
    const [inputValue,setInputValue] = useState('');
    return (
    
    <div className="search-food-form">
        <form>
            <input 
            type="text"
            placeholder="Search food"
            value={inputValue}
            onChange={e => setInputValue(e.target.value)}/>
            <button>Search</button>
        </form>
    </div>
    )
}

export default SearchFoodForm;