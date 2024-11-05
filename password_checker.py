Python 3.12.7 (tags/v3.12.7:0b05ead, Oct  1 2024, 03:06:41) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>  import re
  File "<stdin>", line 1
    import re
IndentationError: unexpected indent
>>>
>>> def rate_password(password):
...     score = 1  # Start with the lowest score
...
>>>     # Check 1: Length
>>>     if len(password) >= 12:
  File "<stdin>", line 1
    if len(password) >= 12:
IndentationError: unexpected indent
>>>         score += 2
  File "<stdin>", line 1
    score += 2
IndentationError: unexpected indent
>>>     elif len(password) >= 8:
  File "<stdin>", line 1
    elif len(password) >= 8:
IndentationError: unexpected indent
>>>         score += 1
  File "<stdin>", line 1
    score += 1
IndentationError: unexpected indent
>>>
>>>     # Check 2: Character Diversity
>>>     has_lower = bool(re.search(r'[a-z]', password))
  File "<stdin>", line 1
    has_lower = bool(re.search(r'[a-z]', password))
IndentationError: unexpected indent
>>>     has_upper = bool(re.search(r'[A-Z]', password))
  File "<stdin>", line 1
    has_upper = bool(re.search(r'[A-Z]', password))
IndentationError: unexpected indent
>>>     has_digit = bool(re.search(r'\d', password))
  File "<stdin>", line 1
    has_digit = bool(re.search(r'\d', password))
IndentationError: unexpected indent
>>>     has_special = bool(re.search(r'[!@#$%^&*()_+{}:;<>,.?/~`]', password))
  File "<stdin>", line 1
    has_special = bool(re.search(r'[!@#$%^&*()_+{}:;<>,.?/~`]', password))
IndentationError: unexpected indent
>>>
>>>     diversity_count = sum([has_lower, has_upper, has_digit, has_special])
  File "<stdin>", line 1
    diversity_count = sum([has_lower, has_upper, has_digit, has_special])
IndentationError: unexpected indent
>>>     if diversity_count >= 3:
  File "<stdin>", line 1
    if diversity_count >= 3:
IndentationError: unexpected indent
>>>         score += 2
  File "<stdin>", line 1
    score += 2
IndentationError: unexpected indent
>>>     elif diversity_count == 2:
  File "<stdin>", line 1
    elif diversity_count == 2:
IndentationError: unexpected indent
>>>         score += 1
  File "<stdin>", line 1
    score += 1
IndentationError: unexpected indent
>>>
>>>     # Check 3: Complexity (no common words, sequences, or repeats)
>>>     common_patterns = [
  File "<stdin>", line 1
    common_patterns = [
IndentationError: unexpected indent
>>>         'password', '1234', 'abcd', 'qwerty', 'admin', 'letmein'
  File "<stdin>", line 1
    'password', '1234', 'abcd', 'qwerty', 'admin', 'letmein'
IndentationError: unexpected indent
>>>     ]
  File "<stdin>", line 1
    ]
IndentationError: unexpected indent
>>>     if any(pattern in password.lower() for pattern in common_patterns):
  File "<stdin>", line 1
    if any(pattern in password.lower() for pattern in common_patterns):
IndentationError: unexpected indent
>>>         score -= 1  # Penalize if password contains common patterns
  File "<stdin>", line 1
    score -= 1  # Penalize if password contains common patterns
IndentationError: unexpected indent
>>>
>>>     # Check 4: Unpredictability (no consecutive or repeating sequences)
>>>     if re.search(r'(.)\1{2,}', password):  # Penalize for repeating characters
  File "<stdin>", line 1
    if re.search(r'(.)\1{2,}', password):  # Penalize for repeating characters
IndentationError: unexpected indent
>>>         score -= 1
  File "<stdin>", line 1
    score -= 1
IndentationError: unexpected indent
>>>     if re.search(r'(012|123|234|345|456|567|678|789|890)', password):  # Penalize for sequences
  File "<stdin>", line 1
    if re.search(r'(012|123|234|345|456|567|678|789|890)', password):  # Penalize for sequences
IndentationError: unexpected indent
>>>         score -= 1
  File "<stdin>", line 1
    score -= 1
IndentationError: unexpected indent
>>>
>>>     # Normalize score between 1 and 5
>>>     if score < 1:
  File "<stdin>", line 1
    if score < 1:
IndentationError: unexpected indent
>>>         score = 1
  File "<stdin>", line 1
    score = 1
IndentationError: unexpected indent
>>>     elif score > 5:
  File "<stdin>", line 1
    elif score > 5:
IndentationError: unexpected indent
>>>         score = 5
  File "<stdin>", line 1
    score = 5
IndentationError: unexpected indent
>>>
>>>     # Return password level
>>>     return score
  File "<stdin>", line 1
    return score
IndentationError: unexpected indent
>>>
>>> # Example Usage
>>> password = input("Enter your password: ")
Enter your password: level = rate_password(password)
>>>
>>> levels = {
...     1: "Under adequate",
...     2: "Reaching adequate",
...     3: "Adequate",
...     4: "Above adequate",
...     5: "Passing adequate"
... }
>>>
>>> print(f"Password Level: {level} - {levels[level]}")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'level' is not defined. Did you mean: 'levels'?
>>>
>>> cd Desktop
  File "<stdin>", line 1
    cd Desktop
       ^^^^^^^
SyntaxError: invalid syntax
>>> python password_checker.py
  File "<stdin>", line 1
    python password_checker.py
           ^^^^^^^^^^^^^^^^
SyntaxError: invalid syntax
>>>
