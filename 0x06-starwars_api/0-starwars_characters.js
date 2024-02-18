#!/usr/bin/node
// script for star wars api

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url,( err, response, body) => {
    if (err) {
        console.log(err);
        return;
    }
    if (response.statusCode != 200) {
        return;
    }
    const FilmData = JSON.parse(body);
    for (let FilmChar of FilmData.characters) {
        request(FilmChar, (err, res, body) => {
            if (err){
                console.log(err);
                return;
            }
            if (res.statusCode != 200) {
                return;
            }
            const names = JSON.parse(body);
            const all = names.name
            console.log(all);   
        })
    }
});
