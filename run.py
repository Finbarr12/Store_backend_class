from _init_ import app



app.env = "development"

if __name__ == "__main__":
    app.run(debug=True,port=4444)