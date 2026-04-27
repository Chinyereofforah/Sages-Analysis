# Building a FastAPI application with Python

from fastapi import FastAPI

# Creat an instance of the FastAPI application
app = FastAPI()

# Study different API methods
@app.get("/") # means defining the root for the API (URL)
def home():
    return {"message": "Welcome to the FastAPI application!",
            "swagger ui": "/docs",
            "endpoints": ["/about", "/csv"]}

@app.get("/about")
def about():
    return {
        "course": "Python Full Stack developer",
        "instructor": "Sage",
        "description": "This course covers Python programming, web development, and more."
    }
@app.get("/csv")
def csv():
    csv_content = "Name,Age,City\nAlice,30,New York\nBob,25,Los Angeles\nCharlie,35,Chicago"
    return {"csv_data": csv_content}