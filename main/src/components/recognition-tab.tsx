import * as React from 'react';
import * as $ from 'jquery';

import {Paper, TextField, Checkbox} from 'material-ui';
import {DropText} from './drop-text';
import EventHandler = __React.EventHandler;
import FormEvent = __React.FormEvent;

interface IRecognitionTab extends React.Props<any> { }

export class RecognitionTab extends React.Component<IRecognitionTab, void> {

  state: any;

  constructor(props) {
    super(props);
    this.state = {
      text: '',
      result: null
    }
  }

  render() {
    const results = this.state.result ?
      <fieldset>
        <h5 >results</h5>
        <pre>{this.state.result}</pre>
        <br />
      </fieldset> : <p></p>;
    return (
      <Paper className="tab-content">
        <form onSubmit={ (e) => this.submitResult(e)}>
          <fieldset>
            <h5 className="attribute-checkbox">attributes to recognize:</h5>

            <Checkbox
              name="classes.author"
              label="author"
              defaultChecked={true}
              className="attribute-checkbox"
            />
            <Checkbox
              name="classes.type"
              label="type"
              defaultChecked={true}
              className="attribute-checkbox"
            />
            <Checkbox
              name="classes.male"
              label="male"
              defaultChecked={true}
              className="attribute-checkbox"
            />
            <TextField
              name="text"
              hintText="type or drop a text"
              floatingLabelText="text to recognize"
              value={this.state.text}
              multiLine={true}
              onChange={event => this.setState({text: event.target.value})}
              fullWidth={true}
              rowsMax={20}
              rows={5}
            />
            <DropText textChange={(text: string) => this.setState({text})}/>

            <button type="submit">submit</button>
          </fieldset>
        </form>
        {
          results
        }

      </Paper>
    );
  }

  submitResult(e) {
    e.preventDefault();
    $.ajax({
      url: 'http://localhost:7001/recognize',
      dataType: 'json',
      cache: false,
      type: 'POST',
      data: {text: this.state.text},
      success: function (data) {
        console.log('get response: ', data);
        this.setState({result: JSON.stringify(data, null, 2)});
      }.bind(this),
      error: function (xhr, status, err) {
        console.error(this.props.url, status, err.toString());
      }.bind(this)
    });
  }
}

//var c = [{
//  "age": {
//    "numerical_classification": "mloda polska",
//    "top_common_words": "mloda polska",
//    "parts_of_speech_frequencies_classification": "barok"
//  }
//}, {
//  "male": {
//    "numerical_classification": "man",
//    "top_common_words": "man",
//    "parts_of_speech_frequencies_classification": "man"
//  }
//}, {
//  "type": {
//    "numerical_classification": "sonet",
//    "top_common_words": "hymn",
//    "parts_of_speech_frequencies_classification": "sonet"
//  }
//}, {
//  "author": {
//    "numerical_classification": "Adam Mickiewicz",
//    "top_common_words": "Jan Kasprowicz",
//    "parts_of_speech_frequencies_classification": "Adam Mickiewicz"
//  }
//}]
