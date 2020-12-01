#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from aima.search import Problem
from utils import from_state_to_dict, beauty_score


class NaoProblem(Problem):

    def __init__(self, initial, goal, moves, threshold, cur_sol, evaluation_function):
        """ Define goal state and initialize a problem """
        super().__init__(initial, goal)
        self.available_moves = moves
        self.previous_moves_done = cur_sol
        self.time_threshold = threshold
        self.evaluation_function = evaluation_function

    def is_move_applicable(self, state, move_name, move):
        state_dict = from_state_to_dict(state)
        if state_dict['remaining_time'] < move.duration:
            return False
        if 'standing' in move.preconditions and state_dict['standing'] != move.preconditions['standing']:
            # If a 'standing' precondition is set, ensure that it's satisfied
            return False
        """
        full_choreography = [*self.previous_moves_done, *state_dict['choreography'], move_name]
        if full_choreography[-3:].count(move_name) > 1:
            return False
        """
        return True

    def actions(self, state):
        """ Return the actions that can be executed in the given state.
        The result would be a list, since there are only four possible actions
        in any given state of the environment """
        usable_actions = []
        for move_name, move in self.available_moves.items():
            if self.is_move_applicable(state, move_name, move):
                usable_actions.append(move_name)
        random.shuffle(usable_actions)
        return usable_actions

    def result(self, state, action):
        """ Given state and action, return a new state that is the result of the action.
        Action is assumed to be a valid action in the state """
        move = self.available_moves[action]
        state_dict = from_state_to_dict(state)
        full_choreography = [*self.previous_moves_done, *state_dict['choreography'], action]
        return (('choreography', (*state_dict['choreography'], action)),
                ('standing', move.postconditions['standing']),
                ('remaining_time', state_dict['remaining_time'] - move.duration),
                ('moves_done', state_dict['moves_done'] + 1),
                ('beauty_score', beauty_score(full_choreography, self.available_moves, method=self.evaluation_function)))

    def goal_test(self, state):
        """ Given a state, return True if state is a goal state or False, otherwise """
        state_dict = from_state_to_dict(state)
        goal_dict = from_state_to_dict(self.goal)

        goal_remaining_time = goal_dict['remaining_time']
        a = goal_remaining_time
        b = goal_remaining_time + self.time_threshold

        return (a <= state_dict['remaining_time'] <= b) and state_dict['moves_done'] >= goal_dict['moves_done'] and \
                state_dict['beauty_score'] >= goal_dict['beauty_score']

    def path_cost(self, c, state1, action, state2):
        """Return the cost of a solution path that arrives at state2 from
           state1 via action, assuming cost c to get up to state1. If the problem
           is such that the path doesn't matter, this function will only look at
           state2. If the path does matter, it will consider c and maybe state1
           and action. The default method costs 1 for every step in the path."""
        '''
        #come costo aggiungo anche l'inverso del beauty score
        a = 1
        state1_dict = from_state_to_dict(state1)
        state2_dict = from_state_to_dict(state2)
        beauty_score_difference = state2_dict['beauty_score']-state1_dict['beauty_score']
        alfa_beauty_score_difference = a * (-beauty_score_difference)
        #print (alfa_beauty_score_difference)
        '''
        action_duration = 0
        for move_name, move in self.available_moves.items():
            if move_name == action:
                action_duration = move.duration
        #print(action_duration)
        #print(str(c))
        return c + action_duration  # + alfa_beauty_score_difference
