import { SEARCH_FOOD_ITEM, CREATE_FOOD_ITEM } from './action.js';

export const foodItems = (state= [],action) => {
    const {type,payload} = action;
    switch (type) {
        case SEARCH_FOOD_ITEM: {
            return state
        }
        case CREATE_FOOD_ITEM: {
            const {foodItem} = payload;
            const newFoodItem = {
                foodItem
            };
            return state.concat(newFoodItem);
        }

        default:
            return state
    }
}