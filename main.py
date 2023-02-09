from _load_files import load_file, who_can_help_array, sis_esl_list_array
from _compare_data import check_to_add_student, check_to_remove_student

# list the paths for the respective documents to work with
who_can_help_doc = "/Users/work/OneDrive - Peel District School Board/OneDrive Desktop/ESL ELL School Data/2022-10-31 ELL List.xlsx"
sis_ell_list = "/Users/work/OneDrive - Peel District School Board/OneDrive Desktop/ESL ELL School Data/2023-02-07 ESL_ELL LIST.xlsx"
sis_master_time_table = "/Users/work/OneDrive - Peel District School Board/OneDrive Desktop/ESL ELL School Data/2022-02-07 Master Time Table.xlsx"


# ----- open files -----
WB_who_can_help = load_file(file_name=who_can_help_doc)
WB_sis_ell_list = load_file(file_name=sis_ell_list)
# WB_sis_master_time_table = load_file(file_name=sis_master_time_table)

# ----- bring data into arrays -----
who_can_help_data = who_can_help_array(workbook=WB_who_can_help)
sis_ell_list_data = sis_esl_list_array(workbook=WB_sis_ell_list)

# ----- determine which students to ADD from ESL/ELL tracking list -----
students_to_add_to_list = []
print(f"\nStudents to ADD to our in school tracking document:")
for row in sis_ell_list_data:
    student = row[0]
    status = check_to_add_student(student_to_check=student,
                                  who_can_help_list=who_can_help_data)
    if status == False:
        # this means that the student on the most recent SIS ESL/ELL report is currently not listed in our
        # in school tracking document
        students_to_add_to_list.append(row)
        print(f"\t {row}")
print(f"Number of students to ADD: {len(students_to_add_to_list)}")

# ----- determine which students to REMOVE from ESL/ELL tracking list -----
students_to_remove_from_list = []
print(f"\nStudents to REMOVE to our in school tracking document:")
for row in who_can_help_data:
    student = row[0]
    status = check_to_remove_student(student_to_check=student,
                                     sis_ell_list=sis_ell_list_data)
    if status == False:
        # this means that the student that is currently on our in school tracking document is no longer registered
        # at the school, meaning that they need to be removed from our list
        students_to_remove_from_list.append(row)
        print(f"\t {row}")
print(f"Number of students to REMOVE: {len(students_to_remove_from_list)}")

# ----- clean our tracking document -----
# add students to the list
for row in students_to_add_to_list:
    who_can_help_data.append(row)

# remove students from the list
for row in students_to_remove_from_list:
    student_number = row[0]
    index = who_can_help_data[0].index(student_number) # 0 = array index for student number
    who_can_help_data.pop(index)
    print(row)



print(f"\nRevised number of ESL/ELL Students: {len(who_can_help_data)}")

