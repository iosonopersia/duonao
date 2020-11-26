#!/usr/bin/python
# -*- coding: utf-8 -*-
from aima.search import *
from nao_problem import NaoProblem
from utils import from_state_to_dict

robotIP = '127.0.0.1'
robotPort = 9559


def is_standing(position):
    if position in ('Crouch', 'Sit', 'SitRelax'):
        return False
    return True

class MoveInfo:
    def __init__(self, duration=None, rating=None, preconditions=None, postconditions=None):
        self.duration = duration
        self.rating = rating
        self.preconditions = preconditions
        self.postconditions = postconditions


if __name__ == '__main__':
    # TODO: win the challenge
    moves = {'AirGuitar':    MoveInfo(5.24,  8, {'standing': True}, {'standing': True}),
             'ArmDance':     MoveInfo(11.34, 3, {'standing': True}, {'standing': False}),
             'BlowKisses':   MoveInfo(4.9,   6, {'standing': True}, {'standing': True}),
             'Bow':          MoveInfo(4.6,   2, {'standing': True}, {'standing': False}),
             'DanceMove':    MoveInfo(6.9,   1, {'standing': True}, {'standing': True}),
             'SprinklerL':   MoveInfo(4.1,   5, {'standing': False}, {'standing': False}),
             'SprinklerR':   MoveInfo(4.1,   5, {'standing': True}, {'standing': True}),
             'Dab':          MoveInfo(3.1,   7, {'standing': True}, {'standing': True}),
             'TheRobot':     MoveInfo(6.04,  4, {'standing': False}, {'standing': True}),
             'ComeOn':       MoveInfo(4.61,  3, {'standing': True}, {'standing': True}),
             'StayingAlive': MoveInfo(5.91,  9, {'standing': True}, {'standing': False}),
             'Rhythm':       MoveInfo(3.96,  2, {'standing': True}, {'standing': True}),
             'PulpFiction':  MoveInfo(5.6,   8, {'standing': False}, {'standing': False})}
    initial_pos = 'StandInit'
    final_goal_pos = 'Crouch'
    mandatory_pos = ['Sit',
                     'SitRelax',
                     'WipeForehead',
                     'Stand',
                     'Hello',
                     'StandZero']
    # Optional step: shuffle mandatory_states
    # random.shuffle(mandatory_states)

    pos_list = [initial_pos, *mandatory_pos, final_goal_pos]
    print(pos_list)

    solution = [initial_pos]
    for index in range(1, len(pos_list)):
        cur_state = (('position', pos_list[index-1]),
                     ('standing', is_standing(pos_list[index-1])),
                     ('remaining_time', 180/7.0),
                     ('moves_done', 0))
        cur_goal_state = (('remaining_time', 0),
                          ('moves_done', 5))
        cur_problem = NaoProblem(cur_state, cur_goal_state, moves, 1, solution)
        cur_solution = iterative_deepening_search(cur_problem)
        if cur_solution is None:
            raise RuntimeError(f'Step {index} - no solution was found!')
        for i, n in enumerate(cur_solution.path()):
            if i > 0:
                solution.append(from_state_to_dict(n.state)['position'])
        solution.append(pos_list[index])

    print(solution)
    # play_song('RockNRollRobot.mp3')
    # do_moves(solution)
