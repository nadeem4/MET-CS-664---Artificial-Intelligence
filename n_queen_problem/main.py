def is_valid(placements, cur_placement):
    for placement in placements[:-1]:
        placement_x, placement_y = placement
        cur_placement_x, cur_placement_y = cur_placement

        if cur_placement_x == placement_x or cur_placement_y == placement_y or abs(
                cur_placement_x - placement_x) == abs(cur_placement_y - placement_y):
            return False
    return True


def solve_n_queen(n, placements, cur_col):
    if cur_col >= n or len(placements) == n:
        return True

    for i in range(0, n):
        placements.append((i, cur_col))
        if is_valid(placements, (i, cur_col)) and solve_n_queen(n, placements, cur_col + 1):
            return True
        placements.pop()
    return False


if __name__ == '__main__':
    eight_queen_placements = []

    if solve_n_queen(8, eight_queen_placements, 0):
        print(eight_queen_placements)
    else:
        print("Placement is not possible")

    fifty_queen_placements = []

    if solve_n_queen(30, fifty_queen_placements, 0):
        print(fifty_queen_placements)
    else:
        print("Placement is not possible")
