import React, { Component } from "react";
import {
  Button,
  Modal,
  ModalHeader,
  ModalBody,
  ModalFooter,
  Form,
  FormGroup,
  Input,
  Label,
} from "reactstrap";

export default class CustomModal extends Component {
  constructor(props) {
    super(props);
    this.state = {
      activeItem: this.props.activeItem,
    };
  }

  handleChange = (e) => {
    let { name, value } = e.target;

    if (e.target.type === "checkbox") {
      value = e.target.checked;
    }

    const activeItem = { ...this.state.activeItem, [name]: value };

    this.setState({ activeItem });
  };

  render() {
    const { toggle, onSave } = this.props;

    return (
      <Modal isOpen={true} toggle={toggle}>
        <ModalHeader toggle={toggle}>Book</ModalHeader>
        <ModalBody>
          <Form>
            <FormGroup>
              <Label for="book-title">Title</Label>
              <Input
                type="text"
                id="book-title"
                name="title"
                value={this.state.activeItem.title}
                onChange={this.handleChange}
                placeholder="Enter Book Title"
              />
            </FormGroup>
            <FormGroup>
              <Label for="book-authors">Title</Label>
              <Input
                type="text"
                id="book-authors"
                name="authors"
                value={this.state.activeItem.authors}
                onChange={this.handleChange}
                placeholder="Enter Authors"
              />
            </FormGroup>
            <FormGroup>
              <Label for="book-description">Description</Label>
              <Input
                type="text"
                id="book-description"
                name="description"
                value={this.state.activeItem.description}
                onChange={this.handleChange}
                placeholder="Enter Book description"
              />
            </FormGroup>
            <FormGroup check>
              <Label check>
                <Input
                  type="checkbox"
                  name="isInStock"
                  checked={this.state.activeItem.isInStock}
                  onChange={this.handleChange}
                />
                In Stock
              </Label>
            </FormGroup>
          </Form>
        </ModalBody>
        <ModalFooter>
          <Button
            color="success"
            onClick={() => onSave(this.state.activeItem)}
          >
            Save
          </Button>
        </ModalFooter>
      </Modal>
    );
  }
}