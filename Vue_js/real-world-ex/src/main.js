import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import upperFirst from 'lodash/upperFirst'
import camelCase from 'lodash/camelCase'
// second way to import global component
import BaseIcon from '@/components/BaseIcon.vue'

// make a vue component with the imported component
Vue.component('BaseIcon', BaseIcon)

const requireComponent = require.context(
  // First item is the directory to search, second item is if you want to search subdirectories, third is a regex of what to look for
  './components',// the relative path of the directory to search
  false,// subdirectories will not be searched
  /Base[A-Z]\w+\.(vue|js)$/ // regular expression that searches for components starting with "Base" and ending in .vue or .js
)

requireComponent.keys().forEach(fileName => {
  // .keys is an array of all file in the folder
  const componentConfig = requireComponent(fileName)
  // convert the filename, all to camel case
  const componentName = upperFirst(
    camelCase(fileName.replace(/^\.\/(.*)\.\w+$/, '1')) // removes what's before and after the filename itself
  )

  Vue.component(componentName, componentConfig.default || componentConfig)
})


Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
