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

### Run your feature

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

### Run again

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

### Run again

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

### Run again

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

### Run again

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

### Run again

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

### Run again

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

### Run again

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

### Run again

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
we will modify the steps we already have defined. 

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

### Run again

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

### Run again

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

## Adding more _scenarios_

So far our String Reverser class is coming along well. It can reverse empty strings and single characters. Let's add
another feature to see if we can reverse a whole world.

Add the following feature to your _reverse.feature_ file;

```gherkin
  Scenario: Multicharacter Word Reversal
    Given a String Reverser
    When I reverse the string "Bacon"
    Then the result is "Bacon"
```

### Run again

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

  Scenario: Multicharacter Word Reversal              # tests/features/reverse.feature:15
    Given a String Reverser                           # tests/features/reverse_s    Given a String Reverser                           # tests/features/reverse_steps.py:9
    When I reverse the string "Bacon"                 # tests/features/reverse_s    When I reverse the string "Bacon"                 # tests/features/reverse_steps.py:13
    Then the result is "Bacon"                        # tests/features/reverse_s    Then the result is "Bacon"                        # tests/features/reverse_steps.py:17

1 feature (1 passed)
3 scenarios (3 passed)
9 steps (9 passed)
```

Great! That already works. Lets add a _scenario_ for a multi-word string.

Modify your _reverse.feature_ file by adding this scenario;

```gherkin
  Scenario: Multiword String Reversal
    Given a String Reverser
    When I reverse the string "Bacon is the life blood of Agile Software Development"
    Then the result is "Development Software Agile of blood life the is Bacon"
```

### Run again

```bash
lettuce tests
```

Your output should look like this;

```bash
Feature: Reverse Words in a String                                                    # tests/features/reverse.feature:1
  In order to read backwards                                                          # tests/features/reverse.feature:2
  readers must have the words in their text reveresed                                 # tests/features/reverse.feature:3

  Scenario: Empty String Reversal                                                     # tests/features/reverse.feature:5
    Given a String Reverser                                                         Given a String Reverser                                                           # tests/features/reverse_steps.py:9
    When I reverse the string ""                                                    When I reverse the string ""                                                      # tests/features/reverse_steps.py:13
    Then the result is ""                                                           Then the result is ""                                                             # tests/features/reverse_steps.py:17

  Scenario: Single Character Reversal                                                 # tests/features/reverse.feature:10
    Given a String Reverser                                                         Given a String Reverser                                                           # tests/features/reverse_steps.py:9
    When I reverse the string "A"                                                   When I reverse the string "A"                                                     # tests/features/reverse_steps.py:13
    Then the result is "A"                                                          Then the result is "A"                                                            # tests/features/reverse_steps.py:17

  Scenario: Multicharacter Word Reversal                                              # tests/features/reverse.feature:15
    Given a String Reverser                                                         Given a String Reverser                                                           # tests/features/reverse_steps.py:9
    When I reverse the string "Bacon"                                               When I reverse the string "Bacon"                                                 # tests/features/reverse_steps.py:13
    Then the result is "Bacon"                                                      Then the result is "Bacon"                                                        # tests/features/reverse_steps.py:17

  Scenario: Multiword String Reversal                                                 # tests/features/reverse.feature:20
    Given a String Reverser                                                         Given a String Reverser                                                           # tests/features/reverse_steps.py:9
    When I reverse the string "Bacon is the life blood of Agile Software Develop    When I reverse the string "Bacon is the life blood of Agile Software Development" # tests/features/reverse_steps.py:13
    Then the result is "Development Software Agile of blood life the is Bacon"      Then the result is "Development Software Agile of blood life the is Bacon"        # tests/features/reverse_steps.py:17
    Traceback (most recent call last):
      File "/Library/Python/2.7/site-packages/lettuce/core.py", line 141, in __call__
        ret = self.function(self.step, *args, **kw)
      File "/Users/rich/projects/python/lettuce_demo/tests/features/reverse_steps.py", line 18, in then_the_result_is_group1
        assert world.result == group1, 'result does not match expectation'
    AssertionError: result does not match expectation

