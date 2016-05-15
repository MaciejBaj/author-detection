import * as React from 'react';
import * as Dropzone from 'react-dropzone';
import {FilesList} from './files-list';

interface IDropText extends React.Props<any> {
  textChange: Function;
}

export class DropText extends React.Component<IDropText, void> {

  state: any;
  fileReader: FileReader;
  
  constructor(props) {
    super(props);
    this.state = {files: []};
    this.fileReader = new FileReader();
    this.fileReader.onload = event => this.props.textChange(event.target.result);
  }

  onDrop(files) {
    console.log('Received files: ', files);
    this.setState({files});
    this.fileReader.readAsText(files[0]);
  }

  render() {
    return (
      <div className="dropzone-container">
        <Dropzone onDrop={this.onDrop.bind(this)}>
          <div>Try dropping some files here, or click to select files to upload.</div>
        </Dropzone>
        {this.state.files ? <FilesList files={ this.state.files } />: null }
      </div>
    );
  }
}
