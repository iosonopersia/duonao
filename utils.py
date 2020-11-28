#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess
import vlc


def play_song(song_name):

    p = vlc.MediaPlayer(song_name)
    p.play()


def do_moves(moves, robot_ip, robot_port):
    for move in moves:
        python2_command = "python2 ./NaoMoves/"+move+".py " + str(robot_ip)+" " + str(robot_port)

        process = subprocess.run(python2_command.split(), stdout=subprocess.PIPE)
        print(process.stdout) # receive output from the python2 script


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


def beauty_score(choreography, moves):
    PUNISHMENT = 1
    MAX_RATING = 10

    points = 0
    for index, move in enumerate(choreography):
        if move not in moves:
            continue
        if move in choreography[:index]:
            cur_value = - PUNISHMENT * index/len(choreography)
        else:
            cur_value = moves[move].rating * 5
        points += cur_value

    # Normalize the result inside the [0,1] interval:
    MAX_POINTS = len(choreography) * MAX_RATING
    MIN_POINTS = - len(choreography) * PUNISHMENT
    # points is now inside the [MIN_POINTS, MAX_POINTS] interval...
    points += abs(MIN_POINTS)
    # points is now inside the [0, MAX_POINTS + abs(MIN_POINTS)] interval...
    return points / (abs(MIN_POINTS) + MAX_POINTS)