1 feature (0 passed)
4 scenarios (3 passed)
12 steps (1 failed, 11 passed)
```

## Fixing the implementation

Our test failed. We need to actually reverse the words in the string in order to get this to pass. Fortunately this is a
very easy thing to do (in Python anyway).

Modify your _string_reverser.py_ file to look like this;

```python
# -*- coding: utf-8 -*-

import string

class Reverser(object):
    def __init__(self):
        pass

    def reverse(self,input):
        words = string.split(input)
        words.reverse()
        return string.join(words, " ")
```

### Run again

```bash
lettuce tests
```

Your output should look like this;

```bash
Feature: Reverse Words in a String                                                    # tests/features/reverse.feature:1
  In order to read backwards                                                          # tests/features/reverse.feature:2
  readers must have the words in their text reveresed                                 # tests/features/reverse.feature:3

  Scenario: Empty String Reversal                                                     # tests/features/reverse.feature:5
    Given a String Reverser                                                         Given a String Reverser                                                           # tests/features/reverse_steps.py:9
    When I reverse the string ""                                                    When I reverse the string ""                                                      # tests/features/reverse_steps.py:13
    Then the result is ""                                                           Then the result is ""                                                             # tests/features/reverse_steps.py:17

  Scenario: Single Character Reversal                                                 # tests/features/reverse.feature:10
    Given a String Reverser                                                         Given a String Reverser                                                           # tests/features/reverse_steps.py:9
    When I reverse the string "A"                                                   When I reverse the string "A"                                                     # tests/features/reverse_steps.py:13
    Then the result is "A"                                                          Then the result is "A"                                                            # tests/features/reverse_steps.py:17

  Scenario: Multicharacter Word Reversal                                              # tests/features/reverse.feature:15
    Given a String Reverser                                                         Given a String Reverser                                                           # tests/features/reverse_steps.py:9
    When I reverse the string "Bacon"                                               When I reverse the string "Bacon"                                                 # tests/features/reverse_steps.py:13
    Then the result is "Bacon"                                                      Then the result is "Bacon"                                                        # tests/features/reverse_steps.py:17

  Scenario: Multiword String Reversal                                                 # tests/features/reverse.feature:20
    Given a String Reverser                                                         Given a String Reverser                                                           # tests/features/reverse_steps.py:9
    When I reverse the string "Bacon is the life blood of Agile Software Develop    When I reverse the string "Bacon is the life blood of Agile Software Development" # tests/features/reverse_steps.py:13
    Then the result is "Development Software Agile of blood life the is Bacon"      Then the result is "Development Software Agile of blood life the is Bacon"        # tests/features/reverse_steps.py:17

1 feature (1 passed)
4 scenarios (4 passed)
12 steps (12 passed)
```

Awesome! It passes. 

## Sanity Checking

Lets add another _scenario_ to our _feature_ to confirm that things are really working well.

Add the following _scenario_ to the _reverse.feature_ file;

```gherkin
  Scenario: Palindrome String Reversal
    Given a String Reverser
    When I reverse the string "Rats Live on no Evil Star"
    Then the result is "Star Evil no on Live Rats"
