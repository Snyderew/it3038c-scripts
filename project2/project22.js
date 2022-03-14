var http = require("http");
var fs = require("fs");

http.createServer(function(req, res){
	
	if (req.url === "/log") {
		
		var arr = fs.readFileSync('/var/log/secure').toString().split('\n');


		html=`
		<!DOCTYPE html>
			<html>
			<head>
				<title>Secure Log</title>
			</head>

			<body>
				<h1><center>Secure Log</center></h1>
			</body>
			</html>`
		res.write(html);
		for(let i in arr) {
                	res.write(arr[i]);
		}
		res.end();
	}

	else {
		res.writeHead(404, {"Content-Type": "text/plain"});
		res.end(`404 File Not Found at ${req.url}`);
	}

}).listen(3000);

console.log("Server listening on port 3000");
