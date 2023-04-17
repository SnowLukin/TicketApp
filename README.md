# Exam tickets generator

## Introduction

The Exam Ticket Generator is an application designed to create 
balanced exam tickets, comprised of both theoretical and practical
tasks, for exams or tests. The app utilizes the Simulated Annealing
algorithm to ensure the generated tickets are randomized, unbiased, 
and efficient.


## Key Features
- Generates balanced tickets, including both theoretical and practical tasks
- Offers customizable settings for adjusting the difficulty level and the proportion of theoretical vs. practical tasks
- Features an easy-to-use interface for quick and efficient ticket generation
- Utilizes an efficient algorithm to ensure randomized and unbiased ticket creation
- Streamlines the ticket generation process, saving time and effort for educators and examiners
- Facilitates a fair and comprehensive evaluation of students' knowledge and skills

##  Approach

This app employs the  [Simulated Annealing algorithm](https://en.wikipedia.org/wiki/Simulated_annealing) 
to generate balanced exam tickets from given theoretical and practical tasks. 
The algorithm efficiently addresses the challenges of large search 
spaces and combinatorial optimization while maintaining a balance 
between exploration and exploitation. This flexibility allows the app 
to generate non-overlapping tickets with balanced complexity for 
both theoretical and practical tasks, ensuring fairness in exam 
ticket distribution.

See implementation in [ticket_generator.py](https://github.com/SnowLukin/TicketApp/blob/main/app/models/ticket_generator.py)

## Instructions

### Document requirements
Ensure that tasks are formatted correctly in a Microsoft Word document 
with the .docx extension. Adhere to the following styles and 
formatting guidelines for each task type:

- **Theory tasks file:** Apply the List Number or List Paragraph style to each task.
- **Practice tasks file:** Mark each task using the pattern Задание №# or Task №#, where # represents the task number and № is optional.
- **Task complexity:** To indicate the complexity of a task, include {#} in the same paragraph as the task, with # representing the complexity value (e.g., {3}).

**Note**: the complexity for tasks are optional

### How to use
1. Launch the app and select the files containing the theoretical and practical tasks. After loading the files, the app will display the total number of tasks recognized.
2. Specify the desired number of exam tickets, as well as the number of theoretical and practical tasks to be included in each ticket.
3. If some tasks do not have specified complexity values and you want to include them in the generated tickets, enable the **_include tasks with no complexity_** option. This will assign a default complexity value of 0 to these tasks.
4. Click the generate button and choose the folder where you want the output to be saved.


### Output
The app will generate a .docx document containing balanced tickets. Theoretical tasks will be presented with their respective descriptions, while practical tasks will be listed as "Task" followed by the task number (e.g., Task 3).

## Preview

<img width="400" alt="app_img_2" src="images/app_img_2.png?raw=true">