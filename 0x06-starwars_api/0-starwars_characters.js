#!/usr/bin/node

const request = require('request');

const id = process.argv[2]
const url = `https://swapi-api.alx-tools.com/api/films/${id}/`;

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const film = JSON.parse(body);
  console.log(film.title);
  const characterUrls = film.characters;

  function fetchCharacter(char_url) {
    return new Promise((resolve, reject) => {
      request(char_url, (err, response, body) => {
        if (err) {
          reject(err);
        } else if (response.statusCode == 200) {
          const character = JSON.parse(body);
          resolve(character.name);
        } else {
          reject(err);
        }
      });
    });
  }

  const characterPromises = characterUrls.map(fetchCharacter);

  Promise.all(characterPromises)
    .then((characters) => {
      for (const character of characters) {
        console.log(character);
      }
    })
    .catch(err => {
      console.error(err);
    });
});
