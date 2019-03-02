$(document).ready(function() {
  var chartValues = chartTemps_all();
});

function new_TempChart(labels, data) {
  //Create the chart
  //console.log(labels);
  //console.log(data);

  var ctx = document.getElementById("kitchen-temp").getContext('2d');
  var tempChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: labels,
      datasets: [{
        data: data,
        label: "Temperature"
      }]
    },
    options: {
      title: {
        display: true,
        text: "All Temperatures"
      }
    }
  });
}

function chartTemps_all() {

  //Get API data
  $.getJSON('/api/TempModel/?format=json', {
    format: "json"
  }).done(function(data){
    console.log(data);

    var newDateArr = data.map(function(e) {
      return e.date;
    });

    var newTempArr = data.map(function(e) {
      return e.temperature_f;
    });

    //console.log(newDateArr);
    //console.log(newTempArr);

    new_TempChart(newDateArr, newTempArr);
  });
}

function chartTemps(room) {
  $.getJSON('/api/TempModel/?format=json', {
    format: "json"
  }).done(function(data){
    //console.log(data);

    //Init empty arrays for date and temp
    var dateArr = [];
    var tempArr = [];

    $.each(data, function(i, item) {
      //console.log(item);
      if (item.room = room) {
        //console.log(item.date);
        //console.log(item.temperature_f);

        dateArr.push(item.date);
        tempArr.push(item.temperature_f);
      }
    })
  })
}
