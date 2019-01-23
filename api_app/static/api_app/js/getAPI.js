/*$(function getTemp() {
  $.ajax({
    type: 'GET',
    url: '/api/room1',
    //url: {% url 'last_temp' %}
    //url: '/api/TempModel/?format=json',
    dataType: 'json',
    success:function(data){
      console.log(data);
      $("#room1").append(data)
    }
  })
})*/

setTimeout(function() {
  $(function getTemp() {
    $.getJSON('/api/temperatures/kitchen', {
      format: "json"
    }).done(function(data){
      console.log(data);
      $.each(data, function(i, item) {
        console.log(item.fields.temperature_f);
        $("#kitchen").append(item.fields.temperature_f + '&#8457;');
      })
    })
    .error(function() {
      $("#kitchen").append("Err");
    })
  })

  $(function getTemp() {
    $.getJSON('/api/temperatures/livingroom', {
      format: "json"
    }).done(function(data){
      console.log(data);
      $.each(data, function(i, item) {
        console.log(item.fields.temperature_f);
        $("#livingroom").append(item.fields.temperature_f + '&#8457;');
      })
    })
  })

  $(function getTemp() {
    $.getJSON('/api/temperatures/mancave', {
      format: "json"
    }).done(function(data){
      console.log(data);
      $.each(data, function(i, item) {
        console.log(item.fields.temperature_f);
        $("#mancave").append(item.fields.temperature_f + '&#8457;');
      })
    })
  })

  $(function getTemp() {
    $.getJSON('/api/temperatures/bedroom', {
      format: "json"
    }).done(function(data){
      console.log(data);
      $.each(data, function(i, item) {
        console.log(item.fields.temperature_f);
        $("#mancave").append(item.fields.temperature_f + '&#8457;');
      })
    })
  })
}, 0);
