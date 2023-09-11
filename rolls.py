import random
import re

def roll_dice(dice_expression: str, verbose: bool = False) -> int:
    """
    Simulate a dice roll based on Dungeons & Dragons notation.
    
    Parameters:
    - dice_expression (str): A string with dice rolls and modifiers, e.g. "2d6 + 1d8 - 3".
    - verbose (bool): If True, returns a detailed string showing individual dice rolls.
    
    Returns:
    - int or str: The total of the dice rolled or a detailed string (if verbose=True)
    """

    # Regular expression to parse dice expressions
    pattern = re.compile(r'(\d*d\d+|[+-]?\d+)')
    
    matches = pattern.findall(dice_expression)
    
    total = 0
    details = []

    for match in matches:
        # Handle flat modifiers (e.g., "+5" or "-3")
        if match.isdigit() or (match.startswith('-') and match[1:].isdigit()) or (match.startswith('+') and match[1:].isdigit()):
            total += int(match)
            details.append(match)
            continue
        
        # Handle dice rolls
        parts = match.split('d')
        count = int(parts[0]) if parts[0] else 1
        faces = int(parts[1])
        
        rolls = [random.randint(1, faces) for _ in range(count)]
        total += sum(rolls)
        details.append(f"{match}({'+'.join(map(str, rolls))}={sum(rolls)})")

    if verbose:
        return f"{dice_expression} => {' + '.join(details)} = {total}"
    else:
        return total

# Test cases
print(roll_dice("d6", verbose=True))
print(roll_dice("3d8 + 5 - 2d4", verbose=True))
print(roll_dice("2d20 + 7 - 1", verbose=True))
print(roll_dice("1d20"))
