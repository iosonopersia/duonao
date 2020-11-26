#!/usr/bin/python
# -*- coding: utf-8 -*-
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
        if move_name == state_dict['position']:
            # Avoid repeating the same move twice in a row
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
        return usable_actions

    def result(self, state, action):
        """ Given state and action, return a new state that is the result of the action.
        Action is assumed to be a valid action in the state """
        move = self.available_moves[action]
        state_dict = from_state_to_dict(state)
        return (('position', action),
                ('standing', move.postconditions['standing']),
                ('remaining_time', state_dict['remaining_time'] - move.duration),
                ('moves_done', state_dict['moves_done'] + 1))

    def goal_test(self, state):
        """ Given a state, return True if state is a goal state or False, otherwise """
        state_dict = from_state_to_dict(state)
        goal_dict = from_state_to_dict(self.goal)

        goal_remaining_time = goal_dict['remaining_time']
        a = goal_remaining_time - self.threshold
        b = goal_remaining_time + self.threshold

        # TODO: valutare anche il beauty_score (deve essere maggiore di una certa soglia minima)
        # Il beauty_score deve essere valutato su TUTTA la coreografia realizzata fino ad adesso!!!
        return (a <= state_dict['remaining_time'] <= b) and state_dict['moves_done'] >= goal_dict['moves_done']

    def h(self, node):
        """ Return the heuristic value for a given state. Default heuristic function used is 
        h(n) = number of misplaced tiles """
        every_move_done_until_now = [*self.previous_moves_done]
        for n in node.path():
            state_dict = from_state_to_dict(n.state)
            every_move_done_until_now.append(state_dict['position'])

        # Con questa euristica dobbiamo valutare "l'artisticità" di tutta la coreografia realizzata fino ad adesso,
        # che è contenuta in every_move_done_until_now. Da penalizzare: ripetitività delle mosse. Da incentivare: punteggio totale raggiunto.
        heuristic = 1 - beauty_score(every_move_done_until_now, self.available_moves)
        print(heuristic)
        return heuristic
