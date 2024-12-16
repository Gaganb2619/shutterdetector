from flask import Flask, render_template, request, redirect, url_for, make_response
import pdfkit  # For PDF generation

app = Flask(__name__)

# Route for index
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Retrieve form data
        data = {
            "name": request.form["name"],
            "designation": request.form["designation"],
            "about": request.form["about"],
            "phone": request.form["phone"],
            "email": request.form["email"],
            "address": request.form["address"],
            "skills": request.form["skills"],
            "languages": request.form["languages"],
            "education_title": request.form["education_title"],
            "education_institution": request.form["education_institution"],
            "education_year": request.form["education_year"],
            "experience_title": request.form["experience_title"],
            "experience_company": request.form["experience_company"],
            "experience_year": request.form["experience_year"],
            "experience_details": request.form["experience_details"],
            "photo": "/static/default-photo.png"
        }
        return render_template("resume.html", **data)
    return render_template("index.html")

# Route for PDF download
@app.route("/download_pdf", methods=["POST"])
def download_pdf():
    rendered_html = render_template("resume.html", **request.form)
    pdf = pdfkit.from_string(rendered_html, False)
    response = make_response(pdf)
    response.headers["Content-Type"] = "application/pdf"
    response.headers["Content-Disposition"] = "inline; filename=resume.pdf"
    return response

if __name__ == "__main__":
    app.run(debug=True)
