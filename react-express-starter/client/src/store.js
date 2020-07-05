import {createStore, combineReducers} from 'redux';
import {foods} from './reducers';

const reducers = {
    foods,
};

const rootReducer = combineReducers(reducers);

export const configureStore = () => createStore(rootReducer);