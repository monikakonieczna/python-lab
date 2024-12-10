def check_str(s: str):
# Normalize the string: lowercased and remove non-alphanumeric characters
    normalized = ''.join(char.lower() for char in s if char.isalnum())
    
    # Compare characters from the start and end
    left, right = 0, len(normalized) - 1
    while left < right:
        if normalized[left] != normalized[right]:
            return False
        left += 1
        right -= 1
    
    return True