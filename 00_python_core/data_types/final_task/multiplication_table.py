from typing import List

def check(row_start:int, row_end:int, column_start:int, column_end:int) -> List[List[int]]:
    # Create the multiplication table as a list of lists
    table = [[i * j for j in range(column_start, column_end + 1)] for i in range(row_start, row_end + 1)]
    
    # Print the column headers
    print("\t".join(str(j) for j in range(column_start, column_end + 1)))
    
    # Print the rows of the table
    for row in table:
        print("\t".join(str(x) for x in row))
    
    return table  # Return the table as a list of lists