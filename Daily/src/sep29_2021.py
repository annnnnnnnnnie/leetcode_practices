# https://leetcode-cn.com/problems/super-washing-machines/

from typing import List

from enum import Enum, unique


@unique
class Move(Enum):
    LEFT = -1
    STAY = 0
    RIGHT = 1
    BOTH = 9
    UNDECIDED = 99


def is_done(machines, avg):
    return all(map(lambda n: n == avg, machines))


def is_connected(machines):
    return all(map(lambda n: n > 0, machines))


def apply_moves(current_machines, moves):
    assert len(current_machines) == len(moves)
    for i in range(len(current_machines)):
        if moves[i] is Move.STAY:
            pass
        elif moves[i] is Move.LEFT:
            current_machines[i] -= 1
            current_machines[i - 1] += 1
        elif moves[i] is Move.RIGHT:
            current_machines[i] -= 1
            current_machines[i + 1] += 1
        else:
            raise Exception("Invalid move encountered")
    return


def find_min_moves(machines):
    n_machines = len(machines)
    if n_machines == 1:
        return 0
    n_laundries = sum(machines)
    if n_laundries % n_machines != 0:
        return -1
    avg = n_laundries // n_machines
    # return max(map(lambda n: abs(n - avg), machines))
    current_machines = machines
    step_count = 0
    while not is_connected(current_machines):
        moves = find_best_moves(machines, avg)
        apply_moves(current_machines, moves)
        step_count += 1
    return step_count + max(map(lambda n: abs(n - avg), machines))


# pre: len(machines) >= 1
def get_move_left_moves(machines, avg):
    # The left-most would not move left
    moves = [Move.STAY]

    for i in range(1, len(machines)):
        if moves[i - 1] is Move.STAY:
            left_machine_after_move = machines[i - 1]
        elif moves[i - 1] is Move.LEFT:
            left_machine_after_move = machines[i - 1] - 1
        else:
            raise Exception("Impossible entry in moves list")

        # if machines[i-1] after move is < avg, and machines[i] is >= avg, then machine[i] will move left
        if left_machine_after_move < avg and machines[i] >= avg:
            moves.append(Move.LEFT)
        else:
            moves.append(Move.STAY)

    return moves


def get_move_right_moves(machines, avg):
    # The right-most would not move right
    moves = [Move.UNDECIDED] * (len(machines) - 1) + [Move.STAY]

    for i in range(len(machines) - 2, -1, -1):
        if moves[i + 1] is Move.STAY:
            right_machine_after_move = machines[i + 1]
        elif moves[i + 1] is Move.RIGHT:
            right_machine_after_move = machines[i + 1] - 1
        else:
            raise Exception("Impossible entry in moves list")

        # if machines[i+1] after move is < avg, and machines[i] is >= avg, then machine[i] will move right
        if right_machine_after_move < avg and machines[i] >= avg:
            moves[i] = Move.RIGHT
        else:
            moves[i] = Move.STAY

    return moves


def combine_move(mv_left, mv_right):
    if mv_left == Move.STAY:
        return mv_right
    if mv_right == Move.STAY:
        return mv_left
    if mv_left == Move.LEFT and mv_right == Move.RIGHT:
        return Move.BOTH
    raise Exception("Should not reach here")


def find_best_moves(machines, avg):
    # scanning from left to right to see if a machine should move left
    # then from the right to the left to see if a machine should move right:
    move_left_moves = get_move_left_moves(machines, avg)
    move_right_moves = get_move_right_moves(machines, avg)

    moves_draft = []
    assert len(move_left_moves) == len(move_left_moves)
    for i in range(len(move_right_moves)):
        moves_draft.append(combine_move(move_left_moves[i], move_right_moves[i]))

    for i in range(len(moves_draft)):
        if moves_draft[i] == Move.BOTH:
            # resolve conflicts if a machine wants to move both to the left and to the right
            # if one of the direction is <= avg - 2, then just pick that direction. Default to left
            if (i - 1) in range(len(moves_draft)) and machines[i - 1] <= avg - 2:
                moves_draft[i] = Move.LEFT
                continue
            elif (i + 1) in range(len(moves_draft)) and machines[i + 1] <= avg - 2:
                moves_draft[i] = Move.RIGHT
                continue
            # if both directions are >= avg - 1
            elif (i - 1) in range(len(moves_draft)) and (
                    ((i - 2) not in range(len(moves_draft)) or moves_draft[i - 2] != Move.RIGHT)):
                # then first consider the direction that is not receiving from others
                moves_draft[i] = Move.LEFT
                continue
            elif (i + 1) in range(len(moves_draft)) and (
                    ((i + 2) not in range(len(moves_draft)) or moves_draft[i + 2] != Move.LEFT)):
                moves_draft[i] = Move.RIGHT
                continue
            else:
                # if still cannot decide, then pick the side that needs more help
                left_need = sum(map(lambda n: n - avg, machines[:i]))
                right_need = sum(map(lambda n: n - avg, machines[i + 1:]))
                if left_need >= right_need:
                    moves_draft[i] = Move.LEFT
                else:
                    moves_draft[i] = Move.RIGHT
    return moves_draft


class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        return find_min_moves(machines)
