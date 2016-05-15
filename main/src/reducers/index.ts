import { combineReducers } from 'redux';
import { routerReducer } from 'react-router-redux';
import { reducer as formReducer } from 'redux-form';
import counter from './counter';


const rootReducer = combineReducers({
  counter,
  routing: routerReducer,
  form: formReducer,
});


export default rootReducer;
