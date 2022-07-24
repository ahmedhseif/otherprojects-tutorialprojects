from flask import Flask, render_template, request
import requests
import smtplib


MY_EMAIL = "EMAIL"
MY_PASS = "PASS"
API_ENDPOINT = "https://api.npoint.io/c790b4d5cab58020d391"

posts = requests.get(API_ENDPOINT).json()

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html", all_posts=posts)

@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.route('/about')
def show_about():
    return render_template("about.html")

@app.route('/contact', methods=["GET", "POST"])
def show_contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}".encode("utf-8")
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASS)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="ahmedseifpython@outlook.com",
                            msg=email_message)

if __name__ == "__main__":
    app.run(debug=True)
