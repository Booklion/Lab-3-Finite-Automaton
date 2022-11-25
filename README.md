# Lab 3 Finite Automaton - Documentation

_Statement:_ Write a program that reads the elements of a finite automaton from a file and:

* Display set of states, alphabet, transitions, set of final states
* Documentation should also include in BNF or EBNF format the form in which the FA.in file should be written

BONUS : Consider the input data corresponding to the lexical tokens of your programming language, verify if a given string is a valid lexical token.

### How to write the FiniteAutomaton.in file: ###

The .in file contains the transitions of the finite automaton. Here are some rules on how to write it:

* < file > ::= < transition >
* < transition > ::= (< statement >, < alphabet >)->< statement >
* < statement > ::= < initialStatement > | < finalStatement > | < basicStatement >
* < initialStatement > ::= {q< digit >}
* < digit > ::= "0" | "1" | ... | "9"
* < finalStatement > ::= (q< digit >)
* < basicStatement > ::= [q< digit >]
* < alphabet > ::= "a" | "b" | ... | "z" | "A" | "B" | ... | "Z" | "_"
