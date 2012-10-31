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

Create a feature file. Lettuce feature files are pretty much identical to Gherkin feature files used in Cucumber. This 
process is very similar to Test Driving code, however we will use the Gherkin-like syntax that Lettuce uses. 
This is a simple format in which we describe features using the keywords _Feature:_ and _Scenario:_. 
A feature is made up of one or more scenarios. Each scenario is made up of statements in the form _Given_, _When_, _Then_.
Note that a _Feature:_ is followed by its name and optionally a description.
A _Scenario:_ is follwed by its name and optionally a description.
You may have more than one _Given_, _When_, or _Then_. 

Later we will discuss other techniques for specifying Scenarios. However, we will start with something simple first.

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
lettuce tests
```

And you output should look approximately like this;

```bash
Feature: Reverse Words in a String                    # tests/features/reverse.feature:1
  In order to read backwards                          # tests/features/reverse.feature:2
  readers must have the words in their text reveresed # tests/features/reverse.feature:3

  Scenario: Empty String Reversal                     # tests/features/reverse.feature:5
    Given a String Reverser                           # tests/features/reverse_s    Given a String Reverser                           # tests/features/reverse_steps.py:7
    Traceback (most recent call last):
      File "/Library/Python/2.7/site-packages/lettuce/core.py", line 141, in __call__
        ret = self.function(self.step, *args, **kw)
      File "/Users/rich/projects/python/lettuce_demo/tests/features/reverse_steps.py", line 8, in given_a_string_reverser
        assert False, 'This step must be implemented'
    AssertionError: This step must be implemented
    When I reverse the string ""                      # tests/features/reverse_s    When I reverse the string ""                      # tests/features/reverse_steps.py:10
    Then the result is ""                             # tests/features/reverse_s    Then the result is ""                             # tests/features/reverse_steps.py:13

1 feature (0 passed)
1 scenario (0 passed)
3 steps (1 failed, 2 skipped, 0 passed)
```

## Fill in the steps

The _@step_ annotation is used to match method definitions with the lines in the _feature_ file. The string 
argument to _@step_ is a regular expression that should match one or more lines in the _feature_. As we saw above,
if a _@step_ is missing, Lettuce will print out the required code for your steps file. Presently we have these steps;

```python
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

Each _@step_ matches a line in our initial _feature_ file's first _scenario_

```bash
  Scenario: Empty String Reversal
    Given a String Reverser
    When I reverse the string ""
    Then the result is ""
```

### Step 1: Given a String Reverser

Just like using any other test first approach, we want to define our test code before we create a solution. 

First we need to add to our imports to get access to the _world_ object in Lettuce. Modify your import to look like this.

```python
from lettuce import step, world
```

Lets start with our _Given_ _step_.

```python
@step(u'Given a String Reverser')
def given_a_string_reverser(step):
    world.reverser = Reverser()
```

This code very simply creates an instance of our String Reverser (_Reverser_) and assigns it to the _world_ object.
Here we are leveraging the open-class capabilities of Python. In all other steps _world.reverser_ will give us reference 
to our String Reverser.

## Run again

```bash
lettuce tests
```

The output will look like this;

```bash
Feature: Reverse Words in a String                    # tests/features/reverse.feature:1
  In order to read backwards                          # tests/features/reverse.feature:2
  readers must have the words in their text reveresed # tests/features/reverse.feature:3

  Scenario: Empty String Reversal                     # tests/features/reverse.feature:5
    Given a String Reverser                           # tests/features/reverse_s    Given a String Reverser                           # tests/features/reverse_steps.py:15
    Traceback (most recent call last):
      File "/Library/Python/2.7/site-packages/lettuce/core.py", line 141, in __call__
        ret = self.function(self.step, *args, **kw)
      File "/Users/rich/projects/python/lettuce_demo/tests/features/reverse_steps.py", line 16, in given_a_string_reverser
        world.reverser = Reverser()
    NameError: global name 'Reverser' is not defined
    When I reverse the string ""                      # tests/features/reverse_s    When I reverse the string ""                      # tests/features/reverse_steps.py:7
    Then the result is ""                             # tests/features/reverse_s    Then the result is ""                             # tests/features/reverse_steps.py:11

1 feature (0 passed)
1 scenario (0 passed)
3 steps (1 failed, 2 skipped, 0 passed)
```

This is of course because caused by the lack of a definition for our String Reverser class. So we need to create that before 
we proceed.

## Create the String Reverser

During setup we created a subdirectory in our project called _string_reverser_. We need to create two files in that location.

First create an empty file named __init.py__

```bash
touch ~/projects/string_reverser/string_reverser/__init__.py
```

>
> Windows Users: The _touch_ command does not exist on Windows. Use your text editor or file manager to create an empty file.
>

