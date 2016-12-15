from flask import Flask, render_template, request, redirect, flash
from TrueDeterminantFinder import Matrix
from input_matrix_validator import checker_matrix_is_square, checker_not_contains_characters, transform_to_list_of_list
import os
from werkzeug.utils import secure_filename
from flask_wtf.file import FileField
from flask_wtf import FlaskForm
from wtforms import TextField

#from image_retification import Rectifier

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app.config['UPLOAD_FOLDER'] = os.path.join(BASE_DIR, "static/img")

WTF_CSRF_ENABLED = False
WTF_CSRF_SECRET_KEY = 'a random string'


class RectifierForm(FlaskForm):
    photo = FileField("photo")
    right_top = TextField("right_top_corner")
    left_top = TextField("left_top_corner")
    right_bottom = TextField("right_bottom_corner")
    left_bottom = TextField("left_bottom_corner")


@app.route('/', methods=('GET', 'POST'))
def upload():
    form = RectifierForm(csrf_enabled=False)
    if form.validate_on_submit():
        filename = secure_filename(form.photo.data.filename)
        form.photo.data.save('static/img/' + filename)
        left_top = form.left_top.data
        right_top = form.right_top.data
        left_bottom = form.left_bottom.data
        right_bottom = form.right_bottom.data
        print(left_bottom, right_top, left_bottom, left_top, right_bottom)
    else:
        filename = None
    return render_template('rectification_page.html', form=form, filename=filename)


"""
@app.route('/', methods=["GET", "POST"])
def image_manipulator():
   if request.method == 'POST':
       str_coordinates = request.form["coordinates"]
       print(str_coordinates)
       '''
       rectifier = Rectifier()
       rectifier.process(path, coordinates, new_path)
       '''
       image_loc = "img/my_file.png"
       image = request.files['image']
       ext = image.filename[image.filename.find('.'):]
       image.save(os.path.join(app.config['UPLOAD_FOLDER'], 'my_file' + ext))
       return render_template('rectification_page.html', image=image_loc)
   return render_template('rectification_page.html')
"""
@app.route('/about_us', methods=["GET", "POST"])
def about_us():
    return render_template('contact_us.html')

@app.route('/determinant', methods=["GET", "POST"])
def get_index():
    if request.method == "POST":
        str_matrix = request.form["matrix"]
        if (len(str_matrix) == 0):
            return render_template('determinant_page.html', error_message="You didn`t input anything, try again.")
        error_message = checker_not_contains_characters(str_matrix)
        if error_message:
            return render_template('determinant_page.html', error_message=error_message)
        data = transform_to_list_of_list(str_matrix)
        checker = True
        while checker:
            if [] in data:
                data.remove([])
            else:
                checker = False
        error_message = checker_matrix_is_square(data)
        if error_message:
            return render_template('determinant_page.html', error_message=error_message)
        determin = Matrix(data).det
        return render_template('determinant_page.html', matrix=str_matrix, data=data, determin=determin)
    else:
        return render_template('determinant_page.html')

if __name__ == "__main__":
    app.run(debug=True)