def solution(park, routes):
    moves = dict({
        "W": [0, -1],
        "E": [0, 1],
        "N": [-1, 0],
        "S": [1, 0]
    })

    park_map = [list(p) for p in park]
    width, height = len(park_map[0]), len(park_map)
    cur = find_start_coord(park_map)

    for route in routes:
        direction, speed = route.split(" ")
        speed = int(speed)

        # check range out
        temp_coord = [cur[0], cur[1]]
        temp_coord = elementwise_add(temp_coord, moves[direction], speed)
        if not (0 <= temp_coord[0] <= height - 1) or not (0 <= temp_coord[1] <= width - 1):
            continue

        # check obstacle
        temp_coord = [cur[0], cur[1]]
        is_obstacle = False
        for i in range(speed):
            temp_coord = elementwise_add(temp_coord, moves[direction])
            is_obstacle = True if park_map[temp_coord[0]][temp_coord[1]] == "X" else False
            if is_obstacle:
                break
                
        if is_obstacle:
            continue
        cur = elementwise_add(cur, moves[direction], speed)
    return cur


def find_start_coord(park_map):
    for i in range(len(park_map)):
        for j in range(len(park_map[i])):
            if park_map[i][j] == "S":
                return [i, j]


def elementwise_add(l1, l2, w=1):
    return [l1[0] + l2[0] * w, l1[1] + l2[1] * w]