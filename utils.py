#!/usr/bin/python
# -*- coding: utf-8 -*-
import importlib
from playsound import playsound


def play_song(song_name):
    # block=False => the command is run asynchronously
    playsound(song_name, block=False)


def do_moves(moves):
    for move in moves:
        importlib.import_module("." + move, "NaoMoves").main(robotIP, robotPort)


def from_state_to_dict(state):
    """
    Converts a state into a dictionary for easier access to the key-value pairs.
    In case of repeated properties, only the last value is kept!

    :param state: a problem state in the form of tuple of tuples
    :return: a dictionary representation of the given state
    """
    params_dict = dict()
    for t in state:
        len_t = len(t)
        if len_t < 2:
            continue
        key = t[0]
        if len_t > 2:
            value = t[1:]
        else:
            value = t[1]
        if key not in params_dict:
            params_dict[key] = value
    return params_dict


def beauty_score(coreography, moves):
    PUNISHMENT = 2
    MAX_RATING = 10

    points = 0
    for index, move in enumerate(coreography):
        if move not in moves:
            continue
        if move in coreography[:index]:
            points -= PUNISHMENT
        else:
            points += moves[move].rating

    # Normalize the result inside the [0,1] interval:
    MAX_POINTS = len(coreography) * MAX_RATING
    MIN_POINTS = - len(coreography) * PUNISHMENT
    # points is now inside the [MIN_POINTS, MAX_POINTS] interval...
    points += abs(MIN_POINTS)
    # points is now inside the [0, MAX_POINTS + abs(MIN_POINTS)] interval...
    return points / (abs(MIN_POINTS) + MAX_POINTS)
