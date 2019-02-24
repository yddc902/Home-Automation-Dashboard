

$(document).ready(function() {
  var chartValues = chartTemps_all();
  var cvDate = chartValues[0];
  var cvTemp = chartValues[1];
  var cvDataPoints = chartValues[2];
});

function new_TempChart(data) {
  //Create the chart
  console.log(data);

  var ctx = document.getElementById("kitchen-temp").getContext('2d');
  var tempChart = new Chart(ctx, {
    type: 'scatter',
    data: data,
  })
}

function chartTemps_all() {
  //Init empty arrays for date and temp
  var dateArr = [];
  var tempArr = [];
  var dataPoints = [];

  //Get API data
  $.getJSON('/api/TempModel/?format=json', {
    format: "json"
  }).done(function(data){
    //console.log(data);

    //Loop through data and get date and temp points
    $.each(data, function(i, item) {
      //console.log(item);
      //console.log(item.date);
      //console.log(item.temperature_f);

      //dateArr.push(item.date);
      var num = i + 1
      dateArr.push(num.toString());
      tempArr.push(item.temperature_f);
      //console.log(dateArr)
      //console.log(tempArr)

      dataPoints.push({x: item.date, y: item.temperature_f});

    })

    setTimeout(new_TempChart(dataPoints), 5000);
  })

  return [
    dateArr,
    tempArr,
    dataPoints
  ];
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
