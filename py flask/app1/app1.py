from flask import Flask , render_template , request
import os

#interaction
web = Flask(__name__)  #construcitor of the Flask class

#mapping

#@web.route("/")  #decorator to tell the application which URL should trigger the function
@web.route("/home")  #multiple routes for the same function
def homepage():
    pic =  "bg.jpg"  #path to the image
    return render_template("index.html", user_img = pic)  #render the HTML template

@web.route("/confirm", methods=["POST"])  #specifying methods
def submit_form():
    name = request.form.get("fullname")
    email = request.form.get("email")
    phone = request.form.get("phone")
    password = request.form.get("password")

    return render_template(
        "confirm.html",
        name=name,
        email=email,
        phone=phone,
        password=password
    )

#Main function
if __name__ == "__main__":
    web.run(debug=True)  #run the application