```

### Run again

```bash
lettuce tests
```

Your output should look like this;

```bash
Feature: Reverse Words in a String                                                    # tests/features/reverse.feature:1
  In order to read backwards                                                          # tests/features/reverse.feature:2
  readers must have the words in their text reveresed                                 # tests/features/reverse.feature:3

  Scenario: Empty String Reversal                                                     # tests/features/reverse.feature:5
    Given a String Reverser                                                         Given a String Reverser                                                           # tests/features/reverse_steps.py:9
    When I reverse the string ""                                                    When I reverse the string ""                                                      # tests/features/reverse_steps.py:13
    Then the result is ""                                                           Then the result is ""                                                             # tests/features/reverse_steps.py:17

  Scenario: Single Character Reversal                                                 # tests/features/reverse.feature:10
    Given a String Reverser                                                         Given a String Reverser                                                           # tests/features/reverse_steps.py:9
    When I reverse the string "A"                                                   When I reverse the string "A"                                                     # tests/features/reverse_steps.py:13
    Then the result is "A"                                                          Then the result is "A"                                                            # tests/features/reverse_steps.py:17

  Scenario: Multicharacter Word Reversal                                              # tests/features/reverse.feature:15
    Given a String Reverser                                                         Given a String Reverser                                                           # tests/features/reverse_steps.py:9
    When I reverse the string "Bacon"                                               When I reverse the string "Bacon"                                                 # tests/features/reverse_steps.py:13
    Then the result is "Bacon"                                                      Then the result is "Bacon"                                                        # tests/features/reverse_steps.py:17

  Scenario: Multiword String Reversal                                                 # tests/features/reverse.feature:20
    Given a String Reverser                                                         Given a String Reverser                                                           # tests/features/reverse_steps.py:9
    When I reverse the string "Bacon is the life blood of Agile Software Develop    When I reverse the string "Bacon is the life blood of Agile Software Development" # tests/features/reverse_steps.py:13
    Then the result is "Development Software Agile of blood life the is Bacon"      Then the result is "Development Software Agile of blood life the is Bacon"        # tests/features/reverse_steps.py:17

  Scenario: Palindrome String Reversal                                                # tests/features/reverse.feature:25
    Given a String Reverser                                                         Given a String Reverser                                                           # tests/features/reverse_steps.py:9
    When I reverse the string "Rats Live on no Evil Star"                           When I reverse the string "Rats Live on no Evil Star"                             # tests/features/reverse_steps.py:13
    Then the result is "Star Evil no on Live Rats"                                  Then the result is "Star Evil no on Live Rats"                                    # tests/features/reverse_steps.py:17

1 feature (1 passed)
5 scenarios (5 passed)
15 steps (15 passed)
```

Still more awesome! This one passes too.

## Exploring other _scenario_ types

### Scenarios with tables in-line

Lettuce supports using inline tables to help you minimize the amount of _feature_ definition required for complicated 
test cases. The following example shows placing a table in the _When_ and again the _Then_ to pass lists of arguments
into the _step_. 

Using this approach we can reproduce all of our test cases in one _scenario_.

Add the folowing _scenario_ to the _feature_ file.

```gherkin
  Scenario: Consolidated Table Example
    Given a String Reverser
    When I reverse these strings:
      | input                                                          |
      |                                                                |
      | A                                                              |
      | Bacon                                                          |
      | Bacon is the life blood of Agile Software Development          |
      | Rats Live on no Evil Star                                      |
    Then the results are:
      | output                                                         |
      |                                                                |
      | A                                                              |
      | Bacon                                                          |
      | Development Software Agile of blood life the is Bacon          |
      | Star Evil no on Live Rats                                      |
```

>
> Note: You don't have to line up the vertical bars, I just like the way it looks
>

You may run the lettuce command now if you like, but it will fail because there are no _steps_ that can handle
these tables. 

Add these two steps to your _reverse_steps.py_ file.

```python
@step('I reverse these strings:')
def when_i_reverse_these_strings(step):
    outputs = list()
    for input in step.hashes:
        outputs.append(world.reverser.reverse(input['input']))
    outputs.reverse()             # must reverse the list so it will match order in the Then step
    world.outputs = outputs

@step('the results are:')
def then_the_results_are(step):
    for expected in step.hashes:
        assert world.outputs.pop() == expected['output'], 'result does not match expectation'
```

Because we passed these table arguments lettuce put the table in _world.hashes_. This is done automatically
by lettuce. _world.hashes_ is a _list_ of _dictionary_ objects. So you can see in the _steps_ that we iterate
accross that list using the Python _for_ loop and access the dictionary items by the column name (input['input']).

Of course you can have multiple columns of data as necessary. The first line of the table will become the _keys_ 
in the _dictionary_ object; each colum is the _key_. Each row becomes an entry in the _list_, in the order defined
in the _scenario_.

### Scenario Outlines

_Scenario_Outlines_ are another mechanism for consolidating our _scenarios_. They use a simple replacement mechanism
and a table in order to run your _steps_. The outline contains masks that match the column headings in the associated
table. In our example below, <a string> matches the first column, who's header is _a_string_.

As the table is read the _Scenario_Outline_ is populated by each row in the table and then executed. 

Add the following _Scenario_Outline_ to your _features_ file.

```gherkin
  Scenario Outline: Outline Example
    Given a String Reverser
    When I reverse the string "<a string>"
    Then the result is "<reversed string>"

  Examples:
    | a string                                              | reversed string                                       |
    |                                                       |                                                       |
    | A                                                     | A                                                     |
    | bacon                                                 | bacon                                                 |
    | Bacon is the life blood of Agile Software Development | Development Software Agile of blood life the is Bacon |
    | Rats Live on no Evil Star                             | Star Evil no on Live Rats                             |
