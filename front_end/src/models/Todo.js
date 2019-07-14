export default class Todo {
  constructor(content, createdOn) {
    this.content = content || "";
    this.createdOn = createdOn || new Date();
    this.isDone = false;
  }
}