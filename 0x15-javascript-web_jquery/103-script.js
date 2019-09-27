$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const code = $('#language_code').val();
    $.getJSON('https://fourtonfish.com/hellosalut/?lang=' + code, function (data) {
      $('DIV#hello').html(data.hello);
    });
  });

  $('INPUT#language_code').on('keypress', function (e) {
    if (e.which === 13) {
      $('INPUT#btn_translate').click();
    }
  });
});

