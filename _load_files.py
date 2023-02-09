import openpyxl as openpyxl
import warnings as warnings

def column_letters():
    # use chr() + ord()
    char_prefixes = ["", "A", "B", "C", "D"]
    col_letters = []

    for p in range(0, len(char_prefixes)):
        ch = "A"
        col_letters.append(char_prefixes[p] + "A")
        for i in range(25):
            new_ch = chr(ord(ch) + 1)
            characters = char_prefixes[p] + new_ch
            col_letters.append(characters)
            ch = new_ch
    return col_letters


def find_col_array_index(column_letter):
    col_letters = column_letters()
    index = col_letters.index(column_letter)
    return index


def load_file(file_name):
    """ Load data from an Excel file. NOTE: the load typically throws this error "UserWarning: Data Validation
    extension is not supported and will be removed warn(msg)", as openpyxl does not support data validation
    (see dropdown OLG and SC columns on 'Tracking Sheet') but should NOT affect overall functioning of this program.
    The 'warnings' module removes the warning from printing in the turn terminal to minimize confusion.
    """
    warnings.simplefilter(action='ignore', category=UserWarning)
    print("File <" + str(file_name) + "> has loaded successfully.")
    return openpyxl.load_workbook(file_name, data_only=True)


def who_can_help_array(workbook):
    sheet_name = "Clean List"
    data_sheet = workbook[sheet_name]
    ell_list = []
    for row in data_sheet.values:
        if row[0] is not None and row[0] != "Student #":
            ell_list.append(row)

    print(f"Current number of ESL/ELL Students: {len(ell_list)}")
    return ell_list


def sis_esl_list_array(workbook):
    student_number_column = find_col_array_index(column_letter="O")
    student_last_name_column = find_col_array_index(column_letter="A")
    student_first_name_column = find_col_array_index(column_letter="B")
    student_sex_column = find_col_array_index(column_letter="AD")
    student_grade_column = find_col_array_index(column_letter="AE")
    student_home_L1_column = find_col_array_index(column_letter="E")
    student_home_L2_column = find_col_array_index(column_letter="F")

    sheet_name = "Sheet1"
    data_sheet = workbook[sheet_name]

    esl_list = []
    previous_student_number = 0
    for row in data_sheet.values:
        current_student_number = row[student_number_column]
        student_data = []
        if current_student_number != previous_student_number:
            student_data.append(row[student_number_column])
            student_data.append(row[student_last_name_column])
            student_data.append(row[student_first_name_column])
            student_data.append(row[student_sex_column])
            student_data.append(row[student_grade_column])
            student_data.append(row[student_home_L1_column])
            student_data.append(row[student_home_L2_column])
            esl_list.append(student_data)
        else:
            pass
        previous_student_number = current_student_number

    # remove header row
    if len(esl_list) > 0:
        esl_list.pop(0)

    return esl_list
