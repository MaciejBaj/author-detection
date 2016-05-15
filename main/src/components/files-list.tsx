import * as React from 'react';

interface IFilesList extends React.Props<any> {
  files: File[]
}

export class FilesList extends React.Component<IFilesList, void> {
  render() {
    return <ul className="preview-file-container"> {this.props.files.map(file => <li>{file.name}</li>)} </ul>
  }
}