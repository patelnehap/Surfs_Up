# 1. Import Flask
from flask import Flask

# 2. Create an app
app = Flask(__name__)


# 3. Define index route
@app.route("/")
def index():
    return "Hello, world!"

# 4. Define the about route
@app.route("/about")
def about():
    name = "Taara"
    location = "New Jersey"
    return f"My name is {name}, and I live in {location}."

# 5. Define the contact route
@app.route("/contact")
def contact():
    email = "taara@gmail.com"

    return f"Please email your concerns to {email}."


# 6. Define main behavior
if __name__ == "__main__":
    app.run(debug=True)
