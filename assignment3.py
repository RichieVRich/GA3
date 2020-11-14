'''
    This file contains the template for Assignment3.  For testing it, I will place it
    in a different directory, call the function <vidrach_itky_leda>, and check its output.
    So, you can add/remove  whatever you want to/from this file.  But, don't change the name
    of the file or the name/signature of the following function.

    Also, I will use <python3> to run this code.
'''

def vidrach_itky_leda(input_file_path, output_file_path):
    '''
    This function will contain your code, it will read the input from the file
    <input_file_path> and write to the file <output_file_path>.

    Params:
        input_file_path (str): full path of the input file.
        output_file_path (str): full path of the output file.
    '''
    # 2D test array
    test_array = [[1,2,4,3],[3,4,1,2],[3,1,2,3],[2,3,1,2]]
    # Print 2d array
    for r in test_array:
        for c in r:
            print(c, end = " ")
        print()
    n = len(test_array) - 1
    red = test_array[0][0]
    blue = test_array[n][n]
    # Red X and Y
    r_x = 0
    r_y = 0
    # Blue X and Y
    b_x = n
    b_y = n
    # Tokens for valid movement
    move1 = 0
    move2 = 0
    # Bound Checker Tokens
    bounds1 = 0
    bounds2 = 0

    print("red = ", red," blue = ", blue)
    completed = 0
    switch = -1
    print("Red = ", red, " Blue = ", blue)
    print("position red x|y", r_x, " | ", r_y)
    print("position blue x|y", b_x, " | ", b_y)
    while completed < 1:
        if red < blue or switch == 0:
            switch = 1
            print("blue is bigger = ", blue)
            if r_y + blue <= n:
                # Check bottom Y

                move1 = test_array[r_y + blue][r_x]
            else:
                print("failed out of bounds move1")
                move1 = -1
            if r_x + blue <= n:
                # Check Right X
                move2 = test_array[r_y][r_x + blue]
            else:
                print("failed out of bounds move2")
                move2 = 0

            # Check for valid input

            print("by ", b_y , "move1 ", move1)
            print("bx ", b_x, "move2 ",move2)
            bounds1 = b_y - move1
            bounds2 = b_x - move2
            print("by ", bounds1)
            print("bx ", bounds2)
            if bounds1 < 0 :
                print(" b1 false")
                bounds1 = 99
            if bounds2 < 0:
                print(" b2 false")
                bounds2 = 99
            # Smallest Wins in this situtation
            if bounds1 < bounds2 or r_x == n:
                red = move1
                r_y = r_y + blue
            else:
                red = move2
                r_x = r_x + blue
            print("red = ", red)


        elif blue < red or switch == 1:
            switch = 0
            print("red is bigger")
            # Check bottom Y
            move1 = test_array[b_y - red][b_x]
            print(move1)
            # Check Right X
            move2 = test_array[b_y][b_x - red]
            print(move2)
            # Check for valid input

            bounds1 = r_y + move1
            bounds2 = r_x + move2
            print("by ", bounds1)
            print("bx ", bounds2)
            if bounds1 > 4 :
                print(" b1 false")
                bounds1 = -1
            if bounds2 > 4:
                print(" b2 false")
                bounds2 = -1
            # Smallest Wins in this situtation
            if bounds2 > bounds1 or b_x == 0:
                print("move1 wins")
                blue  = move1
                b_y = b_y - red
            else:
                print("move2 wins")
                blue = move2
                b_x = b_x - red
            print(blue)


        else:
            print("there is tie leave it to switch")

        if r_x == n and r_y == n and b_x == 0 and b_y == 0:
            completed = completed + 1
        print("Red = ", red, " Blue = ", blue)
        print("position red x|y", r_x, " | ",r_y)
        print("position blue x|y", b_x, " | ", b_y)
print("test")

pass

vidrach_itky_leda('input0.in', 'input0.out')
