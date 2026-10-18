from typing import List


def surviving_ships(ships: List[int]) -> List[int]:
    """
    Problem 2: Spaceship collisions.

    Given `1`a list of ship engine powers (sign = direction: positive is
    right, negative is left), resolve all collisions between ships
    moving toward each other and return the engine powers (with sign)
    of the ships that remain.

    Args:
        ships: list of signed engine powers.

    Returns:
        List of signed engine powers of surviving ships, left to right.
    """
    result = []
    ships_left = []
    ships_right = []
    for i in range(o,len(ships)):
        if ships[i] > 0:
            ships_right.append(ships[i])
        else:
            ships_left.append(ships[i])
    if len(ships_left) > len(ships_right) :
        for i in range(0,len(ships_left)):
            for j in range(0,len(ships_left)):
                if abs(ships_left[i]) > abs(ships_right[j]) :
                    ships_right.pop(j)
                if abs(ships_left[i]) < abs(ships_right[j]) :
                    ships_left.pop(i)
                else :
                    ships_right.pop(j)
                    ships_left.pop(i)
        
    else :
        for i in range(0,len(ships_right)):
            for j in range(0,len(ships_right)):
                if abs(ships_left[i]) > abs(ships_right[j]) :
                    ships_right.pop(j)
                if abs(ships_left[i]) < abs(ships_right[j]) :
                    ships_left.pop(i)
                else :
                    ships_right.pop(j)
                    ships_left.pop(i)
    
    if len(ships_left) > len(ships_right) :
        for i in range(0,len(ships_left)):
            result.append(ships_left[i])
            result.append(ships_right[i])
        else :
            for i in range(0,len(ships_right)):
                result.append(ships_left[i])
                result.append(ships_right[i])
    
    return result
            
    


if __name__ == "__main__":
    # Example sanity checks (see test.py for the real test cases)
    print(surviving_ships([6, 3, -5]))  # expected: [6]
    print(surviving_ships([8, -8]))     # expected: []
