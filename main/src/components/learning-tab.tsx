import * as React from 'react';
import { Paper, TextField, Checkbox} from 'material-ui';
import {DropText} from './drop-text';

interface ILearningTab extends React.Props<any> {}

export class LearningTab extends React.Component<ILearningTab, void> {

  state: any = {
    text: ''
  };

  render() {
    return (
      <Paper className="tab-content">
        <h5 className="attribute-checkbox">Text classes:</h5>
        <iframe name="hiddenFrame" className="hidden-frame"></iframe>
        <form name="add-new-text" target="hiddenFrame" action="http://localhost:7001/parse" method="post" acceptCharset="UTF-8" encType="application/x-www-form-urlencoded">
        <fieldset>
          <TextField
            className="attribute-text-field"
            name="author"
            floatingLabelText="author"
          />
          <TextField
            className="attribute-text-field"
            name="type"
            floatingLabelText="type"
          />
          <TextField
            className="attribute-text-field"
            name="age"
            floatingLabelText="age"
          />
          <TextField
            className="attribute-text-field"
            name="male"
            floatingLabelText="male"
          />
        </fieldset>
        <TextField
          name="text"
          hintText="type a text"
          floatingLabelText="text to recognize"
          value={this.state.text}
          multiLine={true}
          onChange={event => this.setState({text: event.target.value})}
          fullWidth={true}
          rowsMax={20}
          rows={5}
        />
        <br />
        <DropText textChange={(text) => this.setState({text})}/>
        <button type="submit">submit</button>
        
        </form>
      </Paper>
    );
  }
}
