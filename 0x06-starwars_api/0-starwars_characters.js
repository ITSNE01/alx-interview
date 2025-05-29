#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <MOVIE_ID>');
  process.exit(1);
}

const filmUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(filmUrl, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }
  if (res.statusCode !== 200) {
    console.error(`Error: Received status code ${res.statusCode}`);
    return;
  }

  let filmData;
  try {
    filmData = JSON.parse(body);
  } catch (parseErr) {
    console.error('Error parsing response:', parseErr);
    return;
  }

  const characters = filmData.characters || [];

  const fetchCharacter = (index) => {
    if (index >= characters.length) return;
    request(characters[index], (charErr, charRes, charBody) => {
      if (charErr) {
        console.error(charErr);
      } else if (charRes.statusCode !== 200) {
        console.error(`Error fetching character at ${characters[index]}: Status ${charRes.statusCode}`);
      } else {
        try {
          const charData = JSON.parse(charBody);
          console.log(charData.name);
        } catch (e) {
          console.error('Error parsing character JSON:', e);
        }
      }
      fetchCharacter(index + 1);
    });
  };

  fetchCharacter(0);
});
