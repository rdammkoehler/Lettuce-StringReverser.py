# String Reverser in Python using Lettuce to Test Drive

I made this project as part of my learning process for both Python
and the lettuce testing framework. Aside from suffering some painful
lessons about how Python import works, a stellar success. 

I will be adding to the project over the next few days to experiment
with the range of features available in lettuce.

## Usage

You will need a valid/working Python environment with the lettuce
test framework installed. 

Python  http://www.python.org/
PIP     
Lettuce http://lettuce.it/index.html

# Step by Step Construction

## Get Python

### Mac users

You are in luck, already installed.

### Ubuntu Users

```bash
sudo apt-get install python2.6
```

### Windows

Visit the Python download page _http://www.python.org/download/_ and select the correct installer for your environment

## Get PIP

PIP is the package installer for Python. Use the installation instructions here _http://guide.python-distribute.org/installation.html#pip-installs-python-pip_ to install it.

## Get Lettuce



# Lazy Route: Just use the repo

After checkout, from the top directory of this project, run;

```bash
lettuce tests
```

You should see output like this (note, on my Mac I can't see the lines output, presume its my color scheme)

```bash
Feature: Reverse Words in a String                                                                                     # tests/features/reverse.feature:1
  In order to read backwards                                                                                           # tests/features/reverse.feature:2
  readers must have the words in their text reveresed                                                                  # tests/features/reverse.feature:3

  Scenario: Empty String Reversal                                                                                      # tests/features/reverse.feature:5
    Given a String Reverser                                                                                            # tests/features/reverse_steps.py:9
    When I reverse the string ""                                                                                       # tests/features/reverse_steps.py:13
    Then the result is ""                                                                                              # tests/features/reverse_steps.py:17

  Scenario: Single Character Reversal                                                                                  # tests/features/reverse.feature:10
    Given a String Reverser                                                                                            # tests/features/reverse_steps.py:9
    When I reverse the string "A"                                                                                      # tests/features/reverse_steps.py:13
    Then the result is "A"                                                                                             # tests/features/reverse_steps.py:17

  Scenario: Multicharacter Word Reversal                                                                               # tests/features/reverse.feature:15
    Given a String Reverser                                                                                            # tests/features/reverse_steps.py:9
    When I reverse the string "Bacon"                                                                                  # tests/features/reverse_steps.py:13
    Then the result is "Bacon"                                                                                         # tests/features/reverse_steps.py:17

  Scenario: Multiword String Reversal                                                                                  # tests/features/reverse.feature:20
    Given a String Reverser                                                                                            # tests/features/reverse_steps.py:9
    When I reverse the string "Bacon is the life blood of Agile Software Development"                                  # tests/features/reverse_steps.py:13
    Then the result is "Development Software Agile of blood life the is Bacon"                                         # tests/features/reverse_steps.py:17

  Scenario: Palindrome String Reversal                                                                                 # tests/features/reverse.feature:25
    Given a String Reverser                                                                                            # tests/features/reverse_steps.py:9
    When I reverse the string "Rats Live on no Evil Star"                                                              # tests/features/reverse_steps.py:13
    Then the result is "Star Evil no on Live Rats"                                                                     # tests/features/reverse_steps.py:17

  Scenario: Consolidated Table Example                                                                                 # tests/features/reverse.feature:30
    Given a String Reverser                                                                                            # tests/features/reverse_steps.py:9
    When I reverse these strings:                                                                                      # tests/features/reverse_steps.py:21
      | input                                                 |
      |                                                       |
      | A                                                     |
      | Bacon                                                 |
      | Bacon is the life blood of Agile Software Development |
      | Rats Live on no Evil Star                             |
    Then the results are:                                                                                              # tests/features/reverse_steps.py:29
      | output                                                |
      |                                                       |
      | A                                                     |
      | Bacon                                                 |
      | Development Software Agile of blood life the is Bacon |
      | Star Evil no on Live Rats                             |

  Scenario Outline: Outline Example                                                                                    # tests/features/reverse.feature:47
    Given a String Reverser                                                                                            # tests/features/reverse_steps.py:9
    When I reverse the string "<a string>"                                                                             # tests/features/reverse_steps.py:13
    Then the result is "<reversed string>"                                                                             # tests/features/reverse_steps.py:17

  Examples:
    | a string                                              | reversed string                                       |
    |                                                       |                                                       |
    | A                                                     | A                                                     |
    | bacon                                                 | bacon                                                 |
    | Bacon is the life blood of Agile Software Development | Development Software Agile of blood life the is Bacon |
    | Rats Live on no Evil Star                             | Star Evil no on Live Rats                             |

1 feature (1 passed)
11 scenarios (11 passed)
33 steps (33 passed)
```
