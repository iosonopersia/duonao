#!/usr/bin/python
# -*- coding: utf-8 -*-
import time

from aima.search import *
from nao_problem import NaoProblem
from utils import *

robotIP = '127.0.0.1'
robotPort = 9559


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
        self.preconditions = preconditions
        self.postconditions = postconditions


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
    initial_pos = ('StandInit', MoveInfo(0))
    final_goal_pos = ('Crouch', MoveInfo(1.05))
    mandatory_pos = [('Sit', MoveInfo(3.12)),
                     ('SitRelax', MoveInfo(3.02)),
                     ('WipeForehead', MoveInfo(4.1)),
                     ('Stand', MoveInfo(2.02)),
                     ('Hello', MoveInfo(4.02)),
                     ('StandZero', MoveInfo(2.02))]
    # Optional step: shuffle mandatory_states
    random.shuffle(mandatory_pos)

    pos_list = [initial_pos, *mandatory_pos, final_goal_pos]
    # print(pos_list)

    solution = tuple()
    start = time.time()
    for index in range(1, len(pos_list)):
        cur_state = (('choreography', (pos_list[index-1][0],)),
                     ('standing', is_standing(pos_list[index-1])),
                     ('remaining_time', 180/7.0 - pos_list[index][1].duration),
                     ('moves_done', 0),
                     ('beauty_score', 0.0))
        cur_goal_state = (('remaining_time', 0),
                          ('moves_done', 5),
                          ('beauty_score', 0.3))
        cur_problem = NaoProblem(cur_state, cur_goal_state, moves, 1, solution)
        cur_solution = iterative_deepening_search(cur_problem)
        if cur_solution is None:
            raise RuntimeError(f'Step {index} - no solution was found!')

        cur_choreography = from_state_to_dict(cur_solution.state)['choreography']
        print(cur_choreography)
        solution += cur_choreography

    solution += (final_goal_pos[0],)
    print("Needed time to plan: " + str(time.time()-start))
    state_dict = from_state_to_dict(cur_solution.state)
    # print(state_dict['beauty_score']*100)
    # print(solution)
    play_song('RockNRollRobot.mp3')
    start_moves=time.time()
    do_moves(solution, robot_ip, port)
    print("Length of the entire choreography: " + str(time.time()-start_moves))


if __name__ == "__main__":

    robot_ip = "127.0.0.1"
    port = 9559 # Insert NAO port
    if len(sys.argv) <= 1:
        print("robotIP default: 127.0.0.1")
    elif len(sys.argv) <= 2:
        robot_ip = sys.argv[1]
    else:
        port = int(sys.argv[2])
        robot_ip = sys.argv[1]

    main(robot_ip, port)
