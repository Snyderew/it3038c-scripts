from routes import app

if __name__ == "__main__":
    #deploys flask web server locally on port 5000
    app.run(debug=True, port=5000, host='0.0.0.0')
