# Computational-Methods-Final-Project Dexter Limcangco

Sorry for the kinda unorganized README
If you are familiar with Python and prefer to use your own setup or IDE, you can simply install the required packages using your preferred method. 
The dependencies are listed in the requirements.txt file.
If your not familar you can follow the instructions below -- Thanks, Dexter

## Prerequisites
Make sure you have Python installed on your system.

## Installation
1. Run the batch file called install_requirements.bat
2. Select if you want a Virtual Environment or not
3. Run the Python Code
4. If u chose a Virtual Environment you can uninstall by trashing the repository, if not follow the instructions below.


OR YOU CAN DO THE FOLLOWING BELOW, if you don't wanna do the easy way

### Using a Virtual Environment (Recommended)
1. Create a Virtual Environment:
Open a cmd window and run the following code, make sure you open the cmd in your repository, you can do this by typing 'cmd' in the address bar once naviagated to repository:

python -m venv venv

2. Activate the Virtual Environment
Open a cmd window and run the following code:

venv\Scripts\activate

3. Install the Requirments:
Open a cmd window and run the following code:

pip install -r requirements.txt

4. Run the python code (double click the .py file or smth like that)


### Without a Virtual Enviroment
1. Open a cmd window and run the following code, make sure you open the cmd in your repository, you can do this by typing 'cmd' in the address bar once naviagated to repository:

pip install -r requirements.txt



3. Uninstall packages (optional) by running this code in a cmd prompt:

for /F "delims=" %i in (requirements.txt) do pip uninstall -y %i
