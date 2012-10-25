# String Reverser in Python using Lettuce to Test Drive

I made this project as part of my learning process for both Python
and the lettuce testing framework. Aside from suffering some painful
lessons about how Python import works, a stellar success. 

I will be adding to the project over the next few days to experiment
with the range of features available in lettuce.

## Usage

You will need a valid/working Python environment with the lettuce
test framework installed. (links to be added)

After checkout, from the top directory of this project, run;

```bash
lettuce tests
```

You should see output like this (note, on my Mac I can't see the lines output, presume its my color scheme)

```bash
Feature: Reverse Words in a String                                                    # tests/features/reverse.feature:1
  In order to read backwards                                                          # tests/features/reverse.feature:2
  readers must have the words in their text reveresed                                 # tests/features/reverse.feature:3

  Scenario: Empty String Reversal                                                     # tests/features/reverse.feature:5
    Given a String Reverser                                                         Given a String Reverser                                                           # tests/features/reverse_steps.py:8
    When I reverse the string ""                                                    When I reverse the string ""                                                      # tests/features/reverse_steps.py:12
    Then the result is ""                                                           Then the result is ""                                                             # tests/features/reverse_steps.py:16

  Scenario: Single Character Reversal                                                 # tests/features/reverse.feature:10
    Given a String Reverser                                                         Given a String Reverser                                                           # tests/features/reverse_steps.py:8
    When I reverse the string "A"                                                   When I reverse the string "A"                                                     # tests/features/reverse_steps.py:12
    Then the result is "A"                                                          Then the result is "A"                                                            # tests/features/reverse_steps.py:16

  Scenario: Multicharacter Word Reversal                                              # tests/features/reverse.feature:15
    Given a String Reverser                                                         Given a String Reverser                                                           # tests/features/reverse_steps.py:8
    When I reverse the string "Bacon"                                               When I reverse the string "Bacon"                                                 # tests/features/reverse_steps.py:12
    Then the result is "Bacon"                                                      Then the result is "Bacon"                                                        # tests/features/reverse_steps.py:16

  Scenario: Multiword String Reversal                                                 # tests/features/reverse.feature:20
    Given a String Reverser                                                         Given a String Reverser                                                           # tests/features/reverse_steps.py:8
    When I reverse the string "Bacon is the life blood of Agile Software Develop    When I reverse the string "Bacon is the life blood of Agile Software Development" # tests/features/reverse_steps.py:12
    Then the result is "Development Software Agile of blood life the is Bacon"      Then the result is "Development Software Agile of blood life the is Bacon"        # tests/features/reverse_steps.py:16

  Scenario: Palindrome String Reversal                                                # tests/features/reverse.feature:25
    Given a String Reverser                                                         Given a String Reverser                                                           # tests/features/reverse_steps.py:8
    When I reverse the string "Rats Live on no Evil Star"                           When I reverse the string "Rats Live on no Evil Star"                             # tests/features/reverse_steps.py:12
    Then the result is "Star Evil no on Live Rats"                                  Then the result is "Star Evil no on Live Rats"                                    # tests/features/reverse_steps.py:16

1 feature (1 passed)
5 scenarios (5 passed)
15 steps (15 passed)
```
