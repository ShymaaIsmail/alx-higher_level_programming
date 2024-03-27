#!/usr/bin/node
const http = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

http.get(url, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  const result = JSON.parse(body);
  const characters = result.characters;
  const fetchCharacter = (url) => {
    return new Promise((resolve, reject) => {
      http.get(url, function (error, response, body) {
        if (error) {
          reject(error);
        } else {
          const character = JSON.parse(body).name;
          resolve(character);
        }
      });
    });
  };

  const printCharacters = async () => {
    for (const characterUrl of characters) {
      try {
        const characterName = await fetchCharacter(characterUrl);
        console.log(characterName);
      } catch (error) {
        console.error(error);
      }
    }
  };

  printCharacters();
});
