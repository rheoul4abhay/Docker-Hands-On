const express = require('express');
const mongoose = require('mongoose');
const app = express();

mongoose.connect('mongodb://mongo:27017/mydb')
  .then(() => console.log('Connected to MongoDB!'))
  .catch(err => console.error(err));

app.get('/', (req, res) => res.send('Hello from Node + Mongo!'));

app.listen(3000, () => console.log('Listening on port 3000'));
