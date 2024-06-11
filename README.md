# 📚 Engineering Assignments & Github Learning
Welcome to the Engineering Assignments Repository!
Follow the instructions below to learn how to clone the repository, make changes, commit, push, create pull requests, handle failed PRs, and request reviews from the repository owner (@infoyouth).

---

## 🚀 Getting Started

### 1. Clone the Repository
To get started, clone the repository to your local machine:
```
git clone https://github.com/infoyouth/assignments.git
```
### 2. Create a New Branch
Create a new branch for your assignment to keep your work organized and separate from the main branch. Follow these steps:

a. Open your terminal or command prompt.

b. Make sure you are in the repository directory:
    ```cd assignments ```
    
c. Create following directory as applicable and shown in the below tree

 ```   .
├── C                            |   ├── Java
│   ├── student1                 |   │   ├── student1
│   │   ├── assignment1.c        |   │   │   ├── assignment1
│   │   ├── assignment2.c        |   │   │   │   └── pom.xml or build.gradle
│   │   ├── Makefile             |   │   │   ├── assignment2
│   ├── student2                 |   │   │   │   └── pom.xml or build.gradle
│   │   ├── assignment1.c        |   │   ├── student2
│   │   ├── assignment2.c        |   │   │   ├── assignment1
│   │   ├── Makefile             |   │   │   │   └── pom.xml or build.gradle
│   ├── studentN                 |   │   │   ├── assignment2
│   │   ├── assignment1.c        |   │   │   │   └── pom.xml or build.gradle
│   │   ├── assignment2.c        |   │   ├── studentN
│   │   ├── Makefile             |   │   │   ├── assignment1
│                                |   │   │   │   └── pom.xml or build.gradle
├── CPP                          |   │   │   ├── assignment2
│   ├── student1                 |   │   │   │   └── pom.xml or build.gradle
│   │   ├── assignment1.cpp      |
│   │   ├── assignment2.cpp      |   ├── Python
│   │   ├── Makefile             |   │   ├── student1
│   ├── student2                 |   │   │   ├── assignment1.py
│   │   ├── assignment1.cpp      |   │   │   ├── assignment2.py
│   │   ├── assignment2.cpp      |   │   ├── student2
│   │   ├── Makefile             |   │   │   ├── assignment1.py
│   ├── studentN                 |   │   │   ├── assignment2.py
│   │   ├── assignment1.cpp      |   │   ├── studentN
│   │   ├── assignment2.cpp      |   │   │   ├── assignment1.py
│   │   ├── Makefile             |   │   │   ├── assignment2.py
                                

```
d. Create a new branch with a meaningful name:
    ```
    git checkout -b <your-branch-name>
    ```
    Replace `<your-branch-name>` with a descriptive name for your branch, such as `feature/python-assignment1`.

> 💡 **Tip**: Use branch names that reflect the task or feature you are working on to keep things organized.

### 3. Make Changes
Navigate to the folder for your assignment (e.g., `python`, `c`, `cpp`, `java`) and make the necessary changes. Follow these steps:

a. Open your terminal or command prompt.

b. Navigate to the directory for the language you are working on:
    ```
    cd <language-directory>
    ```
    Replace `<language-directory>` with the appropriate folder name, such as `python`, `c`, `cpp`, or `java`.

c. Make the necessary changes to your code files as per the assignment instructions.

> 💡 **Tip**: Regularly save your work and test your code to ensure it meets the assignment requirements.

### 4. Add and Commit Your Changes
Once you have made the necessary changes to your code files, you need to stage and commit your changes. Follow these steps:

a. Stage your changes by adding them to the Git staging area:
    ```
    git add .
    ```

b. Commit your changes with a descriptive message explaining the updates:
    ```
    git commit -m "Completed Assignment 1 in Python"
    ```

> 💡 **Tip**: Write clear and concise commit messages that describe the changes you made. This helps you and others understand the purpose of each commit.

## Further Details

For detailed instructions on each assignment, please refer to the following files:

- [Python Assignments](./python/instructions.md)
- [C Assignments](./c/instructions.md)
- [C++ Assignments](./cpp/instructions.md)
- [Java Assignments](./java/instructions.md)

---
