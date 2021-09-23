document.addEventListener('DOMContentLoaded', function () {
  $('#btn_translate').click(function () {
    const code = $('#language_code').val();
    $.getJSON('https://www.fourtonfish.com/hellosalut/?lang=' + code, function (data) {
      $('#hello').html(data.hello);
    });
  });
