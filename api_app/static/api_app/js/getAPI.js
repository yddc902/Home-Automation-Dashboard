var refreshInterval = 15; //Refresh data interval

//Retrieve temp data from API
function getTemp(room) {
  $.getJSON('/api/temperatures/' + room, {
    format: "json"
  }).done(function(data){
    console.log(data);
    $.each(data, function(i, item) {
      console.log(item.fields.temperature_f);
      $("#" + room).empty().append(item.fields.temperature_f + '&#8457;');      // .empty() removes old data before appending new data
    })
  })
}

function getDetection() {
  $.getJSON('/api/detection', {
    format: "json"
  }).done(function(data) {
    console.log(data);
    var bwDetected = data[0].fields.water_detected;
    if (bwDetected) {
        $("#basement_water").empty().append("Water detected at: " + data[0].fields.date);
    } else {
      $("#basement_water").empty().append("No water detected")
    }
  })
}

function getMail() {
  $.getJSON('/api/mail', {
    format: "json"
  }).done(function(data){
    console.log(data);
    $.each(data, function(i, item) {
      console.log(item.fields.mail_detected);
      //$("#mail").empty().append('Mail arrived: ' + item.fields.mail_detected);
      //if statement to check for true
      if (item.fields.mail_detected) {
        $("#mail").empty().append("Mail arrived at: " + item.fields.date);
      } else {
        $("#mail").empty().append("Mail has not arrived");
      }
    })
  })
}



//Retrieve data as soon as the page loads
getTemp("kitchen");
getTemp("mancave");
getTemp("livingroom");
getTemp("bedroom");
getDetection();
getMail();

//Refresh data every 15 seconds
setInterval( function() {
  getTemp("kitchen");
  getTemp("mancave");
  getTemp("livingroom");
  getTemp("bedroom");
  getMail();
}, refreshInterval * 1000);
