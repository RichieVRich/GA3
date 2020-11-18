'''
    This file contains the template for Assignment3.  For testing it, I will place it
    in a different directory, call the function <vidrach_itky_leda>, and check its output.
    So, you can add/remove  whatever you want to/from this file.  But, don't change the name
    of the file or the name/signature of the following function.

    Also, I will use <python3> to run this code.
'''
import math

def vidrach_itky_leda(input_file_path, output_file_path):
    '''
    This function will contain your code, it will read the input from the file
    <input_file_path> and write to the file <output_file_path>.

    Params:
        input_file_path (str): full path of the input file.
        output_file_path (str): full path of the output file.
    '''
    global Array
    global n
    global line
    global count
    global i
    global insert
    global current
    global rows
    global columns
    rows = 0
    columns = 0
    Array = []
    current = []
    global maximum
    maximum = 0
    global x
    count = 0
    n = 0
    fp = open(input_file_path)
    #print('hello')
    line = fp.readline()
    n = int(math.sqrt(int(line)))
    print(line)
    print(n)
    print("n is", n )
    columns, rows = (n, n)
    for x in range(n):
        if x == line:
            break
      #  print(line[0])
        line = fp.readline()
        line = line.rstrip('\n')
        line = line.split(",")

        print(line)
        line = [int(i) for i in line]
        Array.append(line)
    # 2D test array

    # Print 2d array
    for r in Array:
        for c in r:
            print(c, end = " ")
        print()
    n = len(Array) - 1
    red = Array[0][0]
    blue = Array[n][n]
    # Red X and Y
    r_x = 0
    r_y = 0
    # Blue X and Y
    b_x = n
    b_y = n
    # Tokens for valid movement
    move1 = 0
    move2 = 0
    move3 = 0
    move4 = 0
    # Bound Checker Tokens
    bounds1 = 0
    bounds2 = 0
    bounds3 = 0
    bounds4 = 0
    completed = 0
    switch = -1
 #   print("Red = ", red, " Blue = ", blue)
 #   print("position red x|y", r_x, " | ", r_y)
 #   print("position blue x|y", b_x, " | ", b_y)
    if red < blue:
        switch = 0
    else:
        switch = 1
    # Start the code
    compr = 0
    compb = 0
    while completed < 1:
        # Moving Red
        if switch == 0:
            if r_y == n and r_x == n:
                compr = 1
            switch = 1
            fail1 = 0
            fail2 = 0
            fail3 = 0
            fail4 = 0
           # print("blue is bigger = ", blue)
            if r_y + blue <= n:
                # Check bottom Y
                move1 = Array[r_y + blue][r_x]
            else:
            #    print("failed out of bounds move1", r_y + blue)
                fail1 = 1
            if r_x + blue <= n:
                # Check Right X
                move2 = Array[r_y][r_x + blue]
            else:
           #     print("failed out of bounds move2 ", r_x + blue)
                fail2 = 1

            # Check for valid input
           # print("by ", b_y , "move1 ", move1)
           # print("bx ", b_x, "move2 ",move2)
            if compb == 0:
                bounds1 = b_y - move1
                bounds2 = b_x - move2
                bounds3 = b_y + move3
                bounds4 = b_x + move4
                print("by ", bounds1)
                print("bx ", bounds2)
                if bounds1 < 0:

                    bounds1 = 99
                if bounds2 < 0:
                    # print(" b2 false")
                    bounds2 = 99

                # Smallest Wins in this situtation
                if bounds1 < bounds2 or r_x == n:
                    if fail1 == 0:
                        print("didnt fail")
                        red = move1
                        r_y = r_y + blue
                elif fail2 == 0:
                    #   print("didn't fail")
                    red = move2
                    r_x = r_x + blue

                else:
                    #    print("cannot reasonably move switch to the other")
                    switch = 1
            else:
                if r_x == n:
                    r_y = r_y + blue
                else:
                    r_x = r_x + blue
           # print("red = ", red)
        # Moving Blue ===========
        elif switch == 1:
            switch = 0
            fail1 = 0
            fail2 = 0
            fail3 = 0
            fail4 = 0
           # print("red is bigger")
            if b_y - red >= 0:
                # Check bottom Y
                move1 = Array[b_y - red][b_x]
                #print(move1)
            else:
                fail1 = 1
                #print("failed out of bounds move1", b_y - red)
            if b_x - red >= 0:
                # Check Right X
                move2 = Array[b_y][b_x - red]
               # print(move2)
            else:
               # print("failed out of bounds move")
                fail2 = 1
 
            # Check for valid input, only if r isn't completed
            if compr == 0:
                bounds1 = r_y + move1
                bounds2 = r_x + move2
              #  print("by ", bounds1)
              #  print("bx ", bounds2)
                if bounds1 > n:
               #     print(" r1 false")
                    fail1 = 1
                    bounds1 = -1
                if bounds2 > n:
                #    print(" r2 false")
                    fail2 = 1
                    bounds2 = -1
                # Smallest Wins in this situtation
                if bounds2 < bounds1 or b_x == 0:
                   # print("changing bound 1 ")
                    if fail1 == 0:
                    #    print("move1 wins")
                        blue = move1
                        b_y = b_y - red
                elif fail2 == 0:
                   # print("chainging boutn 2")
                   # print("move2 wins")
                    blue = move2
                    b_x = b_x - red
                else:
                  #  print("cannot move token SWITCH!")
                    switch = 0
            else:
                if b_x == 0:
                    b_y = b_y - red
                else:
                    b_x = b_x - red

          #  print(blue)


        else:
         #   print("there is tie leave it to switch")
            if switch < 0:
                switch = 0

        if r_x == n and r_y == n and b_x == 0 and b_y == 0:
            completed = completed + 1
        print("Red = ", red, " Blue = ", blue)
        print("position red x: ", r_x, " | y:",r_y)
        print("position blue x: ", b_x, " | y:", b_y)
#print("test")

pass

vidrach_itky_leda('input0.in', 'input0.out')
