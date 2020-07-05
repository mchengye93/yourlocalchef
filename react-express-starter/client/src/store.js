import {createStore, combineReducers} from 'redux';

const reduces = {};

const rootReduce = combineReducers(reducers);

export const configureStore = () => createStore(rootReducer);