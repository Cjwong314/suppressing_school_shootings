const http = require('http');

const hostname = '127.0.0.1';
const port = 3000;

const server = http.createServer((req, res) => {
;
  if (req.url === '/') {
    res.write('Hello World');
    res.end();
  }

  if (req.url === '/sound') {
    res.write('nice');
    res.end();
    
  }
   
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});





