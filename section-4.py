'''Section 4: Priority Queue'''
'''
A factory has many chores that need to be done on a regular basis.
The factory needs a priority queue to organize their chores so that the most important tasks get done first.
How important a task is is based on how many days have passed since it was last done and whether it's inspected by regulators.
Longer tasks are considered to be more important than shorter tasks, and inspected tasks are way more important than non-inspected tasks.
Tasks that were done a while ago are more important than tasks done recently.
'''
from heapq import heappush

def weight(hoursRequired, daySinceLast, inspected):
    ### YOUR CODE HERE ###

    '''
    Add calculations for the weight of a task based on the given parameters
    Note that heapq is a min heap, so smaller weights (aka "more" negative) are higher priority
    '''
    
    ### YOUR CODE ENDS ###

if __name__ == '__main__':
    # Tasks as a dictionary of task: [# hours required, # days since last done, inspected?]
    tasks = {
        "Polish Floor": [1, 2, False],
        "Oil Machines": [5, 7, True],
        "Complete Training": [8, 30, True],
        "Calibrate Tools": [5, 60, True],
        "Organize Drawers": [8, 14, False],
        "Refill Liquid Nitrogen": [1, 7, False]
    }

    ordered_tasks = []

    for task in tasks:
        hoursRequired = tasks[task][0]
        daysSinceLast = tasks[task][1]
        inspected = tasks[task][2]

        '''Add the task to the heap with heappush'''

    print(ordered_tasks)