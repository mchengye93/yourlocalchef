import { SEARCH_FOOD, CREATE_FOOD } from './action.js';

export const foods = (state= [],action) => {
    const {type,payload} = action;
    switch (type) {
        case SEARCH_FOOD: {
            return state
        }
        case CREATE_FOOD: {
            const {food} = payload;
            const newFood = {
                food
            };
            return state.concat(newFood);
        }

        default:
            return state
    }
}