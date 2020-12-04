#!/usr/bin/python
# -*- coding: utf-8 -*-

from aima.search import *
from nao_problem import NaoProblem
from utils import *


def is_standing(position):
    if position in ('M_Crouch', 'M_Sit', 'M_SitRelax'):
        return False
    return True


class MoveInfo:
    def __init__(self, duration=None, rating=None, preconditions=None, postconditions=None):
        self.duration = duration
        self.rating = rating
        self.preconditions = preconditions if preconditions is not None else {}
        self.postconditions = postconditions if preconditions is not None else {}


def main(robot_ip, port):
    # TODO: win the challenge
    moves = {'0_StandUp':       MoveInfo(8.3,  5, {'standing': False}, {'standing': True}),
             '1_AirGuitar':     MoveInfo(4.7,  8, {'standing': True}, {'standing': True}),
             '2_ArmDance':      MoveInfo(10.3, 10, {'standing': True}, {'standing': True}),
             '3_BlowKisses':    MoveInfo(4.5, 6, {'standing': True}, {'standing': True}),
             '4_ArmsOpening':   MoveInfo(3.8, 10, None, None),
             '5_Bow':           MoveInfo(4.0,   2, {'standing': True}, {'standing': True}),
             '6_DiagonalLeft':  MoveInfo(3.2, 10, {'standing': True}, {'standing': True}),
             '7_DiagonalRight': MoveInfo(2.8, 10, {'standing': True}, {'standing': True}),
             '8_DanceMove':     MoveInfo(6.3,   1, {'standing': True}, {'standing': True}),
             '9_SprinklerL':    MoveInfo(4.3,   5, {'standing': True}, {'standing': True}),
             '10_SprinklerR':   MoveInfo(4.3,   5, {'standing': True}, {'standing': True}),
             '11_Dab':          MoveInfo(3.3,   7, {'standing': True}, {'standing': True}),
             '12_RightArm':     MoveInfo(9.1, 10, None, None),
             '13_TheRobot':     MoveInfo(6.3,  4, {'standing': True}, {'standing': True}),
             '14_ComeOn':       MoveInfo(3.8,  3, {'standing': True}, {'standing': True}),
             '15_StayingAlive': MoveInfo(6.1,  9, {'standing': True}, {'standing': True}),
             '16_Rhythm':       MoveInfo(3.2,  2, {'standing': True}, {'standing': True}),
             '17_PulpFiction':  MoveInfo(5.8,   8, {'standing': True}, {'standing': True})}
    initial_pos = ('M_StandInit', MoveInfo(1.4, postconditions={'standing': True}))
    mandatory_pos = [('M_Sit', MoveInfo(9.3, postconditions={'standing': False})),
                     ('M_SitRelax', MoveInfo(11.3, postconditions={'standing': False})),
                     ('M_WipeForehead', MoveInfo(4.5)),
                     ('M_Stand', MoveInfo(2.3, postconditions={'standing': True})),
                     ('M_Hello', MoveInfo(4.3)),
                     ('M_StandZero', MoveInfo(1.4, postconditions={'standing': True}))]
    final_goal_pos = ('M_Crouch', MoveInfo(1.3, postconditions={'standing': False}))
    # Optional step: shuffle mandatory_states
    # random.shuffle(mandatory_pos)

    pos_list = [initial_pos, *mandatory_pos, final_goal_pos]

    solution = tuple()
    print("PLANNED CHOREOGRAPHY:")
    start = time.time()
    for index in range(1, len(pos_list)):
        starting_pos = pos_list[index-1]
        ending_pos = pos_list[index]
        choreography = (starting_pos[0],)
        standing = is_standing(starting_pos[0])
        remaining_time = 180.0/7 - ending_pos[1].duration
        cur_state = (('choreography', choreography),
                     ('standing', standing),
                     ('remaining_time', remaining_time),
                     ('moves_done', 0),
                     ('beauty_score', 0.0))
        cur_goal_state = (('remaining_time', 0),
                          ('moves_done', 5),
                          ('beauty_score', 2.5 + 0.2*(index-1)))
        cur_problem = NaoProblem(cur_state, cur_goal_state, moves, 1, solution, "entropy")
        cur_solution = iterative_deepening_search(cur_problem)
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
    play_song("Don't stop me now - Queen.mp3")
    start_moves=time.time()
    do_moves(solution, robot_ip, port)
    print(f"Length of the entire choreography: {time.time()-start_moves} seconds.")


if __name__ == "__main__":

    robot_ip = "127.0.0.1"
    port = 39451  # Insert NAO port
    if len(sys.argv) > 2:
        port = int(sys.argv[2])
        robot_ip = sys.argv[1]
    elif len(sys.argv) == 2:
        robot_ip = sys.argv[1]
    
    main(robot_ip, port)
