import Vue from 'vue'
import vueEventCalendar from 'vue-event-calendar'
import DSPApp from './dark-sky-data.vue'

Vue.use(vueEventCalendar, {locale: 'en'});

window.Vue = Vue;
new Vue({
  el: '#dspapp',
  render: h => h(DSPApp)
});
