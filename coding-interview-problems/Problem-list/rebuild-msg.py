
"""
Problem statement:
Given a list of message parts where each part starts with a character and the
next part starts with the last non-space character of the previous part, rebuild
the full message by chaining parts starting from the part that begins with 'A'
until the message ends with 'Z'.

Time complexity: O(n + L), where n is the number of parts and L is the total
length of the final message (each part is appended once).
Space complexity: O(n + L) for the lookup map and the rebuilt message.
"""

def rebuild_message(parts):
    # Create a mapping of {starting_char: full_part_string}
    # This allows O(1) lookup for the next piece of the puzzle
    parts_map = {part[0]: part for part in parts}

    print(parts_map)
    
    # The message always starts with 'A'
    current_char = 'A'
    current_part = parts_map[current_char]
    
    # Initialize our message with the first part
    message = current_part
    
    # Keep appending parts until the message ends with 'Z'
    while not message.rstrip().endswith('Z'):
        # The next part starts with the character our current message ends with

        next_char = message.rstrip()[-1]
        next_part = parts_map[next_char]

        if next_part is None:
            raise ValueError("Incomplete message parts; cannot find next part starting with '{}'".format(next_char))    
        
        # Append the next part, but skip the first character (the overlap)
        # Using slicing [1:] to get everything but the first character
        message += next_part[1:]
        
    return message

# Example usage:
parts = [
    "A quick brown fox ",
    "x jumps over the lazy dog ",
    "g and runs away to the zoo Z "
]

full_message = rebuild_message(parts)
print(full_message)  # Output: "A quick brown fox jumps over the lazy dog and runs away to the zoo Z"
