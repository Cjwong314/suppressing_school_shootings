const http = require('http');

const server = http.createServer();

server.on('connecton',(socket) => 
{
    console.log('new conection...');

});

server.listen(3000);

console.log('listening on port 3000...')