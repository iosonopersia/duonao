#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from aima.search import Problem
from utils import from_state_to_dict, beauty_score


class NaoProblem(Problem):

    def __init__(self, initial, goal, moves, threshold, cur_sol):
        """ Define goal state and initialize a problem """
        super().__init__(initial, goal)
        self.available_moves = moves
        self.previous_moves_done = cur_sol
        self.threshold = threshold

    def is_move_applicable(self, state, move_name, move):
        state_dict = from_state_to_dict(state)
        if state_dict['remaining_time'] + self.threshold < move.duration:
            return False
        if 'standing' in move.preconditions and state_dict['standing'] != move.preconditions['standing']:
            # If a 'standing' precondition is set, ensure that it's satisfied
            return False
        if move_name == state_dict['choreography'][-1]:
            # Avoid repeating the same move twice in a row
            return False
        full_choreography = [*self.previous_moves_done, *state_dict['choreography'], move_name]
        if full_choreography.count(move_name) > 4:
            return False
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
        full_choreography = [*state_dict['choreography'], action]
        return (('choreography', (*state_dict['choreography'], action)),
                ('standing', move.postconditions['standing']),
                ('remaining_time', state_dict['remaining_time'] - move.duration),
                ('moves_done', state_dict['moves_done'] + 1),
                ('beauty_score', beauty_score(full_choreography, self.available_moves)))

    def goal_test(self, state):
        """ Given a state, return True if state is a goal state or False, otherwise """
        state_dict = from_state_to_dict(state)
        goal_dict = from_state_to_dict(self.goal)

        goal_remaining_time = goal_dict['remaining_time']
        a = goal_remaining_time - self.threshold
        b = goal_remaining_time + self.threshold

        return (a <= state_dict['remaining_time'] <= b) and state_dict['moves_done'] >= goal_dict['moves_done'] and \
                state_dict['beauty_score'] >= goal_dict['beauty_score']
