<h2> Project 3 </h2>
<p>
  For Project 3, I created a Flask web application that has 4 webpages: Homepage, System Information, Storage Space, and System Uptime. The homepage welcomes the user and contains links for the other three pages. The System Information page displays information for the system that the app is hosted on. This information includes currently logged in user, computer name, OS, OS release, OS version, and processor. The Storage Space page displays total, used, and available disk space for the local system in gigabytes. Finally, the System Uptime page displays uptime for the local host machine in week, day, hour, minute format. 
  </p>
<h2> Requirements </h2>

Python Version used: Python 3.6.8 <br>
Modules: flask, os, platform, shutil <br>
Install Flask: pip install flask <br>
Note: os, platform, shutil are included in Python Standard Library <br>

<h2> Instructions </h2>
1. Create Flask venv
<br>
  Windows: <br>
  py -3 -m venv venv <br>
  venv\Scripts\activate.ps1 <br>
<br>  
  Linux: <br>
  python3 -m venv venv <br>
  . venv/bin/activate <br>
2. Run project3.py to deploy web server locally on port 5000 <br>
3. Navigate to http://localhost:5000/ to go to the homepage <br>
   http://localhost:5000/home also takes you to the homepage <br>
4. View the webpages in your browser
  <br>
Note: The functions used in my code should be compatible with Windows, but have only been tested in Linux.
