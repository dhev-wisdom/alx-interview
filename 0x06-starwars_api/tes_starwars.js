const axios = require("axios");

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}/`;

axios.get(url)
  .then(response => {
    const filmData = response.data;
    console.log(filmData.title);

    const characterUrls = filmData.characters;

    // Create an array of promises for character requests
    const characterPromises = characterUrls.map(characterUrl => axios.get(characterUrl));

    // Use Promise.all to wait for all character requests to complete
    Promise.all(characterPromises)
      .then(characterResponses => {
        const characters = characterResponses.map(response => response.data.name);
        characters.forEach(character => console.log(character));
      })
      .catch(error => {
        console.error(error);
      });
  })
  .catch(error => {
    console.error(error);
  });
