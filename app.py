from flask import Flask, render_template, request
from TrueDeterminantFinder import Matrix


app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def get_index():
    if request.method == "POST":
        str_matrix = request.form["matrix"]
        new_matrix = tranpose(str_matrix)
        data = transform_to_list_of_list(str_matrix)
        determin = Matrix(data).det
        return render_template('index.html', matrix=str_matrix, new_matrix=new_matrix, data =data, determin=determin)
    else:
        return render_template('index.html')


def transform_to_list_of_list(str_matrix):
    transformed_list = [[int(i) for i in x.split()] for x in str_matrix.split("\n")]
    return transformed_list



if __name__ == "__main__":
    app.run(debug=True)