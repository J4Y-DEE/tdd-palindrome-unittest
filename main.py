def is_palindrome(s):
    cleaned = s.lower()
    return cleaned == cleaned[::-1]