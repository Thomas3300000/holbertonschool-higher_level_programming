fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => {
    return response.json();
  })
  .then(data => {
    data.results.forEach(movie => {
      const movieElement = document.createElement('li');
      movieElement.textContent = movie.title;
      document.getElementById('list_movies').appendChild(movieElement);
    });
  })
  .catch(error => {
    console.error(error);
  });
