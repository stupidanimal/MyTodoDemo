<template>
  <div>
    <!-- <md-card> -->
    <!-- <md-card-media-cover>
        <div class="todo-media"></div>
        <md-card-area>
          <md-card-header>
            <div class="md-title">My Day</div>
          </md-card-header>
        </md-card-area>
    </md-card-media-cover>-->

    <!-- <md-card-content> -->
    <md-list v-for="(todo,index) in todoList" v-bind:key="index">
      <md-list-item>
        <span class="md-list-item-text" :class="{linethrough:todo.isDone}">
          <md-checkbox
            v-model="todo.isDone"
            class="md-primary"
            @click="doneOrNot(todo)"
          >{{todo.content}}</md-checkbox>
        </span>
      </md-list-item>
    </md-list>
    <md-field>
      <md-input v-model="curInput" placeholder="Add a task" v-on:keydown.enter="addNewTask"></md-input>
    </md-field>
    <!-- </md-card-content>
    </md-card>-->
  </div>
</template>
<script>
import Todo from "@/models/Todo";
export default {
  data() {
    return {
      curInput: "",
      todoList: [
        new Todo("Shopping", "", true),
        new Todo("Work"),
        new Todo("Jogging"),
        new Todo("Reading")
      ]
    };
  },
  methods: {
    doneOrNot(todo) {
      todo.isDone = !todo.isDone;
    },
    addNewTask() {
      let todo = new Todo(this.curInput);
      this.todoList.push(todo);
      this.curInput = "";
    }
  }
};
</script>
<style scoped>
.todo-media {
  width: 100%;
  height: 170px;
  background: linear-gradient(to right, green 30%, gold);
}
.linethrough {
  text-decoration: line-through;
}
</style>