```

No new steps are needed for our _Scenario_Outline_. Very intentionally, each of the _steps_ in the _scenario_outline_ 
are identical to the _steps_ defined previously for other _scenarios_.

## Terrain

Lettuce supports Event Hooks and Shared Methods through what it calls _terrain_. Lettuce will load and execute the code 
found in the _terrain.py_ file in your _features_ subdirectory whenever you run the _lettuce_ command.

### Event Hooks

Lettuce provides event hooks that you can use for setup/teardown activities, logging, or whatever is appropriate to your 
tests. I'd recommend you carefully consider their usage. 

For demonstration purposes, create this _terrain.py_ file in your _features_ folder.

```python
# -*- coding: utf-8 -*-

import os
from lettuce import *

def isDebug():
    rval = False
    try:
        if (os.environ['DEBUG']):
            rval = True
    except KeyError:
        pass
    return rval

def report(message):
    if (isDebug()):
        print message

@before.all
def before_all():
    report("About to do all")
    
@after.all
def after_all(all):
    report("Have done all %s" % (all))
    
@before.each_feature
def before_each_feature(feature):
    report("About to do a feature %s" % (feature))

@after.each_feature
def after_each_feature(feature):
    report("Have done a feature %s" % (feature))

@before.each_scenario
def before_each_scenario(scenario):
    report("About to do a scenario %s" % (scenario))

@after.each_scenario
def after_each_scenario(scenario):
    report("Have done a scenario %s" % (scenario))

@before.each_step
def before_each_step(step):
    report("About to do a step %s\n" % (step))
    
@after.each_step
def after_each_step(step):
    report("\nHave done a step %s" % (step))
```

If you go back an run the tests with the environment variable _DEBUG_ defined you will see output surrounding the more
familiar output.

>
> Note: I didn't test the value of _DEBUG_. I simply check for its existence. 
>

### Run (special)

```bash
DEBUG=Yes lettuce tests
``` 

Your output should look like this;

```bash
About to do all

Feature: Reverse Words in a String                                                                                     # tests/features/reverse.feature:1
  In order to read backwards                                                                                           # tests/features/reverse.feature:2
  readers must have the words in their text reveresed                                                                  # tests/features/reverse.feature:3
About to do a feature <Feature: "Reverse Words in a String">

  Scenario: Empty String Reversal                                                                                      # tests/features/reverse.feature:5
About to do a scenario <Scenario: "Empty String Reversal">
    Given a String Reverser                                                                                            # tests/features/reverse_steps.py:9
About to do a step <Step: "Given a String Reverser">
    Given a String Reverser                                                                                            # tests/features/reverse_steps.py:9

Have done a step <Step: "Given a String Reverser">
    When I reverse the string ""                                                                                       # tests/features/reverse_steps.py:13
About to do a step <Step: "When I reverse the string """>
    When I reverse the string ""                                                                                       # tests/features/reverse_steps.py:13

Have done a step <Step: "When I reverse the string """>
    Then the result is ""                                                                                              # tests/features/reverse_steps.py:17
About to do a step <Step: "Then the result is """>
    Then the result is ""                                                                                              # tests/features/reverse_steps.py:17

Have done a step <Step: "Then the result is """>
Have done a scenario <Scenario: "Empty String Reversal">

  Scenario: Single Character Reversal                                                                                  # tests/features/reverse.feature:10
About to do a scenario <Scenario: "Single Character Reversal">
    Given a String Reverser                                                                                            # tests/features/reverse_steps.py:9
About to do a step <Step: "Given a String Reverser">
    Given a String Reverser                                                                                            # tests/features/reverse_steps.py:9

Have done a step <Step: "Given a String Reverser">
    When I reverse the string "A"                                                                                      # tests/features/reverse_steps.py:13
