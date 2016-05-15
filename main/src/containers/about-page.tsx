import * as React from 'react';
import { connect } from 'react-redux';

interface IAboutPageProps extends React.Props<any> {};

function mapStateToProps() {
  return {};
}

function mapDispatchToProps() {
  return {};
}

class AboutPage extends React.Component<IAboutPageProps, void> {
  render() {
    return (
      <h1>About maci2o</h1>
    );
  }
};

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(AboutPage);
