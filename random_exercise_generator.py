import random
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s'
    ' - %(message)s')

logging.debug('Start of program' + f'\n')

print('Students should be ordered numerically, starting from an index'
    ' of 0. For example, if you have 17 students, then your first student will'
    ' be labeled with a 0, your second student with a 1, and so on, all the'
    ' way to 16. I recommend using alphabetical order to aid with this'
    ' process. Additionally, exercises should be ordered numerically, starting'
    ' from 0.' + f'\n')

#Input the number of students in your class on this day
students = list(range(int(input('Total number of students in the course.'
    ' Enter your number then press return: '))))
print(f'\n')

#Input the number of exercises 
exercises = list(range(int(input('Number of exercises for today?'
    ' The quantity of the number of exercises, multiplied by 3, must be able to'
    ' divide into the number of students eligible to present. This eligibility'
    ' is contigent on relevant presence/absence status. Enter your'
    ' number then press return: '))))
print(f'\n')

sample_size = exercises[-1] + 1

def randomizer(students, exercises, sample_size):
    """This function is a teaching tool to be used in randomly assigning
students exercises to be worked on the board. For each exercise assigned
by the teacher, three students will be charged with presenting this assignment
in the following manner: The first set of students work the problem on the
board. The second set of students correct any mistakes made by the first
student. The third set of students explain to the class the solution to the
problem worked on the board. Some students may be shy about presenting (being
in the third set). For these students, I stipulate they be in the first set
of students every time. Further, some students may have been absent on days
the topic(s) was (were) discussed. Finally, some students may be absent on
the day presentations are expected. Prompting within this function has been
included to handle these situations."""
    
    #Account for absences either when learning the topic(s) or on presentation
    #day
    absences = []
    flag = True
    while flag:
        student_absence = input('Student number for that student'
            ' who is/was absent. Enter the student number, then press return.'
            ' When you are done entering student numbers'
            ' for this portion of the program, simply press the return key: ')
        if not student_absence:
            flag = False
        else:
            absences.append(int(student_absence))
    print(f'\n')
    
    #First set pulled from the total population, with special exceptions
    
    #Students who wish not to be in group three must be in group one
    num_of_shy = int(input('How many students will be left out of the'
        ' third set? Enter your number following by the return key.'
        ' If there are zero shy students, simply press 0 and return: '))
    print(f'\n')
    
    # We construct the set of shy students
    if num_of_shy != 0:
        shy_students = []
        shys = 0
        while shys < num_of_shy:
            shy_student = int(input('For the next shy student, enter their'
                ' student number and press return: '))
            shy_students.append(shy_student)
            shys += 1
        print(f'\n')
    else:
        shy_students = []
        
    #Student population complement to relevant absences and shyness
    remaining_students = []
    for those in students:
        if those not in absences and those not in shy_students:
            remaining_students.append(those)
            
    # We now begin to randomly distribute exercises to today's students
    
    # We have our eligible students wrapped in variable 'todays_population'
    todays_population = shy_students + remaining_students
    
    # A randomly generated list of the students from todays_population, using
    # 100% of the shy students, and filling in the remaining presentations with
    # students from the remaining_students variable, which contains none of
    # the shy students. This will be a list of numbers that you use to
    # identify a student.
    student_sample = shy_students + random.sample(remaining_students,
        sample_size-num_of_shy)
            
    # A randomly generated list of the exercise numbers. This will be a list
    # of number that you use to identify an exercise.
    exercise_sample = random.sample(exercises, sample_size)
    
    # The following statements will take the randomly generated list of student
    # numbers and the randomly generated list of exercise numbers and create a
    # mapping. This will generate the first set of student presenters and the
    # exercises they are to present.
    mapping = {}
    for i in range(len(student_sample)):
        mapping[sorted(student_sample)[i]] = sorted(exercise_sample)[i]
    
    # Removing those students pulled from todays_population to create the
    # remaining population
    for j in student_sample:
        todays_population.remove(j)
    
    # The following statements will randomly generate a second list of student
    # numbers, pulled from the remaining population after the first round of
    # removals above. We first redefine todays_population as the first
    # relevant subset of students: students_subset_1.
    students_subset_1 = todays_population
    student_sample_subset_1 = random.sample(students_subset_1, sample_size)
    
    # The following statements will take the randomly generated list of student
    # numbers from the student_sample_subset_1 list and the randomly generated
    # list of exercise numbers and create a second mapping. This will generate
    # the second set of student presenters and the exercises they are to
    # present.
    mapping_subset_1 = {}
    for k in range(len(student_sample_subset_1)):
        mapping_subset_1[sorted(student_sample_subset_1)[k]] = \
            sorted(exercise_sample)[k]

    # Removing those students pulled from students_subset_1 to create the
    # remaining population
    for l in student_sample_subset_1:
        students_subset_1.remove(l)
    
    # The following statements will randomly generate a third list of student
    # numbers, pulled from the remaining population after the second round of
    # removals above. We first redefine students_subset_1 as the second
    # relevant subset of students: students_subset_2.
    students_subset_2 = students_subset_1
    student_sample_subset_2 = random.sample(students_subset_2, sample_size)

    # The following statements will take the randomly generated list of student
    # numbers from the student_sample_subset_2 list and the randomly generated
    # list of exercise numbers and create a third mapping. This will generate
    # the third set of student presenters and the exercises they are to
    # present.
    mapping_subset_2 = {}
    for m in range(len(student_sample_subset_2)):
        mapping_subset_2[sorted(student_sample_subset_2)[m]] = sorted(exercise_sample)[m]

    # The following statements will remove those students sampled and assigned
    # to present from the students_subset_2 list to create a list
    # of those students who will not have to present today
    for n in student_sample_subset_2:
        students_subset_2.remove(n)
        
    return mapping, mapping_subset_1, mapping_subset_2, students_subset_2

set_1, set_2, set_3, remaining = randomizer(students, exercises, sample_size)
print(f'\n')
print('Here is the first set of students: ')
print(set_1)
print(f'\n')
print('Here is the second set of students: ')
print(set_2)
print(f'\n')
print('Here is the third set of students: ')
print(set_3)
print(f'\n')
print('These students are safe: ')
print(remaining)