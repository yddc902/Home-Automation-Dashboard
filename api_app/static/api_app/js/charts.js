function chartTemps_all(datapoints) {
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

    new_TempChart(newDateArr, newTempArr, "All Temperatures");
  });
}

function chartTemps(room, datapoints) {
  $.getJSON('/api/temperatures/' + room + '/' + datapoints, {
  }).done(function(data){
    console.log(data);
    console.log(data.reverse());

    var newDateArr = $.map(data, function(e) {
      console.log(e.fields.date);
      return e.fields.date;
    });

    var newTempArr = $.map(data, function(e) {
      console.log(e.fields.temperature_f)
      return e.fields.temperature_f;
    });

    new_TempChart(newDateArr, newTempArr, room);
  });
}

function new_TempChart(labels, data, room) {
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
          display: false
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
  var oldval = +$('#datapoints-input').val();
  console.log(oldval);

  var newval = (oldval + 1);
  console.log(newval);

  $('#datapoints-input').val(newval);
}

function subDatapoint() {
  var oldval = +$('#datapoints-input').val();
  console.log(oldval);

  var newval = (oldval - 1);
  console.log(newval);

  $('#datapoints-input').val(newval);

}