About to do a step <Step: "When I reverse the string "A"">
    When I reverse the string "A"                                                                                      # tests/features/reverse_steps.py:13

Have done a step <Step: "When I reverse the string "A"">
    Then the result is "A"                                                                                             # tests/features/reverse_steps.py:17
About to do a step <Step: "Then the result is "A"">
    Then the result is "A"                                                                                             # tests/features/reverse_steps.py:17

Have done a step <Step: "Then the result is "A"">
Have done a scenario <Scenario: "Single Character Reversal">

  Scenario: Multicharacter Word Reversal                                                                               # tests/features/reverse.feature:15
About to do a scenario <Scenario: "Multicharacter Word Reversal">
    Given a String Reverser                                                                                            # tests/features/reverse_steps.py:9
About to do a step <Step: "Given a String Reverser">
    Given a String Reverser                                                                                            # tests/features/reverse_steps.py:9

Have done a step <Step: "Given a String Reverser">
    When I reverse the string "Bacon"                                                                                  # tests/features/reverse_steps.py:13
About to do a step <Step: "When I reverse the string "Bacon"">
    When I reverse the string "Bacon"                                                                                  # tests/features/reverse_steps.py:13

Have done a step <Step: "When I reverse the string "Bacon"">
    Then the result is "Bacon"                                                                                         # tests/features/reverse_steps.py:17
About to do a step <Step: "Then the result is "Bacon"">
    Then the result is "Bacon"                                                                                         # tests/features/reverse_steps.py:17

Have done a step <Step: "Then the result is "Bacon"">
Have done a scenario <Scenario: "Multicharacter Word Reversal">

  Scenario: Multiword String Reversal                                                                                  # tests/features/reverse.feature:20
About to do a scenario <Scenario: "Multiword String Reversal">
    Given a String Reverser                                                                                            # tests/features/reverse_steps.py:9
About to do a step <Step: "Given a String Reverser">
    Given a String Reverser                                                                                            # tests/features/reverse_steps.py:9

Have done a step <Step: "Given a String Reverser">
    When I reverse the string "Bacon is the life blood of Agile Software Development"                                  # tests/features/reverse_steps.py:13
About to do a step <Step: "When I reverse the string "Bacon is the life blood of Agile Software Development"">
    When I reverse the string "Bacon is the life blood of Agile Software Development"                                  # tests/features/reverse_steps.py:13

Have done a step <Step: "When I reverse the string "Bacon is the life blood of Agile Software Development"">
    Then the result is "Development Software Agile of blood life the is Bacon"                                         # tests/features/reverse_steps.py:17
About to do a step <Step: "Then the result is "Development Software Agile of blood life the is Bacon"">
    Then the result is "Development Software Agile of blood life the is Bacon"                                         # tests/features/reverse_steps.py:17

Have done a step <Step: "Then the result is "Development Software Agile of blood life the is Bacon"">
Have done a scenario <Scenario: "Multiword String Reversal">

  Scenario: Palindrome String Reversal                                                                                 # tests/features/reverse.feature:25
About to do a scenario <Scenario: "Palindrome String Reversal">
    Given a String Reverser                                                                                            # tests/features/reverse_steps.py:9
About to do a step <Step: "Given a String Reverser">
    Given a String Reverser                                                                                            # tests/features/reverse_steps.py:9

Have done a step <Step: "Given a String Reverser">
    When I reverse the string "Rats Live on no Evil Star"                                                              # tests/features/reverse_steps.py:13
About to do a step <Step: "When I reverse the string "Rats Live on no Evil Star"">
    When I reverse the string "Rats Live on no Evil Star"                                                              # tests/features/reverse_steps.py:13

Have done a step <Step: "When I reverse the string "Rats Live on no Evil Star"">
    Then the result is "Star Evil no on Live Rats"                                                                     # tests/features/reverse_steps.py:17
About to do a step <Step: "Then the result is "Star Evil no on Live Rats"">
    Then the result is "Star Evil no on Live Rats"                                                                     # tests/features/reverse_steps.py:17

