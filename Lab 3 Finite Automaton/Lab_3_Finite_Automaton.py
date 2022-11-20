"""
    Lab 3 Statement:
    Write a program that reads the elements of a finite automaton from a file and:
    - Display set of states, alphabet, transitions, set of final states
    - Documentation should also include in BNF or EBNF format the form in which the FA.in file should be written
    - BONUS : Consider the input data corresponding to the lexical tokens of your programming language, verify if
      a given string is a valid lexical token.
"""

if __name__ == '__main__':
    '''
        We will need to classify all the elements of an automaton
        Classes are: initial state (initialState), final states (finalStates), all the states we have (initial, final and intermediary) (states), transitions from one state to
        the other (transitions) and the alphabet (alphabet). They will be represented as lists.
    '''
    initialState = []
    finalStates = []
    states = []
    transitions = []
    alphabet = []
    f = open("automaton.txt", "r")
    automaton = f.read().split("\n") 
    for line in automaton:
        """
            We go line by line through the file where the final automaton is represented (automaton.txt) and start the classification
        """
        splitLine = line.split("->")    # the arrow represents the transition and what is on the left and right sides are the elements
        left = splitLine[0]   # the left side of the transition (this is what will transition)
        right = splitLine[1]  # the right side of the transition (this is the result of the transition)
        """
            The left side of the transition is made out of 2 parts:
            1. The state itself, denoted by qi, with i=0,1,2
            2. The possible values it can take to reach the next state (this will make up the alphabet)
            The states enclosed between {} are the initial states
            The states enclosed between [] are intermediary states
            The states enclosed between () are the final states 
        """

        state = left.split(",")[0][1:]
        alphabetPart = left.split(",")[1][0:-1]
        if alphabetPart not in alphabet:
           # We check if this part of the alphabet is already in the list of pieces of the alphabet. If it isn't, we add it
            alphabet.append(alphabetPart)

        if state not in states:
            # Now we deal with the states
            if state[0] == "{":
                # This is an initial state. We will format it a bit, to get rid of the paranthesis, and then we check if it already is in the
                # initial state list (if not, we add it). Afterwards, we will add it to the list of all states, unless it is already there
                state = state.replace("{", "").replace("}", "") 
                if state not in initialState:
                    initialState.append(state)
            states.append(state)

        if right[0] == "(":
            # This is a final state. We check if it is in the final states list and add it it it is not there
            elem = right.replace("(", "").replace(")", "")
            if elem not in finalStates:
                finalStates.append(elem)
            transitions.append([state, elem])

        if right[0] == "[":
            # This is a state which is neither initial nor final, but we have to add it to the set of states
            elem = right.replace("[", "").replace("]", "")
            if elem not in states:
                states.append(elem)
            transitions.append([state, elem])

    print("Alphabet:\n", alphabet, "\n")
    print("Set of states:\n", states, "\n")
    print("Initial  state:\n", initialState, "\n")
    print("Final states:\n", finalStates, "\n")
    print("Transition:\n", transitions, "\n")
    
