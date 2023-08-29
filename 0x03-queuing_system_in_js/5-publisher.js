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

// Function to publish message after a delay
function publishMessage(message, time) {
  setTimeout(() => {
    console.log('About to send', message);
    client.publish('holberton school channel', message);
  }, time);
}

// Call the publishMessage function with different messages and times
publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
