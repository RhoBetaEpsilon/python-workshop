'''Section 5: State Machines'''
'''
Follow the prompts in the match statement to fill in the state machine.
Things that are done repeatedly in a state go in the case statement, while things that are done once go in the if statement that changes the state.
'''
from random import randint
from time import sleep

my_states = ["ADD", "SUBTRACT", "IDLE"]
current_state = my_states[2]
i = 0

while True:
    sensor_reading = randint(-1, 9)
    
    match current_state: # use match instead of switch syntax
        case "ADD":
            ### YOUR CODE HERE ###

            '''
            In the add state, keep adding sensor_reading to i
            If the sensor reads more than 4, switch to SUBTRACT
            If the sensor reads -1, switch to IDLE
            '''

            ### YOUR CODE ENDS ###

        case "SUBTRACT":
            ### YOUR CODE HERE ###

            '''
            In the subtract state, keep subtracting sensor_reading from i
            If the sensor reads less than 4, switch to ADD
            If the sensor reads -1, switch to IDLE
            '''

            ### YOUR CODE ENDS ###
            
        
        case "IDLE":
            ### YOUR CODE HERE ###

            '''
            In the idle state, keep diving i by 2
            If the sensor reads more than 4, switch to SUBTRACT
            If the sensor reads less than 4, switch to ADD
            If the sensor reads -1, switch to IDLE
            '''

            ### YOUR CODE ENDS ###

        case _: #default case
            break
    
    sleep(1)