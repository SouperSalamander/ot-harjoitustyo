# Usage Instructions

The first thing to do is download the program from the release `loppupalautus` found in the `README` file. Then run `poetry install`. 

To start the program, run `poetry run invoke start`.

### First time user:

When using the program for the first time the user will be required to make an account. To do this, pick an available username and a password containing both a letter and a number.
Type username and password into the entry boxes, press the “Enter” button.
If the username and password meet the given requirements (available username, strong password, password confirmation matches) the user will be taken to the login page. 
Otherwise, a relevant error message will be shown and the user can change their chosen account details accordingly.

### To log in:

On the log in frame the user will enter their username and password and then they will press the “Enter” button.
If the username exists and the password on file for that username matches the one that had been entered then the user will be taken to the main menu page.
If the details don’t exist or the password doesn't match then the user will be shown an error message and will have to either try again to login or make a new account.

### Once on the menu page:

The user will choose between “Greatest Common Factor”, “Lowest Common Multiple”, “Prime Factorisation”, “Test Yourself”, “Search History”, and “Log Out” by pressing the respective button. 
Each button takes the user to a different part of the program.

### After choosing “Greatest Common Factor”:

In this frame the user can enter a number into each of the two entry boxes and then press “Calculate”.
This will calculate the greatest common factor of the two numbers using euclid's algorithm and output a step by step solution for the user.
It will also add the numbers and result to the user’s search history.
From there they can press “clear” which will clear the frame of the current solution. Alternatively they can press “back” which returns the user to the menu frame.

### After choosing “Lowest Common Multiple”:

In this frame the user can enter a number into each of the two entry boxes and then press “Calculate”.
This will calculate the lowest common multiple of the two numbers by dividing the product of the numbers by the greatest common factor of the numbers and output a step by step solution for the user.
It will also add the numbers and result to the user’s search history.
From there they can press “clear” which will clear the frame of the current solution. Alternatively they can press “back” which returns the user to the menu frame.

### After choosing “Prime Factorisation”:

In this frame the user can enter a number into the entry box and then press “Calculate”.
This will display the number as the product of its prime factors.
It will also add the number and result to the user’s search history.
From there they can press “clear” which will clear the frame of the current solution. Alternatively they can press “back” which returns the user to the menu frame.

### After choosing “Test Yourself”:

The user is taken to a page where they can choose the test topic. Currently the available topics are “Greatest Common Factor”, "Lowest Common Multiple", and "Prime Factorisation". 
This is selected by pressing the button with the same name.
The user will then be given a random number theory question on the chosen topic. 
The answer is typed into the entry box. 
After pressing enter the user will find out if they were correct or incorrect. 
From there they can either press “try again” to get a new question, or they can press “back” to return to the topic menu in the test yourself section.
Pressing the “back” button will return the user to the main menu.

### After choosing “Search History”:

The user will be shown all their previous searches.
Pressing the “back” button returns the user to the main menu.

### After choosing “Log Out”:

The user will be returned to the very beginning of the program.
Where they can either log in, create an account, or exit the program.