This file tells python that the folder contains a module.

Next, we need to define the class Reverser.

Create a file in the _string_reverser_ subdirectory called _string_reverser.py_

Add the following content to that file;

```python
# -*- coding: utf-8 -*-

class Reverser(object):
      pass
```

Return to your steps file and add an import for this new module after the import for lettuce.

```python
from string_reverser.string_reverser import Reverser 
```

## Run again

```bash
lettuce tests
```

Your output should look like this;

```bash
Feature: Reverse Words in a String                    # tests/features/reverse.feature:1
  In order to read backwards                          # tests/features/reverse.feature:2
  readers must have the words in their text reveresed # tests/features/reverse.feature:3

  Scenario: Empty String Reversal                     # tests/features/reverse.feature:5
    Given a String Reverser                           # tests/features/reverse_s    Given a String Reverser                           # tests/features/reverse_steps.py:8
    When I reverse the string ""                      # tests/features/reverse_s    When I reverse the string ""                      # tests/features/reverse_steps.py:12
    Traceback (most recent call last):
      File "/Library/Python/2.7/site-packages/lettuce/core.py", line 141, in __call__
        ret = self.function(self.step, *args, **kw)
      File "/Users/rich/projects/python/lettuce_demo/tests/features/reverse_steps.py", line 13, in when_i_reverse_the_string
        assert False, 'This step must be implemented'
    AssertionError: This step must be implemented
    Then the result is ""                             # tests/features/reverse_s    Then the result is ""                             # tests/features/reverse_steps.py:16

1 feature (0 passed)
1 scenario (0 passed)
3 steps (1 failed, 1 skipped, 1 passed)
```

As you can see, our _Given_ step now passes, however our other steps are still failing. 

## Step 2: Fill in the _When_ step

Lets add code to complete the other steps we have defined. 
Leveraging the open nature of python objects, in our _When_ step, use the reverser to reverse the input ""

```python
@step(u'When I reverse the string ""')
def when_i_reverse_the_string_group1(step):
    world.result = world.reverser.reverse("")
```

## Run again

```bash
lettuce tests
```

Your output should look like this;

```bash
Feature: Reverse Words in a String                    # tests/features/reverse.feature:1
  In order to read backwards                          # tests/features/reverse.feature:2
  readers must have the words in their text reveresed # tests/features/reverse.feature:3

  Scenario: Empty String Reversal                     # tests/features/reverse.feature:5
    Given a String Reverser                           # tests/features/reverse_s    Given a String Reverser                           # tests/features/reverse_steps.py:8
    When I reverse the string ""                      # tests/features/reverse_s    When I reverse the string ""                      # tests/features/reverse_steps.py:12
    Traceback (most recent call last):
      File "/Library/Python/2.7/site-packages/lettuce/core.py", line 141, in __call__
        ret = self.function(self.step, *args, **kw)
      File "/Users/rich/projects/python/lettuce_demo/tests/features/reverse_steps.py", line 13, in when_i_reverse_the_string_group1
        world.result = world.reverser.reverse("")
    AttributeError: 'Reverser' object has no attribute 'reverse'
    Then the result is ""                             # tests/features/reverse_s    Then the result is ""                             # tests/features/reverse_steps.py:16

1 feature (0 passed)
1 scenario (0 passed)
3 steps (1 failed, 1 skipped, 1 passed)
```

The test fails of course because we have not defined the _reverse(input)_ method. 

## Adding to the String Reverser

Lets add the _reverse(input)_ method to our _Reverser_ class.
Modify the code in _string_reverser.py_ to look like this;

```python
# -*- coding: utf-8 -*-

class Reverser(object):
    def __init__(self):
        pass

    def reverse(self,input):
    	pass
```

## Run again

```bash
lettuce tests
```

Your output should look like this;

```bash
Feature: Reverse Words in a String                    # tests/features/reverse.feature:1
  In order to read backwards                          # tests/features/reverse.feature:2
  readers must have the words in their text reveresed # tests/features/reverse.feature:3

  Scenario: Empty String Reversal                     # tests/features/reverse.feature:5
    Given a String Reverser                           # tests/features/reverse_s    Given a String Reverser                           # tests/features/reverse_steps.py:8
    When I reverse the string ""                      # tests/features/reverse_s    When I reverse the string ""                      # tests/features/reverse_steps.py:12
    Then the result is ""                             # tests/features/reverse_s    Then the result is ""                             # tests/features/reverse_steps.py:16
    Traceback (most recent call last):
      File "/Library/Python/2.7/site-packages/lettuce/core.py", line 141, in __call__
        ret = self.function(self.step, *args, **kw)
      File "/Users/rich/projects/python/lettuce_demo/tests/features/reverse_steps.py", line 17, in then_the_result_is
        assert False, 'This step must be implemented'
    AssertionError: This step must be implemented

1 feature (0 passed)
1 scenario (0 passed)
3 steps (1 failed, 2 passed)
```

