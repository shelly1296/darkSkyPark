<template>
    <div id="dspapp">
        <h1>Dark Sky Data View</h1>
        <h2 class="t-center mt150">Please select a date to see the graph and data for that day</h2>
        <vue-event-calendar :events="darkSkyEvents">
            <template scope="props">
                <div v-for="(event, index) in props.showEvents" class="event-item">
                    <h3 class="title">{{index+1}}. {{event.title}}</h3>

                    <p v-if="typeof(event.desc ) !== 'undefined' && event.desc !== ''" class="desc">{{event.desc}}</p>
                    <p v-else>No Graph</p>
                    {{event}}
                </div>
            </template>
        </vue-event-calendar>
    </div>
</template>

<script>
  let today = new Date();
  export default {
    name: 'app',
    data () {
      return {
        darkSkyEvents: [{
          date: `${today.getFullYear()}/${today.getMonth() + 1}/${today.getDate()}`,
          title: 'Title-1',
          desc: 'longlonglong description'
        },{
          date: `${today.getFullYear()}/${today.getMonth() + 1}/${today.getDate()}`,
          title: 'Title-1',
          desc: 'longlonglong description'
        },{
          date: `${today.getFullYear()}/${today.getMonth() + 1}/${today.getDate()}`,
          title: 'Title-1',
          desc: 'longlonglong description'
        },{
          date: `${today.getFullYear()}/${today.getMonth() + 1}/${today.getDate()}`,
          title: 'Title-1',
          desc: 'longlonglong description'
        },{
          date: `${today.getFullYear()}/${today.getMonth() + 1}/${today.getDate()}`,
          title: 'Title-1',
          desc: 'longlonglong description'
        },{
          date: `${today.getFullYear()}/${today.getMonth() + 1}/${today.getDate()}`,
          title: 'Title-1',
          desc: 'longlonglong description'
        },{
          date: `${today.getFullYear()}/${today.getMonth() + 1}/15`,
          title: 'Title-1',
          desc: 'longlonglong description'
        },{
          date: `${today.getFullYear()}/${today.getMonth() + 1}/24`,
          title: 'Title-2'
        },{
          date: `${today.getFullYear()}/${today.getMonth() === 11 ? 1 : today.getMonth() + 2}/06`,
          title: 'Title-3',
          desc: 'description'
        }]
      }
    },
    methods: {
      handleDayChanged (data) {
      },
      handleMonthChanged (data) {
      }
    }
  }
</script>

<style>
    #dspapp {
        font-family: 'Avenir', Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        color: #2c3eF0;
        margin-top: 30px;
    }

    h1, h2, h3 {
        font-weight: normal;
        margin: 0;
        padding: 0;
    }

    ul {
        list-style-type: none;
        padding: 0;
    }

    li {
        display: inline-block;
        margin: 0 10px;
    }

    a {
        color: #42b983;
    }

    .t-center {
        text-align: center;
        margin: 20px;
    }

    .mt150 {
        margin-top: 150px;
    }
</style>
