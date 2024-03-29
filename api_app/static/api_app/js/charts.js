function chartTemps_all(datapoints, isDisplayEnabled) {
  //Get API data
  $.getJSON('/api/TempModel/', {
    format: "json"
  }).done(function(data){
    console.log(data);

    //why e? I should rename this
    var newDateArr = data.map(function(e) {
      return e.date;
    });

    var newTempArr = data.map(function(e) {
      return e.temperature_f;
    });

    new_TempChart(newDateArr, newTempArr, "All Temperatures", isDisplayEnabled);
  });
}

function chartTemps(room, datapoints, isDisplayEnabled) {
  $.getJSON('/api/temperatures/' + room + '/' + datapoints, {
  }).done(function(data){
    console.log(data);
    console.log(data.reverse());

    var newDateArr = $.map(data, function(e) {
      return new Date(e.fields.date).toLocaleString();
    });

    var newTempArr = $.map(data, function(e) {
      console.log(e.fields.temperature_f)
      return e.fields.temperature_f;
    });

    console.log(newDateArr);
    new_TempChart(newDateArr, newTempArr, room, isDisplayEnabled);
  });
}

function new_TempChart(labels, data, room, isDisplayEnabled) {
  //Create the chart
  var ctx = document.getElementById(room + "-temp").getContext('2d');

  var tempChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: labels,
      datasets: [{
        data: data,
        label: "Temperature",
        //backgroundColor: ['rgba(115, 134, 213, .4)']
      }]
    },
    options: {
      scales: {
        xAxes: [{
          display: isDisplayEnabled //false or true
        }]
      },
      title: {
        display: true,
        text: room,
      },
      responsive: true,
      maintainAspectRatio: false,
      responsiveAnimationDuration: 30,
    }
  });
}

function addDatapoint() {
  var oldVal = +$('#datapoints-input').val();
  var newVal = (oldVal + 1);

  $('#datapoints-input').val(newVal);
}

function subDatapoint() {
  var oldVal = +$('#datapoints-input').val();
  var newVal = (oldVal - 1);

  $('#datapoints-input').val(newVal);
}

function updateChart() {
  var room = $('#room-name').val();
  var newDatapoints = $('#datapoints-input').val();

  chartTemps(roomValue, newDatapoints);

}
