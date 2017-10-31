import Vue from 'vue'
import VueEventCalendar from 'vue-event-calendar'
import App from './dark-sky-data.vue'

Vue.use(vueEventCalendar, {locale: 'en'})

window.Vue = Vue
new Vue({
  el: '#dspapp',
  render: h => h(App)
});
