/**
 * Must run 'npm install express' before running the server
 */

const express = require('express');
const app = express();
app.use(express.static(__dirname));
app.listen(3000)
