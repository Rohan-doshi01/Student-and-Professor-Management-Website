
# STUDENT & PROFESSOR MANAGEMENT WEBSITE


## How to run:
Open terminal by
```bash
  " ctrl + ` "
 ```
  Create a Virtual Environment by
 ```bash
 "python -m venv venv"
 ```
  Activate Virtual Environment 
 ```bash
"venv\Scripts\activate"
 ```
 Install Requirements Package 
 ```bash
 "pip install -r requirements.txt"
 ```
 Install addons by
 ```bash
  "pip install pillow"
 ```
 Create database by
 ```bash
  "python manage.py makemigrations"
 ```
  Migrate Database
 ```bash
 "python manage.py migrate"
 ```
  Create Super User
 ```bash
 "python manage.py createsuperuser"
 ```
 Finally Run The Project by typing 
 ```bash
 "python manage.py runserver"
 ```

 



## Objectives :

1. Ability to create courses
2. Certification tracking
3. Cross platform availability
4. Performance based tasks for skill analysis
5. Easily accessible to navigate user interface
6. Maintain all the database of teachers , students and employees
7. Maintain the accuracy , integrity and consistency of the data

## Proposed System :

1. A Course Management System is a set of software tools designed to manage user learning interventions including online, virtual classroom, and instructor-led courses.
2. Web-based and facilitate "anytime, any place, any pace" access to learning content and administration.
3. Students can register to the system. After registration a student can log in to the system using email and password. Instructors and Admin can also login to the system using the same login by inputting the email and password provided by the main admin.
4. Once main admin creates Instructors and Admin , they will receive a confirmation email and for students also once they are registered, they will receive a verification email to activate their account.
5. Instructors can add course and create assignment materials to the system and then student can view the courses and upload files to the created assignments.
6. All the Admin/Instructors/Students cans search courses by providing course name or course id.
7. Students can enroll in a course and later also withdraw from the course.Ability to modify any detail of the course.
8. This proposed system has several advantages 
 - User friendly interface 
 - Fast access to database 
 - Less error 
 - More Storage Capacity 
 - Search facility 
 - Look and Feel Environment 

9. All the manual difficulties in managing the student details in a school or college have been rectified by implementing computerization. 


# System Architecture/ Framework :

## INPUT DESIGN
 
Input design is the process of converting user-oriented input to a computer based format. Input design is a part of overall system design, which requires very careful attention. Often the collection of input 
data is the most expensive part of the system. The main objectives of the input design are …
1. Produce cost effective method of input 
2. Achieve highest possible level of accuracy 
3. Ensure that the input is acceptable to and understood by the staff. 

## INPUT DATA 

The goal of designing input data is to make entry easy, logical and free from errors as possible. The entering data entry operators need to know the allocated space for each field; field sequence and which must match with that in the source document. The format in which the data fields are entered should be given in the input form. Here data entry is online; it makes use of processor that accepts commands and data from the operator through a keyboard. The input required is analyzed by the processor. It is then accepted or rejected.

### Input stages include the following processes :
 
- Data Recording 
- Data Transcription 
- Data Conversion 
- Data Control 
- Data Transmission 
- Data Correction One of the aims of the system analyst must be to select data capture method and devices, which reduce the number of stages so as to reduce both the changes of errors and the cost.  Input types, can be characterized as:
- External 
- Internal 
- Operational 
- Computerized 
- Interactive Input files can exist in document form before being input to the computer. Input design is rather complex since it involves procedures for capturing data as well as inputting it to the computer. 

## OUTPUT DESIGN 

Outputs from computer systems are required primarily to communicate the results of processing to users. They are also used to provide a permanent copy of these result for latter consultation. Computer output is the most important and direct source of information to the users. Designing computer output should proceed in an organized well through out the manner. The right output must be available for the people who find the system easy o use. The outputs have been defined during the logical design stage. If not, they should have defined at the beginning of the output designing terms of types of output connect, format, response etc. 

Various types of outputs are 

- External outputs 
- Internal outputs 
- Interactive outputs 


## DATABASE DESIGN 

The general theme behind a database is to handle information as an integrated whole. A database is a collection of interrelated data stored with minimum redundancy to serve many users quickly and effectively. After designing input and output, the analyst must concentrate on database design or how data should be organized around user requirements. The general objective is to make information access, easy quick, inexpensive and flexible for other users. During database design the following objectives are concerned:- 

- Data independence 
- Accurate and integrating 
- More information
- Recovery from failure 
- Privacy and security 
- Performance 
- Ease of learning and use 

## Flowchart of the system : 

![Flowchart](https://github.com/Rohan-doshi01/Student-and-Professor-Management-Website/blob/main/Screenshot%202023-04-05%20201338.png)

### Modules : 
 
There are 10 different modules in the project controlling the different aspects of the program.
 
They are :-
- Academic – To track the content of the courses(subjects)
- Account – To create / manage the account of registered  individuals.
- Address – To manage the details of registered individuals.
- Administration – To manage the administration account.
- Attendance – To take the attendance of students.
- Course management – To  manage the courses.
- Employee – To manage the account of the employees.
- Result – To show the results of the courses.
- Student – To create / manage the account of Students.
- Teacher - To create / manage the account of Teachers.

## Screenshots of the program :

![Screenshots](https://github.com/Rohan-doshi01/Student-and-Professor-Management-Website/blob/main/Screenshot%202023-04-06%20133157.png)

![Screenshots](https://github.com/Rohan-doshi01/Student-and-Professor-Management-Website/blob/main/Screenshot%202023-04-06%20133232.png)

![Screenshots](https://github.com/Rohan-doshi01/Student-and-Professor-Management-Website/blob/main/Screenshot%202023-04-06%20133258.png)

![Screenshots](https://github.com/Rohan-doshi01/Student-and-Professor-Management-Website/blob/main/Screenshot%202023-04-06%20133615.png)

![Screenshots](https://github.com/Rohan-doshi01/Student-and-Professor-Management-Website/blob/main/Screenshot%202023-04-06%20133634.png)

## Refrences :-
https://blog.mettl.com/your-ultimate-guide-to-creating-a-scalable-online-certification-program/

CSS:
[Tutorialspoint](https://www.tutorialspoint.com/css/index.htm)
 
Django:
[MDN](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django)
 
[Github](https://cft.vanderbilt.edu/guides-sub-pages/course-management-systems/)

[Youtube](https://www.youtube.com/watch?v=JIFqqdRxmVo)










