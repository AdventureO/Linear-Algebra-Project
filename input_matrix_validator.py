


def transform_to_list_of_list(str_matrix):
    transformed_list = [[float(i) for i in x.split()] for x in str_matrix.split("\n")]
    return transformed_list

def checker_not_contains_characters(str_matrix):
    new_string = str_matrix
    if ". " in new_string or  ".\r" in new_string or new_string[-1] == ".":
        return "Your matrix can`t contain characters, only digits, try again!"
    new_string = new_string.replace("\n","").replace(" ", "").replace("\r", "").replace(".", "")
    if new_string.isdigit():
        return
    return "Your matrix can`t contain characters, only digits, try again!"

def checker_matrix_is_square(matrix):
    number_of_rows_columns = len(matrix)
    for columns in matrix:  # Verification of square matrix
        if number_of_rows_columns != len(columns):
            return "Can't find determinant, because Your matrix isn't square. Please enter correct square matrix!"