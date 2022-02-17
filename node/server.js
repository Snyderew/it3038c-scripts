var http = require("http");
var fs = require("fs");
var os = require("os");
var ip = require('ip');

http.createServer(function(req, res){
	
	if (req.url === "/") {
		fs.readFile("./public/index.html", "UTF-8", function(err, body){
		res.writeHead(200, {"Content-Type": "text/html"});
		res.end(body);
	});
	}

	else if(req.url.match('/sysinfo')) {
		myHostName=os.hostname();
		uptime = os.uptime();
		ut_day = Math.floor(uptime / 86400);
		uptime -= ut_day * 86400;
		ut_hour = Math.floor(uptime / 3600) %24;
		uptime -= ut_hour * 3600;
		ut_min = Math.floor(uptime / 60) %60;
		uptime -= ut_min * 60;
		ut_sec = uptime %60;
		totalmem = Math.round(os.totalmem()/(1024*1024));
		freemem = Math.round(os.freemem()/(1024*1024));
		html=`
		<!DOCTYPE html>
		<html>
		<head>
			<title>Node JS Reponse</title>
		</head>
		<body>
			<p>Hostname: ${myHostName}</p>
			<p>IP: ${ip.address()}</p>
			<p>Server Uptime: Days: ${ut_day}, Hours: ${ut_hour}, Minutes: ${ut_min}, Seconds:${ut_sec}</p>
			<p>Total Memory: ${totalmem} MB </p>
			<p>Free Memory: ${freemem} MB </p>
			<p>Number of CPUs: ${os.cpus().length} </p>
		</body>
		</html>`
		res.writeHead(200, {"Content-Type": "text/html"});
		res.end(html);

	}
	else {
		res.writeHead(404, {"Content-Type": "text/plain"});
		res.end(`404 File Not Found at ${req.url}`);
	}

}).listen(3000);

console.log("Server listening on port 3000");


