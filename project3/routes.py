from flask import Flask, render_template, request
import platform
import shutil
import os

app = Flask(__name__)
app.config.from_object(__name__)

#homepage that can be accessed by navigating to 'http://localhost:5000/' or 'http://localhost:5000/home'
#contains hyperlinks to navigate to other three webpages
@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")

#webpage that displays system information using os and platform modules
@app.route('/sysinfo')
def sysinfo():

    user = os.getlogin()
    computername = platform.node()
    OSname = platform.system()
    release = platform.release()
    version = platform.version()
    processor = platform.processor()

    return render_template("sysinfo.html", value=user, value1=computername, value2=OSname, value3=release, value4=version, value5=processor)

#webpage that displays total, used, and available disk space in gigabytes using shutil module
@app.route('/storage')
def storage():

    GB = 1000000000
    #displays total disk space in bytes
    tbyte = shutil.disk_usage('/').total
    #converts total disk space from bytes to gigabytes
    totalgb = (float(tbyte)/GB)
    #rounds decimal value to hundredths 
    totalspace = round(totalgb, 2)
    #repeats disk space calculation, conversion, and rounding for used disk space
    ubyte = shutil.disk_usage('/').used
    usedgb = (float(ubyte)/GB)
    usedspace = round(usedgb, 2)
    #repeats disk space calculation, conversion, and rounding for free disk space
    abyte = shutil.disk_usage('/').free
    availablegb = (float(abyte)/GB)
    availablespace = round(availablegb, 2)

    return render_template("storage.html", value1=totalspace, value2=usedspace, value3=availablespace)

@app.route('/uptime')
def uptime():
    #displays system uptime in week, day, hour, minute format

    uptime = os.popen('uptime -p').read()

    return render_template("uptime.html", value=uptime)

