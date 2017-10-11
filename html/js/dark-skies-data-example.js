Vue.use(VueEventCalendar.default, {locale: 'en', color: '#4fc08d'}) //hack here (.default)
new Vue({
  el: '#example',
  data: function () {
    return {
      demoEvents: [{
        date: '2017/10/15',
        title: 'Adam -- Title1',
        desc: 'longlonglong description'
      },{
        date: '2017/10/12',
        title: 'Adam - Title2',
        desc: 'aaa'
      }]
    }
  }
})