<template>
  <div id="app">
    <div class="page-container">
      <md-app>
        <md-app-toolbar class="md-primary" md-elevation="0">
          <md-button class="md-icon-button" v-if="!menuVisible">
            <md-icon>menu</md-icon>
          </md-button>
          <span class="md-title">My Day</span>
        </md-app-toolbar>

        <md-app-drawer :md-active.sync="menuVisible" md-persistent="mini">
          <md-toolbar class="md-transparent" md-elevation="0">
            <span>User Icon & Ids</span>

            <div class="md-toolbar-section-end">
              <md-button class="md-icon-button md-dense">
                <md-icon>search</md-icon>
              </md-button>
            </div>
          </md-toolbar>

          <md-list>
            <md-list-item>
              <md-icon>wb_sunny</md-icon>
              <span class="md-list-item-text" @click="clickListName('001')">My Day</span>
            </md-list-item>

            <md-list-item>
              <md-icon>star_border</md-icon>
              <span class="md-list-item-text" @click="clickListName('002')">Important</span>
            </md-list-item>

            <md-list-item>
              <md-icon>calendar_today</md-icon>
              <span class="md-list-item-text" @click="clickListName('003')">Planned</span>
            </md-list-item>

            <md-list-item>
              <md-icon>done</md-icon>
              <span class="md-list-item-text" @click="clickListName('004')">Tasks</span>
            </md-list-item>
          </md-list>
        </md-app-drawer>

        <md-app-content>
          <TodoList :todoListCode="todoListCode"></TodoList>
        </md-app-content>
      </md-app>
    </div>
  </div>
</template>

<script>
import TodoList from "@/components/TodoList";
export default {
  data() {
    return {
      curInput: "",
      menuVisible: true,
      todoListCode: ""
    };
  },
  methods: {
    clickListName(code) {
      this.todoListCode = code;
    }
  },
  components: {
    TodoList: TodoList
  }
};
</script>

<style scoped>
.md-app {
  min-height: 350px;
  border: 1px solid rgba(#000, 0.12);
}

.md-drawer {
  width: 230px;
  max-width: calc(100vw - 125px);
}
</style>


