#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

request.get(apiUrl, function (error, response, body) {
  if (error) {
    console.error('Error fetching data:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Failed to fetch data. Status code:', response.statusCode);
    return;
  }

  try {
    const todos = JSON.parse(body);
    const completedTasksByUser = {};

    // Filter completed tasks and count them by user ID
    todos.forEach(todo => {
      if (todo.completed) {
        if (completedTasksByUser[todo.userId]) {
          completedTasksByUser[todo.userId]++;
        } else {
          completedTasksByUser[todo.userId] = 1;
        }
      }
    });

    // Print users with completed tasks and the number of tasks completed
    console.log(completedTasksByUser);
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError);
  }
});
