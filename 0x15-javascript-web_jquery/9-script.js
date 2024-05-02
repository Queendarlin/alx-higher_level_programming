// To fetch the translation of "hello" in French from the provided URL https://hellosalut.stefanbohacek.dev/?lang=fr and display it in the HTML tag DIV#hello
$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
  $('DIV#hello').text(data.hello);
});
