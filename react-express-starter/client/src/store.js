import {createStore, combineReducers} from 'redux';
import {foodItems} from './reducers';

const reducers = {
    foodItems,
};

const rootReducer = combineReducers(reducers);

export const configureStore = () => createStore(rootReducer);