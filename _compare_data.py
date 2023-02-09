def check_to_add_student(student_to_check, who_can_help_list):
    for row in who_can_help_list:
         student_number = row[0]
         if student_to_check == student_number:
             return True
    return False

def check_to_remove_student(student_to_check, sis_ell_list):
    for row in sis_ell_list:
        student_number = row[0]
        if student_to_check == student_number:
            return True
    return False

def find_student_to_remove(student_to_check, who_can_help_list):
    for row_index in range(0, len(who_can_help_list)):
        current_student = who_can_help_list[row_index]
        if current_student == student_to_check:
            return row_index
    return False