## Step 3: Fill in the _Then_ step

Our test is failing because we have not finished the definition of the _Then_ step. Here we will simply compare the
result of our _Then_ step, stored in _world.result_ with our expected output, ""

Modify your third step to look like this;

```python
@step(u'Then the result is ""')
def then_the_result_is(step):
    assert world.result == "", 'result does not match expectation' 
```

## Run again

```bash
lettuce tests
```

Your output should look like this;

```bash
Feature: Reverse Words in a String                    # tests/features/reverse.feature:1
  In order to read backwards                          # tests/features/reverse.feature:2
  readers must have the words in their text reveresed # tests/features/reverse.feature:3

  Scenario: Empty String Reversal                     # tests/features/reverse.feature:5
    Given a String Reverser                           # tests/features/reverse_s    Given a String Reverser                           # tests/features/reverse_steps.py:9
    When I reverse the string ""                      # tests/features/reverse_s    When I reverse the string ""                      # tests/features/reverse_steps.py:13
    Then the result is ""                             # tests/features/reverse_s    Then the result is ""                             # tests/features/reverse_steps.py:17
    Traceback (most recent call last):
      File "/Library/Python/2.7/site-packages/lettuce/core.py", line 141, in __call__
        ret = self.function(self.step, *args, **kw)
      File "/Users/rich/projects/python/lettuce_demo/tests/features/reverse_steps.py", line 18, in then_the_result_is_group1
        assert world.result == "", 'result does not match expectation'
    AssertionError: result does not match expectation

1 feature (0 passed)
1 scenario (0 passed)
3 steps (1 failed, 2 passed)
```

This test executes but fails because we need to complete the _Reverser_ code. 

Modify your _Reverser_ to look like this;

```python
class Reverser(object):
    def __init__(self):
        pass

    def reverse(self,input):
    	return ""
```

## Run again

```bash
lettuce tests
```

Your output should look like this;

```bash
Feature: Reverse Words in a String                    # tests/features/reverse.feature:1
  In order to read backwards                          # tests/features/reverse.feature:2
  readers must have the words in their text reveresed # tests/features/reverse.feature:3

  Scenario: Empty String Reversal                     # tests/features/reverse.feature:5
    Given a String Reverser                           # tests/features/reverse_s    Given a String Reverser                           # tests/features/reverse_steps.py:8
    When I reverse the string ""                      # tests/features/reverse_s    When I reverse the string ""                      # tests/features/reverse_steps.py:12
    Then the result is ""                             # tests/features/reverse_s    Then the result is ""                             # tests/features/reverse_steps.py:16

1 feature (1 passed)
1 scenario (1 passed)
3 steps (3 passed)
```

## Adding more _scenarios_

Go back to your _reverse.feature_ file and add another _scenario_ to the file;

```gherkin
  Scenario: Single Character Reversal
    Given a String Reverser
    When I reverse the string "A"
    Then the result is "A"
```

## Run again

```bash
lettuce tests
```

Your output should look like this;

```bash
Feature: Reverse Words in a String                    # tests/features/reverse.feature:1
  In order to read backwards                          # tests/features/reverse.feature:2
  readers must have the words in their text reveresed # tests/features/reverse.feature:3

  Scenario: Empty String Reversal                     # tests/features/reverse.feature:5
    Given a String Reverser                           # tests/features/reverse_s    Given a String Reverser                           # tests/features/reverse_steps.py:9
    When I reverse the string ""                      # tests/features/reverse_s    When I reverse the string ""                      # tests/features/reverse_steps.py:13
    Then the result is ""                             # tests/features/reverse_s    Then the result is ""                             # tests/features/reverse_steps.py:17

  Scenario: Single Character Reversal                 # tests/features/reverse.feature:10
    Given a String Reverser                           # tests/features/reverse_s    Given a String Reverser                           # tests/features/reverse_steps.py:9
    When I reverse the string "A"                     # tests/features/reverse.feature:12
    Then the result is "A"                            # tests/features/reverse.feature:13

1 feature (0 passed)
2 scenarios (1 passed)
6 steps (2 undefined, 4 passed)

You can implement step definitions for undefined steps with these snippets:

# -*- coding: utf-8 -*-
from lettuce import step

@step(u'When I reverse the string "([^"]*)"')
def when_i_reverse_the_string_group1(step, group1):
    assert False, 'This step must be implemented'
@step(u'Then the result is "([^"]*)"')
def then_the_result_is_group1(step, group1):
    assert False, 'This step must be implemented'
```

