export const SEARCH_FOOD_ITEM = 'SEARCH_FOOD_ITEM';
export const searchFoodItem = () => ({  
        type: SEARCH_FOOD_ITEM,
        payload: {},
           
});

export const CREATE_FOOD_ITEM = 'CREATE_FOOD_ITEM';
export const createFoodItem = (foodItem) => ({  
        type: CREATE_FOOD_ITEM,
        payload: {foodItem},
           
});

