var path = require("path");
var hello = "Hello from NodeJs Variable"
console.log(`Printing from variable: ${hello}`);

console.log("directory name: " + __dirname);
console.log("directory and file name: " + __filename);

console.log("Using PATH module:");
console.log(`Hello from file ${path.basename(__filename)}`);



//console.log("Hello, world");

console.log(`Process args: ${process.argv}`)
