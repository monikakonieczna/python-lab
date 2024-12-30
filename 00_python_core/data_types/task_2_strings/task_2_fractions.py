def get_fractions(a_b: str, c_b: str) -> str:
    # Split the fractions into numerators and denominators
    a_num, a_den = map(int, a_b.split('/'))
    c_num, c_den = map(int, c_b.split('/'))
    
    # Since denominators are the same, add the numerators
    sum_numerator = a_num + c_num
    
    # Return the sum expression
    return f"{a_b} + {c_b} = {sum_numerator}/{a_den}"