Have done a step <Step: "Then the result is "Star Evil no on Live Rats"">
Have done a scenario <Scenario: "Palindrome String Reversal">

  Scenario: Consolidated Table Example                                                                                 # tests/features/reverse.feature:30
About to do a scenario <Scenario: "Consolidated Table Example">
    Given a String Reverser                                                                                            # tests/features/reverse_steps.py:9
About to do a step <Step: "Given a String Reverser">
    Given a String Reverser                                                                                            # tests/features/reverse_steps.py:9

Have done a step <Step: "Given a String Reverser">
    When I reverse these strings:                                                                                      # tests/features/reverse_steps.py:21
      | input                                                 |
    When I reverse these strings:                                                                                      # tests/features/reverse_steps.py:21
      | input                                                 |
      |                                                       |
      | A                                                     |
      | Bacon                                                 |
      | Bacon is the life blood of Agile Software Development |
      | Rats Live on no Evil Star                             |

Have done a step <Step: "When I reverse these strings:">
    Then the results are:                                                                                              # tests/features/reverse_steps.py:29
      | output                                                |
    Then the results are:                                                                                              # tests/features/reverse_steps.py:29
      | output                                                |
      |                                                       |
      | A                                                     |
      | Bacon                                                 |
      | Development Software Agile of blood life the is Bacon |
      | Star Evil no on Live Rats                             |

Have done a step <Step: "Then the results are:">
Have done a scenario <Scenario: "Consolidated Table Example">

  Scenario Outline: Outline Example                                                                                    # tests/features/reverse.feature:47
About to do a scenario <Scenario: "Outline Example">
    Given a String Reverser                                                                                            # tests/features/reverse_steps.py:9
About to do a step <Step: "Given a String Reverser">


Have done a step <Step: "Given a String Reverser">
    When I reverse the string "<a string>"                                                                             # tests/features/reverse_steps.py:13
About to do a step <Step: "When I reverse the string """>


Have done a step <Step: "When I reverse the string """>
    Then the result is "<reversed string>"                                                                             # tests/features/reverse_steps.py:17
About to do a step <Step: "Then the result is """>


Have done a step <Step: "Then the result is """>

  Examples:
    | a string                                              | reversed string                                       |
    |                                                       |                                                       |
    | A                                                     | A                                                     |
    | bacon                                                 | bacon                                                 |
    | Bacon is the life blood of Agile Software Development | Development Software Agile of blood life the is Bacon |
    | Rats Live on no Evil Star                             | Star Evil no on Live Rats                             |
Have done a scenario <Scenario: "Outline Example">
Have done a feature <Feature: "Reverse Words in a String">

1 feature (1 passed)
11 scenarios (11 passed)
33 steps (33 passed)
Have done all <lettuce.core.TotalResult object at 0x1051fe950>
```

### World methods

#### absorb

Lettuce also supports the idea of sharing global methods. The admit this is not _The_Python_Way_ [See|http://lettuce.it/reference/terrain.html#world-absorb]

I've put a contrived method in place just to show how this works. Modify your _terrain.py_ file by adding this code;

```python
@world.absorb
def assert_equal(string1, string2):
    assert string1 == string2, "\n'%s'\nis not equal to\n'%s'" % (string1, string2)
```

Then modify your _reverse_steps.py_ file by replacing each assertion with our new method

Replace
```python
assert world.result == group1, 'result does not match expectation'
```

With this;
```python
world.assert_equal(world.result, group1)
```

You can also replace
```python
assert world.outputs.pop() == expected['output'], 'result does not match expectation'
```

With this;
```python
world.assert_equal(world.outputs.pop(), expected['output'])
```

Now run again. You won't see any actual differences in the output. But, we now have a consolidated assertion method in 
which we can customize the output or do some other 'shared' thing. This can be useful for any number of reasons. I will
leave that speculation as an exercise for the reader.

#### spew

In order to remove a method from the _world_ object, use the _spew_ method. 

>
> Still working on a demo of this that works.
>

---------------------------------------
---------------------------------------

# Variations on Feature Writing

## Avoid Magic Numbers

From the perspective of enhancing understanding we don't really want to
write tests that contain magic numbers unless they really have meaning.
As a contrived example I've added a _feature_ for a Flying Tractor in
which the _scenario_ is defined using words like 'minimum forward speed' and 'minimum safe altitude'. 

This example is of course totally contrived. 

```gherkin
Feature: Flying Tractor Altitude Management
         As a Tractor Operator
         I want Altitude Management
         So I can operate my Flying Tractor safely

         Scenario: Velocity Affects Altitude
                   Given a Flying Tractor
                   When I operate at the minimum forward speed
                   Then the Flying Tractor will rise to the minimum safe altitude
