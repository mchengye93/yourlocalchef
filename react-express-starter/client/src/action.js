export const SEARCH_FOOD = 'SEARCH_FOOD';
export const searchFood = () => ({  
        type: SEARCH_FOOD,
        payload: {},
           
});

export const CREATE_FOOD = 'CREATE_FOOD';
export const createFood = (food) => ({  
        type: CREATE_FOOD,
        payload: {food},
           
});

