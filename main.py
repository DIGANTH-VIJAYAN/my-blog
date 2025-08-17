import os
from flask import Flask, render_template, request
import requests
import smtplib
from datetime import datetime

MY_GMAIL = os.getenv("MY_GMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")
TO_GMAIL = os.getenv("TO_GMAIL")

def fetch_and_process_posts():
    url = "https://api.npoint.io/8a7c4d9c892ec1ccd1bb"
    all_posts = requests.get(url=url).json()

    for post in all_posts:
        post["parsed_date"] = datetime.strptime(post["Date"], "%dth %b, %Y")

    sorted_posts = sorted(all_posts, key = lambda x: x["parsed_date"], reverse=True)

    return sorted_posts

sorted_all_posts = fetch_and_process_posts()

app = Flask(__name__)

@app.route("/")
@app.route("/index.html")
def home_page():
    latest_posts = sorted_all_posts[:3]
    return render_template("index.html", posts=latest_posts)

@app.route("/about.html")
def display_about():
    return render_template("about.html")

@app.route("/contact.html")
def display_contact():
    return render_template("contact.html")

@app.route("/post/<index>")
def get_post(index):
    return render_template("post.html", post=sorted_all_posts[int(index) - 1])

@app.route("/form-entry", methods=['GET', 'POST'])
def receive_data():
    if request.method == "POST":
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            name = request.form["name"]
            email = request.form["email"]
            phone = request.form["phone"]
            message = request.form["message"]
            connection.starttls()
            connection.login(user=MY_GMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_GMAIL,
                to_addrs=TO_GMAIL,
                msg=f"Subject: A New Connection Request\n\nName: {name} \nEmail: {email} \nPhone: {phone} \nMessage: {message}"
            )
            return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)



if __name__ == "__main__":
    app.run()


