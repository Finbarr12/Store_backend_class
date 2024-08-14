from app import app



app.env = "development"

if __name__ == "__main__":
    app.run(debug=True,port=4444)