import * as React from 'react';
import { connect } from 'react-redux';
import { increment, decrement } from '../actions/counter';
import Counter from '../components/counter';


interface ICounterPageProps extends React.Props<any> {
  counter: number;
  increaseCounter: () => void;
  decreaseCounter: () => void;
}

function mapStateToProps(state) {
  return {
    counter: state.counter.get('count'),
  };
}

function mapDispatchToProps(dispatch) {
  return {
    increaseCounter: (): void => dispatch(increment()),
    decreaseCounter: (): void  => dispatch(decrement()),
  };
}

class CounterPage extends React.Component<ICounterPageProps, void> {
  render() {
    const { counter, increaseCounter, decreaseCounter } = this.props;

    return (
      <div>
        <h1 className="center">Counter</h1>
        <Counter
          counter={ counter }
          increment={ increaseCounter }
          decrement={ decreaseCounter } />
      </div>
    );
  };
}

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(CounterPage);
