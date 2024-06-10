# Python Assignments

Welcome to the Python assignments section! Below are the assignments along with their descriptions, tasks, and examples. Feel free to expand/collapse each assignment for more information.

<details>
  <summary><span style="font-size: larger;">🔢 Assignment 1: Calculate Factorial</span></summary>
  
  ## Description
  Calculate the factorial of a given number.

  ### Details
  - **Input:** A non-negative integer `n`.
  - **Output:** The factorial of `n`.

  ### Example
  - **Input:** `5`
  - **Output:** `120`

  ## Task
  Write a Python function `factorial(n)` that calculates the factorial of a non-negative integer `n`.

</details>

<details>
  <summary><span style="font-size: larger;">🔍 Assignment 2: Prime Number Checker</span></summary>
  
  ## Description
  Check if a number is prime.

  ### Details
  - **Input:** An integer `n`.
  - **Output:** `True` if `n` is prime, `False` otherwise.

  ### Example
  - **Input:** `7`
  - **Output:** `True`

  ## Task
  Write a Python function `is_prime(n)` that checks if a number `n` is a prime number.

</details>

<details>
  <summary><span style="font-size: larger;">🔢 Assignment 3: Fibonacci Series</span></summary>
  
  ## Description
  Generate a Fibonacci series up to a given number.

  ### Details
  - **Input:** A positive integer `n`.
  - **Output:** A list of Fibonacci numbers up to `n`.

  ### Example
  - **Input:** `10`
  - **Output:** `[0, 1, 1, 2, 3, 5, 8]`

  ## Task
  Write a Python function `fibonacci(n)` that generates a list of Fibonacci numbers up to `n`.

</details>

---
# Python Projects

Welcome to the Python project section! In this project, you'll be building a small application that requires two Python files. Below are the detailed requirements and instructions on how to implement it:

<details>
  <summary><span style="font-size: larger;"><b>Interactive Number Analyzer</b></span></summary>

Welcome to the Interactive Number Analyzer project! In this project, you'll be building a small application that requires two Python files. Below are the detailed requirements and instructions on how to implement it:

## Project Requirements
- The application should consist of two Python files: `main.py` and `helper.py`.
- `main.py` should be the main entry point of the application.
- `helper.py` should contain helper functions used by `main.py`.
- The application should perform the following tasks:
  1. Accept user input for their name.
  2. Greet the user with a personalized message.
  3. Ask the user to enter a number.
  4. Use a helper function from `helper.py` to determine if the number is even or odd.
  5. Display a message indicating whether the number is even or odd.
- The application should handle invalid inputs gracefully.
- Additional Features:
  - Provide an option for the user to choose between checking if a number is even or odd.
  - Add error handling to handle non-numeric inputs.

## Methods to Implement
### In `main.py`:
1. `get_user_name()`: Method to accept user input for their name.
   - No arguments needed.
   - Returns the user's name as a string.
   
2. `get_user_choice()`: Method to accept user input for choosing between even or odd.
   - No arguments needed.
   - Returns the user's choice as a string ('even' or 'odd').
   
3. `get_user_number()`: Method to accept user input for a number.
   - No arguments needed.
   - Returns the user's number as an integer.
   
4. `greet_user(name)`: Method to greet the user with a personalized message.
   - Arguments: `name` (string) - The user's name.

### In `helper.py`:
1. `is_even(number)`: Method to determine if a number is even.
   - Arguments: `number` (int) - The number to check.
   - Returns `True` if the number is even, `False` otherwise.

2. `is_odd(number)`: Method to determine if a number is odd.
   - Arguments: `number` (int) - The number to check.
   - Returns `True` if the number is odd, `False` otherwise.

## Implementation Instructions
1. Create a new folder named `interactive_number_analyzer` within the `assignments/python` directory.
2. Inside the `interactive_number_analyzer` folder, create two Python files: `main.py` and `helper.py`.
3. Implement the methods described above in `main.py` and `helper.py`.
4. Import the required methods from `helper.py` into `main.py` as needed.
5. Implement error handling to handle non-numeric inputs and other edge cases.
6. Test your application thoroughly with various inputs to ensure it works as expected.
7. Document your code and include comments where necessary.

Good luck with your project!

</details>

# What all needed to submit
<details>
  <summary><span style="font-size: larger;"><b>Submission</b></span></summary>

## Definition of Done Requirements
To consider your project completed and ready for submission, ensure the following criteria are met:
- All PR (Pull Request) checks are green, indicating that your code passes all automated checks.
- Your PR has received approval from at least one reviewer.
- You have addressed any feedback or suggestions provided by the reviewer.
- You have thoroughly tested your application with various inputs to ensure it works correctly.
- You have documented your code and included comments where necessary.
- You have attached screenshots of the output of your application to showcase its functionality.

## Attaching Output Screenshots
When submitting your project, please ensure to attach screenshots of the output of your application. This will help demonstrate the functionality of your code and provide clarity to the reviewers. You can include screenshots of:
- The application prompting for user input.
- The application displaying the output based on the input provided.
- Any relevant error messages or edge cases handled by your code.

### Example Screenshots:
![Input Prompt](path/to/input_prompt_screenshot.png)
![Output Display](path/to/output_display_screenshot.png)
![Error Handling](path/to/error_handling_screenshot.png)

Ensure that the screenshots are clear and readable. If your application has multiple screens or outputs, include screenshots for each relevant step.

Once all the above requirements are met, you can proceed to submit your project.

</details>
