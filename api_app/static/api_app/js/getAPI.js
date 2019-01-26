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

//Retrieve data as soon as the page loads
getTemp("kitchen");
getTemp("mancave");
getTemp("livingroom");
getTemp("bedroom");

//Refresh data every 15 seconds
setInterval( function() {
  getTemp("kitchen");
  getTemp("mancave");
  getTemp("livingroom");
  getTemp("bedroom");
}, refreshInterval * 1000);
