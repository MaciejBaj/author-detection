import * as React from 'react';
import { connect } from 'react-redux';
import { Link } from 'react-router';
import { RaisedButton, AppBar, Styles, Tab, Tabs, Paper, TextField, Divider, Checkbox} from 'material-ui';
//https://github.com/callemall/material-ui/blob/master/docs/src/app/components/pages/customization/themes.jsx
import { ThemeManager } from 'material-ui/lib/styles/theme-manager';
import {RecognitionTab} from  '../components/recognition-tab';
import {LearningTab} from  '../components/learning-tab';

interface IAppProps extends React.Props<any> {
  muiTheme: Object;
}

function mapStateToProps(state) {
  return {
    router: state.router,
  };
}

function mapDispatchToProps(dispatch) {
  return { };
}

class App extends React.Component<IAppProps, void> {

  public render() {
    const { children } = this.props;
    return (
      <div>
        <AppBar className="app-bar" title="Characteristics recognition" iconElementLeft={<p></p>}/>
        <Tabs>
          <Tab label="Recognition" >
            <RecognitionTab></RecognitionTab>
          </Tab>
          <Tab label="Learning" >
            <LearningTab></LearningTab>
          </Tab>
        </Tabs>
      </div>
    );
  };

}


export default connect(
  mapStateToProps,
  mapDispatchToProps
)(App);