Notice that lettuce is indicating that we are missing some steps. But, we are _not_ going to add new steps, rather
we will modify the steps we already have defined. [This is really a short cut.]

## Add Regular Expressions to Existing Steps

The two steps that lettuce is asking us to add are essentially the same as the existing _When_ and _Then_ steps, but they
include regular expression matches for the quoted text. 

>
> If you need help with Regular Expressions, try this site: http://www.regular-expressions.info/
>

Modify your steps by replacing the _step_ matcher for your _When_ and _Then_ steps. The file should look like this;

```python
from lettuce import step, world
from string_reverser.string_reverser import Reverser 

@step(u'Given a String Reverser')
def given_a_string_reverser(step):
    world.reverser = Reverser()

@step(u'When I reverse the string "([^"]*)"')
def when_i_reverse_the_string_group1(step, group1):
    world.result = world.reverser.reverse(group1)

@step(u'Then the result is "([^"]*)"')
def then_the_result_is_group1(step, group1):
    assert world.result == group1, 'result does not match expectation'
```

## Run again

```bash
lettuce tests
```

Your output should look like this;

```bash
Feature: Reverse Words in a String                    # tests/features/reverse.feature:1
  In order to read backwards                          # tests/features/reverse.feature:2
  readers must have the words in their text reveresed # tests/features/reverse.feature:3

  Scenario: Empty String Reversal                     # tests/features/reverse.feature:5
    Given a String Reverser                           # tests/features/reverse_s    Given a String Reverser                           # tests/features/reverse_steps.py:9
    When I reverse the string ""                      # tests/features/reverse_s    When I reverse the string ""                      # tests/features/reverse_steps.py:13
    Then the result is ""                             # tests/features/reverse_s    Then the result is ""                             # tests/features/reverse_steps.py:17

  Scenario: Single Character Reversal                 # tests/features/reverse.feature:10
    Given a String Reverser                           # tests/features/reverse_s    Given a String Reverser                           # tests/features/reverse_steps.py:9
    When I reverse the string "A"                     # tests/features/reverse_s    When I reverse the string "A"                     # tests/features/reverse_steps.py:13
    Then the result is "A"                            # tests/features/reverse_s    Then the result is "A"                            # tests/features/reverse_steps.py:17
    Traceback (most recent call last):
      File "/Library/Python/2.7/site-packages/lettuce/core.py", line 141, in __call__
        ret = self.function(self.step, *args, **kw)
      File "/Users/rich/projects/python/lettuce_demo/tests/features/reverse_steps.py", line 18, in then_the_result_is_group1
        assert world.result == group1, 'result does not match expectation'
    AssertionError: result does not match expectation

1 feature (0 passed)
2 scenarios (1 passed)
6 steps (1 failed, 5 passed)
``` 

## Fix the implementation

Our tests ran, but failed because of our implementation of the _reverse(input)_ method. We can make a simple modification of 
that and get all of our tests passing.

Modify the _Reverser_ class's _reverse(input)_ method so that it returns its input.

```python
class Reverser(object):
    def __init__(self):
        pass

    def reverse(self,input):
    	return input
```

## Run again

```bash
lettuce tests
```

Your output should look like this;

```bash
Feature: Reverse Words in a String                    # tests/features/reverse.feature:1
  In order to read backwards                          # tests/features/reverse.feature:2
  readers must have the words in their text reveresed # tests/features/reverse.feature:3

  Scenario: Empty String Reversal                     # tests/features/reverse.feature:5
    Given a String Reverser                           # tests/features/reverse_s    Given a String Reverser                           # tests/features/reverse_steps.py:8
    When I reverse the string ""                      # tests/features/reverse_s    When I reverse the string ""                      # tests/features/reverse_steps.py:12
    Then the result is ""                             # tests/features/reverse_s    Then the result is ""                             # tests/features/reverse_steps.py:16

  Scenario: Single Character Reversal                 # tests/features/reverse.feature:10
    Given a String Reverser                           # tests/features/reverse_s    Given a String Reverser                           # tests/features/reverse_steps.py:8
    When I reverse the string "A"                     # tests/features/reverse_s    When I reverse the string "A"                     # tests/features/reverse_steps.py:12
    Then the result is "A"                            # tests/features/reverse_s    Then the result is "A"                            # tests/features/reverse_steps.py:16

1 feature (1 passed)
2 scenarios (2 passed)
6 steps (6 passed)
```





















# Lazy Route: Just use the repo

After checkout, from the top directory of this project, run;

```bash
lettuce tests
```

You should see output like this (note, on my Mac I can't see the lines output, I presume its my color scheme)

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
