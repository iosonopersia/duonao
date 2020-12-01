#!/usr/bin/python
# -*- coding: utf-8 -*-
import time

from aima.search import *
from nao_problem import NaoProblem
from utils import *


def is_standing(position):
    """
    if position in ('Crouch', 'Sit', 'SitRelax'):
        return False
    """
    return True

class MoveInfo:
    def __init__(self, duration=None, rating=None, preconditions=None, postconditions=None):
        self.duration = duration
        self.rating = rating
        self.preconditions = preconditions if preconditions is not None else {}
        self.postconditions = postconditions if preconditions is not None else {}


def main(robot_ip, port):
    # TODO: win the challenge
    moves = {'AirGuitar':    MoveInfo(5.24,  8, {'standing': True}, {'standing': True}),
             'ArmDance':     MoveInfo(11.34, 10, {'standing': True}, {'standing': True}),
             'BlowKisses':   MoveInfo(4.9,   6, {'standing': True}, {'standing': True}),
             'Bow':          MoveInfo(4.6,   2, {'standing': True}, {'standing': True}),
             'DanceMove':    MoveInfo(6.9,   1, {'standing': True}, {'standing': False}),
             'SprinklerL':   MoveInfo(4.1,   5, {'standing': True}, {'standing': True}),
             'SprinklerR':   MoveInfo(4.1,   5, {'standing': True}, {'standing': True}),
             'Dab':          MoveInfo(3.1,   7, {'standing': True}, {'standing': True}),
             'TheRobot':     MoveInfo(6.04,  4, {'standing': True}, {'standing': True}),
             'ComeOn':       MoveInfo(4.61,  3, {'standing': True}, {'standing': True}),
             'StayingAlive': MoveInfo(5.91,  9, {'standing': True}, {'standing': True}),
             'Rhythm':       MoveInfo(4.02,  2, {'standing': True}, {'standing': True}),
             'PulpFiction':  MoveInfo(5.6,   8, {'standing': True}, {'standing': True})}
    initial_pos = ('StandInit', MoveInfo(0, postconditions={'standing': True}))
    final_goal_pos = ('Crouch', MoveInfo(1.05, postconditions={'standing': False}))
    mandatory_pos = [('Sit', MoveInfo(3.12, postconditions={'standing': False})),
                     ('SitRelax', MoveInfo(3.02, postconditions={'standing': False})),
                     ('WipeForehead', MoveInfo(4.1)),
                     ('Stand', MoveInfo(2.02, postconditions={'standing': True})),
                     ('Hello', MoveInfo(4.02)),
                     ('StandZero', MoveInfo(2.02, postconditions={'standing': True}))]
    # Optional step: shuffle mandatory_states
    random.shuffle(mandatory_pos)

    pos_list = [initial_pos, *mandatory_pos, final_goal_pos]

    solution = tuple()
    print("PLANNED CHOREOGRAPHY:")
    start = time.time()
    for index in range(1, len(pos_list)):
        choreography = (pos_list[index-1][0],)
        standing = is_standing(pos_list[index-1])
        remaining_time = 180.0/7 - pos_list[index][1].duration
        cur_state = (('choreography', choreography),
                     ('standing', standing),
                     ('remaining_time', remaining_time),
                     ('moves_done', 0),
                     ('beauty_score', 0.0))
        cur_goal_state = (('remaining_time', 0),
                          ('moves_done', 5),
                          ('beauty_score', 2.5))
        cur_problem = NaoProblem(cur_state, cur_goal_state, moves, 1, solution, "entropy")
        cur_solution = iterative_deepening_search(cur_problem)
        #cur_solution = uniform_cost_search(cur_problem) #it takes too much time
        #cur_solution = depth_first_graph_search(cur_problem)
        #print(str(index)+ "solution found")
        if cur_solution is None:
            raise RuntimeError(f'Step {index} - no solution was found!')

        cur_choreography = from_state_to_dict(cur_solution.state)['choreography']
        print(cur_choreography)
        solution += cur_choreography

    solution += (final_goal_pos[0],)
    print(f"Needed time to plan: {time.time()-start} seconds.")
    state_dict = from_state_to_dict(cur_solution.state)
    print(f"Beauty_score: {state_dict['beauty_score']}")
    print(f"Estimated choreography duration: {180.0 - state_dict['remaining_time']}")
    print("-------------------------------------------------------")
    
    # Dance execution
    play_song('RockNRollRobot.mp3')
    start_moves=time.time()
    do_moves(solution, robot_ip, port)
    print(f"Length of the entire choreography: {time.time()-start_moves} seconds.")


if __name__ == "__main__":

    robot_ip = "127.0.0.1"
    port = 9559 # Insert NAO port
    if len(sys.argv) > 2:
        port = int(sys.argv[2])
        robot_ip = sys.argv[1]
    elif len(sys.argv) == 2:
        robot_ip = sys.argv[1]
    
    main(robot_ip, port)
