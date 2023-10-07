# Visual Calculator Based on Python
# Assignment Table
| The Link Your Class |https://bbs.csdn.net/forums/ssynkqtd-04 |
| ----------------- |--------------- |
| The Link of Requirement of This Assignment | https://bbs.csdn.net/topics/617332156 |
| The Aim of This Assignment | Implement the basic functions of a scientific calculator and have a beautiful UI design |
| MU STU ID and FZU STU ID |21125783_832102229 |
# PSP Table
| Personal Software Process Stages   | Estimated Time（minutes） | Actual Time（minutes） |
| :-------------------------------------- | :------------------------ | :--------------------- |
| Planning                                |       20                    |                  30      |
| • Estimate                              |        20                   |  30                      |
| Development                             |   490                        |          725              | 
| • Analysis                              |       120                    |                100        |
| • Design Spec                           |    30                       |                    20    |
| • Design Review                         |      20                     |               20         |
| • Coding Standard                       |    15                       |          20              |
| • Design                                |   30                        |           35             |
| • Coding                                |  180                         |                  260      |
| • Code Review                           |          20                 |               30         |
| • Test                                  |    120                       |       240                 |
| Reporting                               |         190                  |                230        |
| • Test Repor                            |  120                         |       130                 |
| • Size Measurement                      |        10                   |                    10    |
| • Postmortem & Process Improvement Plan |       60                    |             90           |
| Sum                                 |   700                        |                985        |
# Task objectives and realization ideas
## Task objectives
Implement a scientific calculator with basic operations as well as trigonometric and power function operations.
## Realization ideas
### 1 Preliminary ideas
Implementing this calculator requires a visual interface and calculation functions. Python not only has its powerful computing capabilities, but also the Tkinter library can easily create visual interfaces. At the same time, Python is very concise, so I plan to use Python to complete this project.
### 2 Search for information
I use CSDN to search for the information I need
# Design and implementation process
The design of the calculator is divided into several parts：
## Visual Interface
In this section, Tkinter can quickly design the required visual interface and adjust it according to preferences
## Interactive button logic
Design interactive buttons. When a user clicks a button, a function bound to the button is triggered to input the value corresponding to the button onto the screen. When the user presses the equals sign, the function calculates all values.
## Calculation logic
Python has a powerful built-in function: eval(). This function accepts an arithmetic expression in the form of a string and returns the value evaluated by the expression. This function can greatly simplify the calculation process, allowing us to only focus on designing expressions. However, incorrect expressions can lead to system errors. Therefore, we need to design possible user expressions correctly and add try-catch to prevent crashes caused by system errors.
In addition, eval() accepts expressions in Python form, not in human form. For example, except for/instead of ÷, and the sine function being numpy. sin() instead of sin, it is necessary to construct expressions for eval() and expressions presented on the screen separately.
# Code Description

# Specific demonstration
# Summary and possible future improvements
# In the last