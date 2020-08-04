# Leetcode Solution Tester

This repositor contains files to automate the execution of the manual testcases on Leetcode. Automated testing of manual testcases can provide quite a few benefits. Some are listed below:
- More frequent tests for any code changes made in the solution, thus reducing the probability of a wrong submission.
- Avoid running into regressions introduced during performace optimizations

<br />
## Tool

The idea is to use Browser Based GUI automation (Python and Selenium) to execute the test cases listed by the user to verify the correctness of the program. The procedure to use the tool is described below:
- Start the tool and enter the problem url.
- The tool will open a browser window. Login and load your solution into the solution space.
- Provide the necessary test cases in the test cases file. 
- Now you are ready to run the automations using the tool.

The tool will not exit after running the automations. You can modify the code and call the test case runner multiple times before deciciding to submit the code.

<br />
## Input Test Cases File

The input to the automation tool is a set of manual test cases that need to be executed. The test cases can be provided in a 'testcases.txt'. The script will expect the presence of this file in the same folder and will parse the testcases by reading its contents. The testcases that need to be executed can be populated in the text file. The test cases must appear in file as they would in the custom test case input box. The test cases are separated by a new line starting with a semicolon (';'). A sample testcase file is provided in the repository 

Prerequists:
- This tool performs automations in the browser. Ensure that the Selenium package and the corresponsding Web-drivers are properly installed on your system. 
