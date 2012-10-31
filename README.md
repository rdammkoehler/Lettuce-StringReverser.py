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

You are in luck, python is already installed.

### Ubuntu Users

```bash
sudo apt-get install python2.6
```

### Windows

Visit the Python download page _http://www.python.org/download/_ and select the correct installer for your environment

## Get PIP

PIP is the package installer for Python. Use the installation instructions here _http://guide.python-distribute.org/installation.html#pip-installs-python-pip_ to install it.

## Get Lettuce

PIP will install lettuce for you;

```bash
pip install lettuce
```

If you are so inclined you can visit the lettuce site for information on getting the source code here _http://lettuce.it/intro/install.html#intro-install_

# Getting started

## Create a project folder

_Assuming you start from your home directory_

```bash
mkdir -p projects/string_reverser/tests/features
mkdir -p projects/string_reverser/string_reverser
```

## Start with your feature file

Create a feature file. Lettuce feature files are pretty much identical to Gherkin feature files used in Cucumber.

Put the following text in your feature file

```bash
Feature: Reverse Words in a String
  In order to read backwards
  readers must have the words in their text reveresed

  Scenario: Empty String Reversal
    Given a String Reverser
    When I reverse the string ""
    Then the result is ""
```

## Run your feature

Before going any farther, lets make sure that we can run the lettuce feature.

From the command line, change directory to the top level project directory

```bash
cd ~/projects/string_reverser
```

Now invoke lettuce

```bash
lettuce tests
```

You should see output similar to this;

```bash
Feature: Reverse Words in a String                    # tests/features/reverse.feature:1
  In order to read backwards                          # tests/features/reverse.feature:2
  readers must have the words in their text reveresed # tests/features/reverse.feature:3

  Scenario: Empty String Reversal                     # tests/features/reverse.feature:5
    Given a String Reverser                           # tests/features/reverse.feature:6
    When I reverse the string ""                      # tests/features/reverse.feature:7
    Then the result is ""                             # tests/features/reverse.feature:8

1 feature (0 passed)
1 scenario (0 passed)
3 steps (3 undefined, 0 passed)

You can implement step definitions for undefined steps with these snippets:

# -*- coding: utf-8 -*-
from lettuce import step

@step(u'Given a String Reverser')
def given_a_string_reverser(step):
    assert False, 'This step must be implemented'
@step(u'When I reverse the string ""')
def when_i_reverse_the_string(step):
    assert False, 'This step must be implemented'
@step(u'Then the result is ""')
def then_the_result_is(step):
    assert False, 'This step must be implemented'
```

## Create a Steps file

Copy the output from running lettuce into a file called reverser_steps.py, place this file in your _tests/features_ folder.

The file should look like this;

```python
# -*- coding: utf-8 -*-
from lettuce import step

@step(u'Given a String Reverser')
def given_a_string_reverser(step):
    assert False, 'This step must be implemented'
@step(u'When I reverse the string ""')
def when_i_reverse_the_string(step):
    assert False, 'This step must be implemented'
@step(u'Then the result is ""')
def then_the_result_is(step):
    assert False, 'This step must be implemented'
```

Now run your feature again!

```bash
```

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
