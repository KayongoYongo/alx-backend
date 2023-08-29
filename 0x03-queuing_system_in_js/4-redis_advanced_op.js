import { createClient, print } from 'redis';

// Create a Redis Client
const client = createClient();

// Listen for the 'connect' event
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Listen for the 'error' event
client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err.message}`);
});

//set hash key-value in HolbertonSchools list
client.hset('HolbertonSchools', 'Portland', '50', print);
client.hset('HolbertonSchools', 'Seattle', '80', print);
client.hset('HolbertonSchools', 'New York', '20', print);
client.hset('HolbertonSchools', 'Bogota', '20', print);
client.hset('HolbertonSchools', 'Cali', '40', print);
client.hset('HolbertonSchools', 'Paris', '2', print);

// Use hgetall to display hash
client.hgetall('HolbertonSchools', (err, result) => {
  if (err) {
    console.error('Error:', err);
  } else {
    console.log('Hash Object:', result);
  }
  
  // Close the Redis connection when done
  client.quit();
});

