<!---

TASK LIST:

  * Use cp -rf *.* to copy all of the files and directories in this repository
    to the starter repository for this assignment
  * Change into the directory for the starer repository
  * Update the header (e.g., #) to only give the name of the assignment
  * Update the first paragraph to include the commented-out content
  * Change the link in the # Problems section to point to this lab's starter
  * Create the assignment in the GitHub Classroom, noting the URL
  * Test the assignment by accepting it with your own GitHub account
  * Check to ensure that your GitHub repository is created correctly
  * Share the assignment link with all of the students using email or Slack

PROBLEMS?

  * Contact Gregory M. Kapfhammer by email or Slack
  * Raise an issue in the GitHub repository for this assignment

-->

# cs280-F2017-lab1

Designed for use with [GitHub Classroom](https://classroom.github.com/), this
repository contains the solution for Laboratory 1 in Computer Science 280.
Since the Travis builds for this repository will initially fail (as evidenced
by a red &#x2717; appearing in the commit logs instead of a green &#x2714;),
the programmer is responsible for completing all of the steps needed to satisfy
the requirements for the assignment, thus causing a &#x2714; to instead appear
in the commit logs.

## Introduction

This assignment requires a programmer to implement and test a Python 3 program,
called `duplicates.py`, that will remove the duplicate values between two input
lists. Currently, the provided version of the system does not work correctly.
You can read the comments in the source code of the `duplicates.py` file to
understand how the program is intended to work. Then, you will have to find and
fix the defect(s) in this program.

The programmer is also responsible for writing a two-paragraph reflection, added
to the file called `README.md`, that explains the challenges that you faced and
the solutions you developed. This is a Markdown file that must adhere to the
standards described in the [Markdown Syntax
Guide](https://guides.github.com/features/mastering-markdown/). Remember, you
can preview the contents of a comitted Markdown file by clicking on the name of
the file in your GitHub repository. Finally, don't forget that your `README.md`
file should adhere to the Markdown standards established by the [Markdown
linting tool](https://github.com/markdownlint/markdownlint).

<!---

Available for download at [Computer Science 111 Lab
1](https://github.com/Allegheny-Computer-Science-111-F2017/cs111-F2017-lab-sheets/releases/download/cs111F2017_lab01-1.0.4/cs111F2017_lab01.pdf),
the carefully formatted assignment sheet for this project provides more details
about the steps that a computer scientist should take to complete this
assignment. You can also view this same assignment sheet by visiting the listing
of laboratories on the course web site.

--->

## Learning

If you have not done so already, please read all of the relevant [GitHub
Guides](https://guides.github.com/) that explain how to use many of the features
that GitHub provides. In particular, please make sure that you have read the
following GitHub guides: [Mastering
Markdown](https://guides.github.com/features/mastering-markdown/), [Hello
World](https://guides.github.com/activities/hello-world/), and [Documenting Your
Projects on GitHub](https://guides.github.com/features/wikis/). Each of these
guides will help you to understand how to use both [GitHub](http://github.com) and
[GitHub Classroom](https://classroom.github.com/).

To do well on this assignment, you should also read Chapter 1 of the SETP course
textbook, paying particularly close attention to Sections 1.3 through 1.5 and
the discussion of software quality and system boundaries. Please see the course
instructor if you have questions about any of these reading assignments.

## Requirements

The Python3 software that supports this assignment requires you to install the
`pytest` library by typing the command `python3 -m pip install --user -r
duplicates/requirements.txt` from the root directory of your GitHub repository.

## Commands

When you are in the `duplicates` directory of your GitHub repository, you can
type the command `python3 duplicates.py --listone 1 2 3 4 --listtwo 1 2 5 6`. The
correct version of this program would then produce the following output.

```
Duplicates removes duplicates from lists

Removing the duplicates:

List one: ['3', '4']
List two: ['1', '2', '5', '6']

```

However, when you run the provided version of the program, you should notice
that it does not produce the same output. This means that there is a defect in
this program! In fact, when you run the test suite for the program with the
command `pytest tests` in the `duplicates` directory you should notice that the
test suite fails.

## Assignment

For this assignment, you are invited to find and fix the defect in this program.
If you would like to learn more about the Python 3 programming language, then
you can download the book [A Whirlwind Tour of
Python](http://www.oreilly.com/programming/free/a-whirlwind-tour-of-python.csp)
for free. After learning more about Python 3 and finding the defect, you should
ensure that your program produces the intended output in the terminal window.
Next, you should ensure that the test suite for your program passes correctly.
After the tests pass, you should add at least four more test cases that all
successfully demonstrate that your program is working correctly.

Finally, you should edit the file, called `README.md`, in your GitHub
repository. This file should contain a new header called `## Reflection` and,
additionally, a two paragraph reflection on your experiences when completing
this laboratory assignment. The first paragraph in your reflection should
comment on the challenges that you experienced and the steps that you took to
handle them. The second paragraph must state what the defect was in the program
and how you fixed it.

## Updates

If the course instructor updates the provided material for this assignment and
you would like to receive these updates, then you can type this command in the
main directory for this assignment:

```
git remote add download git@github.com:Allegheny-Computer-Science-280-F2017/cs280-F2017-lab1-starter.git
```

You should only need to type this command once; typing the command additional
times may yield an error message but will not negatively influence the state of
your repository. Now, you are ready to download the updates provided by the
course instructor by typing:

```
git pull download master
```

This second command can be run whenever the course instructor needs to provide
you with new source code for this assignment. However, please note that, if you
have edited the files that the course instructor updated, running the previous
command may lead to Git merge conflicts. If this happens, you may need to
manually resolve them with the help of the instructor or a teaching assistant.

## Travis

This assignment uses [Travis CI](https://travis-ci.com/) to automatically run
the test suite for the program every time you commit to your GitHub repository.
The checking will start as soon as you have accepted the assignment, thus
creating your own private repository, and the course instructor enables Travis
for it. If you are using Travis for the first time, you will need to authorize
Travis CI to access the private repositories that you created on GitHub.

## Problems

If you have found a problem with this assignment's provided source code, then
you can go to the [Computer Science 280 Lab 1
Starter](https://github.com/Allegheny-Computer-Science-280-F2017/cs280-F2017-lab1-starter)
repository and create an issue by clicking the "Issues" tab and then clicking
the green "New Issue" button. To ensure that your issue is properly resolved,
please provide as many details as is possible about the problem that you
experienced. If you discover a problem with the laboratory assignment sheet,
then please raise an issue in the
[cs280-F2017-lab-sheets](https://github.com/Allegheny-Computer-Science-280-F2017/cs280-F2017-lab-sheets)
repository and mention this assignment.

Students who find, and use the appropriate GitHub issue tracker to correctly
document, a mistake in any aspect of this laboratory assignment will receive
free laptop stickers and extra credit towards their grade for it.

## Assistance

If you are having trouble completing any part of this project, then please talk
with the course instructor. Alternatively, you may ask questions in the Slack
team for this course. Finally, you can schedule a meeting during the course
instructor's office hours.

## Reflection

	I found this lab extremely challenging. I have never written in python or even used GitHub before so it seemed like every step stumped me. I spent the majority of the lab session just reading about GitHub through all the links posted in the lab assignment and then attempting to gain at least a basic understanding of python. The remainder of the lab, for me, was spent on setting everything up properly and dissecting the ReadMe file. My GitHub was not set up properly at first so I could not run the program. I fixed this with Professor Kapfhammer’s help by using export PATH="${PATH}:$HOME/.local/bin" and adding that to $HOME/.zprofile. I spent the next three days reading and re-reading the python file, looking up all the words, and trying to figure out where the error could be. It was very difficult for me because I am very inexperienced with python and there were no error statements to give me any guidances. This made it much more difficult because everything was “right” It just did not run right. 
	Once I finally located and fixed the error – with help from one of the computer science TA’s – I ran a few different number lists in order to make sure all duplicates were removed. I had planned on writing my own test cases, but I ran out of time. If I had, had time, however, I would have   tested different data types. The current program is only written to handle strings. It could be improved by also taking ints, floats, and chars. I would have also written test cases to check if the program could handle and fix more than one duplicate, no input at all, varying sized lists, and elements in list two that exist in list one. Although I did not have time for all of this, this lab was still an incredible learning experience for me. I  now have a much better understanding of python and, although I did not get the chance to implement them, I have spent a great deal of time thinking about good testing practices and code development. I now also understand how to use GitHub – how to access labs and information and how to submit work. 