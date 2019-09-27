$.get('https://swapi.co/api/films/?format=json', function (data) {
  for (const movie of data.results) {
    $('UL#list_movies').append(`<li>${movie.title}</li>`);
  }
});
