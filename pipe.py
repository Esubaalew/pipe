from collections import deque

def parse_input_file(file_path):
    """
    Reads and parses the input file to extract the grid layout, source, and sinks.

    Args:
        file_path (str): The path to the input file.

    Returns:
        tuple: A tuple containing the grid dictionary, source coordinates, and sinks dictionary.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    grid = {}
    source = None
    sinks = {}
    
    for line in lines:
        char, x, y = line.split()
        x, y = int(x), int(y)
        if char == '*':
            source = (x, y)
        else:
            grid[(x, y)] = char
            if char.isalpha():
                sinks[char] = (x, y)
    
    return grid, source, sinks

def bfs_connected_sinks(grid, source):
    """
    Performs a BFS on the grid to find all connected sinks from the source.

    Args:
        grid (dict): The grid dictionary with coordinates as keys and characters as values.
        source (tuple): The coordinates of the source (x, y).

    Returns:
        set: A set of connected sink characters.
    """
    queue = deque([source])
    visited = set([source])
    connected_sinks = set()
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if (nx, ny) in grid and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny))
                if grid[(nx, ny)].isalpha():
                    connected_sinks.add(grid[(nx, ny)])
    
    return connected_sinks

def get_connected_sinks(file_path):
    """
    Main function to read the input file and find all connected sinks from the source.

    Args:
        file_path (str): The path to the input file.

    Returns:
        str: A sorted string of connected sink characters.
    """
    grid, source, sinks = parse_input_file(file_path)
    connected_sinks = bfs_connected_sinks(grid, source)
    return ''.join(sorted(connected_sinks))

# Example usage:
result = get_connected_sinks('input.txt')
print(result)