```

The steps file.

```python
# -*- coding: utf-8 -*-

import sys
from lettuce import step, world
from flying.equipment import FlyingTractor

@step(u'Given a Flying Tractor')
def given_a_flying_tractor(step):
    world.flying_tractor = FlyingTractor()

@step(u'When I operate at the minimum forward speed')
def when_i_operate_at_the_minimum_forward_speed(step):
    world.flying_tractor.setSpeed(FlyingTractor.MIN_SAFE_SPEED)

@step(u'Then the Flying Tractor will rise to the minimum safe altitude')
def then_the_flying_tractor_will_rise_to_the_minimum_safe_distance(step):
    assert world.flying_tractor.getAltitude() == FlyingTractor.MIN_SAFE_ALTITUDE, "your tractor is operating dangerously"
```

The code under test

```python
# -*- encoding utf-8 -*-

class FlyingTractor(object):

    MIN_SAFE_SPEED = 5
    MIN_SAFE_ALTITUDE = 6

    def __init__(self):
        pass

    def setSpeed(self,speed):
        pass

    def getAltitude(self):
        return self.MIN_SAFE_ALTITUDE
```

---------------------------------------
---------------------------------------

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
 
# Setting Up Jenkins-CI to Run Lettuce

I'm a huge fan of Jenkins for CI. I thought it would be helpful to show how I setup Jenkins to run my new Lettuce tests. 

## Setup/Configuration

### Install Jenkins-CI
First things first, we need Jenkins. Please visit the Jenkins website to download Jenkins and learn how to start it. 

Jenkins-CI http://jenkins-ci.org/
>
> For reference I'm using Tomcat 7 to run Jenkins as a war file, but it can be run standalone.
>

### Add plugins to Jenkins CI

Visit the manage Jenkins tab and add the following plugins

Jenkins GIT plugin   https://wiki.jenkins-ci.org/display/JENKINS/Git+Plugin
xUnit plugin	     http://wiki.jenkins-ci.org/display/JENKINS/xUnit+Plugin

### Create a new Job in Jenkins

1. Click on 'New Job'
1. Name the job 'My Lettuce Project'
1. Select 'Build a free-style software project'
1. Click 'OK'

### Configure you build job

1. Under Source Code Management, select 'Git'
1.1. Enter the repository url file:///Users/rich/projects/python/lettuce_demo

> Note: That's the file location on my machine, substitute the correct path to your project

1.1. Leave the Branch Specifier set to * *

> You might change this to a branch name if you don't want to build from master

1. Under Build Triggers select 'Poll SCM' and enter the mask _*/5_*_*_*_*_. This sets up a build every 5 minutes based on changes to the repo (meaning if you committed code in the past 5 minutes it will build, if not, nothing happens)
1. In the 'Build' section, select 'Add build Step' and pick 'Execute Shell' from that list.
1.1. In the 'Command' text area enter the following command;

```bash
lettuce --with-xunit --xunit-file=lettucetests.xml tests
```

1. Under 'Post Build Actions' Add 'Publish xUnit test results report'
1.1. Select 'Add' and pick 'Junit' from the dropdown.
1.1. In the 'Junit pattern' text box enter _lettucetests.xml_ this is the same name we used as the argumnt for --xunit-file above (it is also the default value, as long as they match you will be OK)
1. Hit 'Save'

### Test the execution of you job

Go back to your project directory and type this;

```bash
echo " " >> tests/features/flying_tractor.feature
```

Then commit this to your git-repo with;

```bash
git commit -a -m 'trigger build'
```

### Wait for Jenkins to Run

In five minutes or less Jenkins should run your job. You will see a Test report (with a graph) for your lettuce tests. 

>
> For the impatient, you can just click on the 'Build Now' link of your job
>

