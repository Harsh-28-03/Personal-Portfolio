from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/projects")
def projects():
    return render_template("projects.html")


@app.route("/resume")
def resume():
    return render_template("resume.html")


@app.route("/download-resume")
def download_resume():
    return send_from_directory(
        directory="static/files",
        path="Harsh_Shinde_Resume.pdf",
        as_attachment=True
    )


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        return render_template(
            "contact.html",
            success="Thank you! Your message has been received."
        )
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
