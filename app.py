from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# Create a route for the homepage
@app.route("/")
def home():
    # This will load your index.html file from the "templates" folder
    return render_template("index.html")

# Run the app locally!
if __name__ == "__main__":
    app.run(debug=True)
