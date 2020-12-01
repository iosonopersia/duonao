#!/usr/bin/python
# -*- coding: utf-8 -*-
import math
import subprocess
import time

import vlc


def play_song(song_name):

    p = vlc.MediaPlayer(song_name)
    p.play()


def do_moves(moves, robot_ip, robot_port):
    for move in moves:
        python2_command = "python2 ./NaoMoves/"+move+".py " + str(robot_ip)+" " + str(robot_port)
        start_move=time.time()
        process = subprocess.run(python2_command.split(), stdout=subprocess.PIPE)
        move_length = time.time()-start_move
        #print(process.stdout) # receive output from the python2 script
        print(move +" "+ str(move_length))


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


def beauty_score(choreography, moves, method="entropy"):
    if method == "entropy":
        return calc_entropy(choreography)
    elif method == "custom":
        return calc_custom(choreography, moves)


def calc_entropy(choreography):
    frequency_dict = {}
    for move in choreography:
        if move not in frequency_dict:
            frequency_dict[move] = 1
        else:
            frequency_dict[move] += 1

    entropy = 0.0
    for unique_move, frequency in frequency_dict.items():
        probability = frequency / len(choreography)
        entropy -= probability * math.log(probability, 2)

    return entropy


def calc_custom(choreography, moves):
    PUNISHMENT = 1
    MAX_RATING = 10

    points = 0
    for index, move in enumerate(choreography):
        if move not in moves:
            continue
        if move in choreography[:index]:
            cur_value = - PUNISHMENT * index/len(choreography)
        else:
            cur_value = moves[move].rating * 2
        points += cur_value

    # Normalize the result inside the [0,1] interval:
    MAX_POINTS = len(choreography) * MAX_RATING
    MIN_POINTS = - len(choreography) * PUNISHMENT
    # points is now inside the [MIN_POINTS, MAX_POINTS] interval...
    points += abs(MIN_POINTS)
    # points is now inside the [0, MAX_POINTS + abs(MIN_POINTS)] interval...
    return points / (abs(MIN_POINTS) + MAX_POINTS)
