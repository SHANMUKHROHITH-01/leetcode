class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        # Initialize the triangle with the first row
        triangle = [[1]]
        
        for i in range(1, numRows):
            # Start each row with 1
            row = [1]
            # Get the previous row to calculate current values
            prev_row = triangle[i - 1]
            
            # Each middle element is the sum of the two elements above it
            for j in range(1, i):
                row.append(prev_row[j - 1] + prev_row[j])
            
            # End each row with 1
            row.append(1)
            triangle.append(row)
            
        return triangle