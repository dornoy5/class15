from flask import Flask, request, render_template, send_from_directory

app = Flask(__name__)

# Define the folder where uploaded photos will be stored
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def upload():
    uploaded_filename = None

    if request.method == "POST":
        # Check if a file was submitted
        if 'photo' not in request.files:
            return "No file part"

        photo = request.files['photo']

        # Check if the user didn't select a file
        if photo.filename == '':
            return "No selected file"

        # Check if the file has an allowed extension (e.g., .jpg, .png)
        allowed_extensions = {'jpg', 'jpeg', 'png', 'gif'}
        if '.' in photo.filename and photo.filename.rsplit('.', 1)[1].lower() not in allowed_extensions:
            return "Invalid file extension"

        # Save the uploaded photo to the UPLOAD_FOLDER
        photo.save(app.config['UPLOAD_FOLDER'] + '/' + photo.filename)

        uploaded_filename = photo.filename

    return render_template("upload.html", uploaded_filename=uploaded_filename)

# Route to serve uploaded photos
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == "__main__":
    app.run(debug=True)
