def calculate_area(length, width):
    result = length * width
    if result > 100:
        print("Large area!")
    return result


my_length = 10
my_width = 5
area = calculate_area(my_length, my_width)
print(f"The area is: {area}")


"""
FLAKE 8 FIRST PASS:

bad_style.py:1:19: E211 whitespace before '('
bad_style.py:1:21: E201 whitespace after '('
bad_style.py:1:28: E203 whitespace before ','
bad_style.py:1:36: E202 whitespace before ')'
bad_style.py:3:20: E701 multiple statements on one line (colon)
bad_style.py:3:27: E211 whitespace before '('
bad_style.py:3:29: E201 whitespace after '('
bad_style.py:3:43: E202 whitespace before ')'
bad_style.py:6:1: E305 expected 2 blank lines after class or function definition, found 1
bad_style.py:8:22: E211 whitespace before '('
bad_style.py:8:24: E201 whitespace after '('
bad_style.py:8:44: E202 whitespace before ')'
bad_style.py:9:6: E211 whitespace before '('
bad_style.py:9:8: E201 whitespace after '('
bad_style.py:9:31: E202 whitespace before ')'
bad_style.py:9:33: W292 no newline at end of file

FLAKE 8 SECOND PASS:
No style or logical errors

Note: after adding this comment and running flake8,
it outputs:
bad_style.py:25:80: E501 line too long (89 > 79 characters)
running black does not fix the formatting issue
"""
