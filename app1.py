from flask import Flask, render_template, request, redirect, flash
from TrueDeterminantFinder import Matrix


app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def image_manipulator():
   if request.method == 'POST':
       # check if the post request has the file part
       image = request.files['image']
       image.save(image.filename)
   return render_template('image-manipulator.html')


if __name__ == "__main__":
    app.run(debug=True)