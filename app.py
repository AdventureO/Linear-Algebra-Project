from flask import Flask, render_template, request, redirect, flash
from TrueDeterminantFinder import Matrix
from input_matrix_validator import checker_matrix_is_square, checker_not_contains_characters, transform_to_list_of_list
import os
#from image_retification import Rectifier

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app.config['UPLOAD_FOLDER'] = os.path.join(BASE_DIR, "static/img")

@app.route('/', methods=["GET", "POST"])
def image_manipulator():
   if request.method == 'POST':
       """
       rectifier = Rectifier()
       rectifier.process(path, coordinates, new_path)
       """
       image_loc = "img/my_file.png"
       image = request.files['image']
       ext = image.filename[image.filename.find('.'):]
       image.save(os.path.join(app.config['UPLOAD_FOLDER'], 'my_file' + ext))
       return render_template('rectification_page.html', image=image_loc)
   return render_template('rectification_page.html')

@app.route('/example')
def example():
    return render_template('example.html')

@app.route('/determinant', methods=["GET", "POST"])
def get_index():
    if request.method == "POST":
        str_matrix = request.form["matrix"]
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
        error_mesage = checker_matrix_is_square(data)
        if error_message:
            return render_template('determinant_page.html', error_message=error_message)
        determin = Matrix(data).det
        return render_template('determinant_page.html', matrix=str_matrix, data =data, determin=determin)
    else:
        return render_template('determinant_page.html')

if __name__ == "__main__":
    app.run(debug=True)