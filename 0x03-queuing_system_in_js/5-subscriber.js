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

//subscribe to holberton school channel
client.subscribe('holberton school channel');

// On receiving a message
client.on('message', (channel, message) => {
  console.log(`Received message on channel ${channel}: ${message}`);

  // Unsubscribe and quit if the message is "KILL_SERVER"
  if (message === 'KILL_SERVER') {
    client.unsubscribe();
    client.quit();
  }
});
