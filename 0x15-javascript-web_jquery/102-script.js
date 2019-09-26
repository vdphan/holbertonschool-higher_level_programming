$( document ).ready(function() {
    $('INPUT#btn_translate').click(function() {
        const code = $('#language_code').val()
        $.getJSON('https://fourtonfish.com/hellosalut/?lang=' + code, function(data){
             $('DIV#hello').text(data.hello);
        });
    });
});