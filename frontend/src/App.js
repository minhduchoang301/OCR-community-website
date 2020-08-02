import React, { Component } from 'react';
import './App.css';
import {CustomInput, Button, FormGroup, Jumbotron} from 'reactstrap';
import axios from 'axios';

class App extends Component {
  state = {
    selectedFile: null
  };

  onFileChange = (e) => {
    this.setState({selectedFile: e.target.files[0]});
  }

  onFileUpload = () => {
    const formData = new FormData();
    if (this.state.selectedFile) {
      formData.append('file', this.state.selectedFile, this.state.selectedFile.name);
    }
    axios.post('http://localhost:3001/upload', formData)
    .then((response) => {
      console.log(response);
    }
    ).catch((error) => {
      console.log(error);
    })
  }

  render() {
    return (
      <div className="App">
        <Jumbotron>
          <h1>OCR Project</h1>
          <h3>Read text from images</h3>
        </Jumbotron>
        <FormGroup className="form">
          <CustomInput onChange={this.onFileChange} type='file' label='Upload a file here' id='input'/>
          <Button style={{'margin': '20px'}} onClick={this.onFileUpload}>Upload</Button>
        </FormGroup>
      </div>
    );
  }
}

export default App;
