# @Author     : Himanya Verma
# @Student ID : 169051154
# @Date       : March 4th 2026
# @Course     : CP312 Assignment 3 Question 2 Part B
# @Description: A python solution to find the minimum number of packages to reach an exact target amount.
# Academic Integrity Statement: I certify that this assignment is entirely my own work and that all external resources, if used, have been properly acknowledged.
import sys

def solve():
    # Read the filename from the command line
    if len(sys.argv) < 2:
        print("Please provide the input filename.")
        return 

    filename = sys.argv[1]

    try:
        with open(filename, 'r') as f:
            lines = f.read().splitlines()
        if len(lines) < 2:
            return
        # Parse the package sizes and target amount
        sizes = [int(x.strip()) for x in lines[0].split(',')]
        m = int(lines[1].strip())
    except Exception as e:
        print(f"Error reading file: {e}")
        return 

    # Initalize DP array with infinity 
    dp = [float('inf')] * (m+1)
    dp[0] = 0

    # Array to track which package size was used to reach the weight w
    choice = [-1] * (m + 1)

    # Fill in the DP table
    for w in range(1, m + 1):
        for s in sizes:
            if w >= s and dp[w - s] != float('inf'):
                if dp[w - s] + 1 < dp[w]:
                    dp[w] = dp[w - s] + 1
                    choice[w] = s

    # If the target cannot be reached exactly 
    if dp[m] == float('inf'):
        print("-1")
        print("There's no solution")
        return
    
    # Print the total number of packages
    print(dp[m])

    # Backtrack to count the quantity fo each package size 
    counts = {}
    curr = m
    while curr > 0:
        s = choice[curr]
        counts[s] = counts.get(s, 0) + 1
        curr -=s
    
    # Format the second line of output 
    result_parts = []
    for s in sizes:
        if s in counts:
            count = counts[s]
            plural = "packages" if count > 1 else "package"
            result_parts.append(f"{count} {plural} of size {s}")
    
    print(" and ".join(result_parts))

if __name__ == "__main__":
    solve()