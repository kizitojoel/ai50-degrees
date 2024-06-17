from tictactoe import *
b = [[X, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY]]

def min_value(b):
        # If we have a terminal state we return the utility of the state
        if terminal(b):
            return(utility(b))
        # Set v to be a high value first because we will be trying to minimize
        v = 100
        for action in actions(b):
            # Assume that out of all the actions you take, opp will be optimal
            # Then find the path that has the minimum endgoal
            v = min(v, max_value(result(b, action)))
        return v
    
def max_value(b):
    if terminal(b):
        return(utility(b))
    v = -100
    for action in actions(b):
        print(result(b, action))
        v = max(v, min_value(result(b, action)))
    return v

# if player(b) == X:
#     outcomes = []
#     for action in actions(b):
#          outcomes.append((action, min_value(result(b, action))))
#     sorted_outcomes = sorted(outcomes, key=lambda x : x[1])
#     print(sorted_outcomes)
# else:
#     outcomes = []
#     for action in actions(b):
#          outcomes.append((action, max_value(result(b, action))))
#     sorted_outcomes = sorted(outcomes, key=lambda x : x[1])
#     print(sorted_outcomes)

print(actions(b))