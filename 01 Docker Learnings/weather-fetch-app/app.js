const express = require('express');
const axios = require('axios');
require('dotenv').config();

const app = express();
const PORT = 5000;

app.get('/weather/:city', async (req, res) => {
	  const city = req.params.city;
	  const apiKey = process.env.OPENWEATHER_KEY;

	  try {
		      const response = await axios.get(
			            `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`
			          );
		      res.json(response.data);
		    } catch (error) {
			        res.status(500).json({ error: 'Error fetching weather data' });
			      }
});

app.listen(PORT, () => {
	  console.log(`Server running on port ${PORT}`);
});

