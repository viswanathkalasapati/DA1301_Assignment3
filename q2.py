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
    result=[]
    ships_left=[]
    ships_right=[]
    for i in range(0,len(ships)):
        if ships[i]>0:
            ships_left.append(ships[i])
        else:
            ships_right.append(ships[i])
    
    for i in range(0,len(ships)):
        if abs(ships_left[i])>abs(ships_right[i]):
            result.append(ships_left[i])
        if abs(ships_left[i])<abs(ships_right[i]):
            result.append(ships_right[i])
        else:
            continue

    return result
    


if __name__ == "__main__":
    # Example sanity checks (see test.py for the real test cases)
    print(surviving_ships([6, 3, -5]))  # expected: [6]
    print(surviving_ships([8, -8]))     # expected: []
