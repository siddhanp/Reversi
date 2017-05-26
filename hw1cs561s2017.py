import copy

def main():

    global consta
    global mylist
    global xturn

    mylist = []
    board = []

    infile = open("input.txt","r")


    turn = infile.readline()
    turn = list(turn)[0]
    #print turn

    #consta = infile.readline()
    consta = int(list(infile.readline())[0])
    #print consta

    board = infile.readlines()
    for s in range(0,8):
        board[s]=list(board[s])

    #for s in range(0,8):
        #print board[s]


    infile.close()

    tempboard = copy.deepcopy(board)

    consta = int(consta)
    depth = 0
    #print turn
    xturn = turn
    result = alphabeta(tempboard, turn, depth)

def alphabeta(tempboard, turn, depth):

    infinity = float("inf")
    ninfinity = float("-inf")
    positionx = "root"
    positiony = "root"
    v = maxvalue(tempboard, positionx, positiony, ninfinity, infinity, turn, depth, False)
    return v

def maxvalue(tempboard, positionx, positiony, alpha, beta, turn, depth, gameover):

    if depth == 0:
        bestboard = copy. deepcopy(tempboard)

    #print ("MAX VALUE", depth)
    #print (positionx, positiony, turn)
    #print turn, "Hi", gameover
    if turn == 'X':
        opponent = 'O'
    else:
        opponent = 'X'

    v = float("-inf")
    #print("1")
    if positionx == "root" and positiony == "root":
        #print("root", depth, v, alpha, beta)
        outputqueue("root", depth, v, alpha, beta)
    elif positionx == "pass" and positiony == "pass":
        #print("pass", depth, v, alpha, beta)
        outputqueue("pass", depth, v, alpha, beta)
    elif depth!= consta:
        #print(converttosquare(positionx, positiony), depth, v, alpha, beta)
        outputqueue(converttosquare(positionx, positiony), depth, v, alpha, beta)


    if gameover == True and positionx == "pass" and positiony =="pass" and depth + 1 == consta:
        #print "gameover"
        #print("pass",depth+1, evaluationfunction(tempboard, xturn), alpha, beta)
        outputqueue("pass",depth+1, evaluationfunction(tempboard, xturn), alpha, beta)
        #print("pass", depth, evaluationfunction(tempboard, xturn), max(alpha, evaluationfunction(tempboard, xturn)), beta)
        outputqueue("pass", depth, evaluationfunction(tempboard, xturn), max(alpha, evaluationfunction(tempboard, xturn)), beta)
        return evaluationfunction(tempboard, xturn)

    if gameover == True and positionx == "pass" and positiony =="pass":
        #print "gameover"
        #print("pass",depth+1, evaluationfunction(tempboard, xturn), alpha, beta)
        outputqueue("pass",depth+1, evaluationfunction(tempboard, xturn), alpha, beta)
        #print("pass", depth, evaluationfunction(tempboard, xturn), alpha, min(beta,evaluationfunction(tempboard, xturn)))
        outputqueue("pass", depth, evaluationfunction(tempboard, xturn), alpha, min(beta,evaluationfunction(tempboard, xturn)))
        return evaluationfunction(tempboard, xturn)


    #print opponent
    avm = allvalidmoves(tempboard, turn)

    #print avm
    #print len(avm)

    if depth == consta:

        #print "idepth == consta"
        #print(converttosquare(positionx, positiony),depth, evaluationfunction(tempboard, xturn), alpha, beta,)
        outputqueue(converttosquare(positionx, positiony),depth, evaluationfunction(tempboard, xturn), alpha, beta)
        #print evaluationfunction(tempboard, turn)
        return evaluationfunction(tempboard, xturn)

    if len(avm) == 0:

        avmnext = allvalidmoves(tempboard, opponent)

        if(len(avmnext)==0):
            #print("if(len(avmnext)==0):")
            v = max(v, minvalue(tempboard, "pass", "pass", alpha, beta, opponent, depth + 1, True))
            alpha = max(alpha, v)
            #print("2")
            if positionx == "root" and positiony == "root":
                #print("root", depth, v, alpha, beta)
                outputqueue("root", depth, v, alpha, beta)
            elif positionx == "pass" and positiony == "pass":
                #print("pass", depth, v, alpha, beta)
                outputqueue("pass", depth, v, alpha, beta)
            else:
                #print(converttosquare(positionx, positiony), depth, v, alpha, beta)
                outputqueue(converttosquare(positionx, positiony), depth, v, alpha, beta)

        else:
            #print("else if(len(avmnext)==0):")
            v = max(v, minvalue(tempboard, "pass", "pass", alpha, beta, opponent, depth + 1, False))
            if v >= beta:
                #print(converttosquare(positionx, positiony), depth, v, alpha, beta)
                outputqueue(converttosquare(positionx, positiony), depth, v, alpha, beta)
            else:
                alpha = max(alpha, v)
                #print("3")
                if positionx == "root" and positiony == "root":
                    #print("root", depth, v, alpha, beta)
                    outputqueue("root", depth, v, alpha, beta)
                elif positionx == "pass" and positiony == "pass":
                    #print("pass", depth, v, alpha, beta)
                    outputqueue("pass", depth, v, alpha, beta)
                else:
                    #print(converttosquare(positionx, positiony), depth, v, alpha, beta)
                    outputqueue(converttosquare(positionx, positiony), depth, v, alpha, beta)

    else:
        #print("else")
        for m in range(len(avm)):

            boardmax = copy.deepcopy(tempboard)
            flipboard = flip(tempboard, turn, avm[m][0], avm[m][1])
            fornow = copy.deepcopy(flipboard)
            tempv = minvalue(flipboard, avm[m][0], avm[m][1], alpha, beta, opponent, depth + 1, False)
            if depth == 0:
                if tempv > v:
                    #print ("In temp > v")
                    bestboard = fornow
            v = max(v, tempv)
            tempboard = boardmax

            if v >= beta:
                #print ("In v >= beta")
                #print(converttosquare(positionx, positiony), depth, v, alpha, beta)
                outputqueue(converttosquare(positionx, positiony), depth, v, alpha, beta)
                return v
            #print("4")
            alpha = max(alpha, v)
            if positionx == "root" and positiony == "root":
                ##print("root", depth, v, alpha, beta)
                outputqueue("root", depth, v, alpha, beta)
            elif positionx == "pass" and positiony == "pass":
                #print("pass", depth, v, alpha, beta)
                outputqueue("pass", depth, v, alpha, beta)
            else:
                #print(converttosquare(positionx, positiony), depth, v, alpha, beta)
                outputqueue(converttosquare(positionx, positiony), depth, v, alpha, beta)

    #print ("leaving MAX value", depth)

    if depth == 0:
        printbestmove(bestboard)
    return v


def minvalue(tempboard, positionx, positiony, alpha, beta, turn, depth, gameover):

    if turn == 'X':
        opponent = 'O'
    else:
        opponent = 'X'

    #print("MIN VALUE", depth)
    #print positionx, positiony, turn
    w = float("inf")
    #print turn, gameover

    #print("1")
    if positionx == "root" and positiony == "root":
        #print("root", depth, w, alpha, beta)
        outputqueue("root", depth, w, alpha, beta)
    elif positionx == "pass" and positiony == "pass":
        #print("pass", depth, w, alpha, beta)
        outputqueue("pass", depth, w, alpha, beta)
    elif depth != consta:
        #print(converttosquare(positionx, positiony), depth, w, alpha, beta)
        outputqueue(converttosquare(positionx, positiony), depth, w, alpha, beta)

    if gameover is True and positionx == "pass" and positiony == "pass" and depth + 1 == consta:
        #print "gameover"
        #print("pass",depth+1, evaluationfunction(tempboard, xturn), alpha, beta)
        outputqueue("pass",depth+1, evaluationfunction(tempboard, xturn), alpha, beta)
        #print("pass", depth, evaluationfunction(tempboard, xturn), max(alpha, evaluationfunction(tempboard, xturn)), beta)
        outputqueue("pass", depth, evaluationfunction(tempboard, xturn), max(alpha, evaluationfunction(tempboard, xturn)), beta)
        return evaluationfunction(tempboard, xturn)


    if gameover is True and positionx == "pass" and positiony == "pass":
        #print "gameover"
        #print("pass",depth+1, evaluationfunction(tempboard, xturn), alpha, beta)
        outputqueue("pass",depth+1, evaluationfunction(tempboard, xturn), alpha, beta)
        #print("pass", depth, evaluationfunction(tempboard, xturn), alpha, min(beta,evaluationfunction(tempboard, xturn)))
        outputqueue("pass", depth, evaluationfunction(tempboard, xturn), alpha, min(beta,evaluationfunction(tempboard, xturn)))
        return evaluationfunction(tempboard, xturn)


    avm =allvalidmoves(tempboard, turn)

    if depth == consta:
        #print "depth == consta"
        #print(converttosquare(positionx, positiony),depth, evaluationfunction(tempboard, xturn), alpha, beta)
        outputqueue(converttosquare(positionx, positiony),depth, evaluationfunction(tempboard, xturn), alpha, beta)
        #print ("leaving MIN with leaf")
        return evaluationfunction(tempboard, xturn)

    if len(avm)==0:
        avmnext = allvalidmoves(tempboard, opponent)

        if(len(avmnext)==0):
            #print "(len(avmnext)==0):"
            w = min(w, maxvalue(tempboard, "pass", "pass", alpha, beta, opponent, depth + 1, True))
            beta = min(beta, w)
            #print("2")
            if positionx == "root" and positiony == "root":
                #print("root", depth, w, alpha, beta)
                outputqueue("root", depth, w, alpha, beta)
            elif positionx == "pass" and positiony == "pass":
                #print("pass", depth, w, alpha, beta)
                outputqueue("pass", depth, w, alpha, beta)
            else:
                #print(converttosquare(positionx, positiony), depth, w, alpha, beta)
                outputqueue(converttosquare(positionx, positiony), depth, w, alpha, beta)
        else:
            #print("else of (len(avmnext)==0):")
            w = min(w, maxvalue(tempboard, "pass", "pass", alpha, beta, opponent, depth + 1, False))
            #print("3")
            #print w, alpha, beta
            if w <= alpha:
                #print ("Hi")
                #print(converttosquare(positionx,positiony), depth, w, alpha, beta)
                outputqueue(converttosquare(positionx, positiony), depth, w, alpha, beta)
            else:
                beta = min(w, beta)
                #print w, alpha, beta
                if positionx == "root" and positiony == "root":
                    print("root", depth, w, alpha, beta)
                    outputqueue("root", depth, w, alpha, beta)
                elif positionx == "pass" and positiony == "pass":
                    print("pass", depth, w, alpha, beta)
                    outputqueue("pass", depth, w, alpha, beta)
                else:
                    #print converttosquare(positionx, positiony)
                    #print(converttosquare(positionx, positiony), depth, w, alpha, beta)
                    outputqueue(converttosquare(positionx, positiony), depth, w, alpha, beta)

    else:
        #print ("else")
        for n in range(len(avm)):

            boardmin = copy.deepcopy(tempboard)
            flipboard = flip(tempboard, turn, avm[n][0], avm[n][1])
            w = min(w, maxvalue(flipboard, avm[n][0], avm[n][1], alpha, beta, opponent, depth + 1, False))
            tempboard = boardmin


            if w <= alpha:
                #print("In here")
                #print(converttosquare(positionx,positiony), depth, w, alpha, beta)
                outputqueue(converttosquare(positionx,positiony), depth, w, alpha, beta)
                return w

            beta = min(beta, w)
            #print("4")
            if positionx == "root" and positiony == "root":
                #print("root", depth, w, alpha, beta)
                outputqueue("root", depth, w, alpha, beta)
            elif positionx == "pass" and positiony == "pass":
                #print("pass", depth, w, alpha, beta)
                outputqueue("pass", depth, w, alpha, beta)
            else:
                #print(converttosquare(positionx,positiony), depth, w, alpha, beta)
                outputqueue(converttosquare(positionx,positiony), depth, w, alpha, beta)
    #print ("leaving MIN value", depth)
    return w


def isvalidmove(board, turn, x, y):

    if turn == 'X':
        opponent = 'O'
    else:
        opponent = 'X'
    temp = False

    if board[x][y] == 'X' or board[x][y] == 'O':
        return False

    d = [[-1, 1], [-1, 0], [-1, -1], [0, 1], [0, -1], [1, 1], [1, 0], [1, -1]]
    xt, yt = x, y
    for a, b in d:
        x, y = xt, yt
        x = x + a
        y = y + b
        if checklimit(x, y) is False:
            continue
        if board[x][y] == turn:
            continue
        while board[x][y] == opponent:
            x = x + a
            y = y + b
            if checklimit(x, y) is False:
                break
        if checklimit(x, y) is False:
            continue
        if board[x][y] == turn:
            while x != xt or y != yt:
                x = x-a
                y = y-b
                temp = True
    return temp

def flip(tempboard, turn, x, y):

    if turn == 'X':
        opponent = 'O'
    else:
        opponent = 'X'

    d = [[-1, 1], [-1, 0], [-1, -1], [0, 1], [0, -1], [1, 1], [1, 0], [1, -1]]
    xt, yt = x, y
    for a, b in d:
        x, y = xt, yt
        x = x + a
        y = y + b
        if checklimit(x, y) is False:
            continue
        if tempboard[x][y] == turn:
            continue
        while tempboard[x][y] == opponent:
            x = x + a
            y = y + b
            if checklimit(x, y) is False:
                break
        if checklimit(x, y) is False:
            continue

        if tempboard[x][y] == turn:
            while x != xt or y != yt:
                x = x-a
                y = y-b
                tempboard[x][y] = turn
    return tempboard

def evaluationfunction(tempboard, turn1):

   # print("In evaluation function")
   # print turn1
    if turn1 == 'X':
        opp = 'O'
    else:
        opp = 'X'

    func = [[99, -8, 8, 6, 6, 8, -8, 99], [-8, -24, -4, -3, -3, -4, -24, -8], [8, -4, 7, 4, 4, 7, -4, 8], [6, -3, 4, 0, 0, 4, -3, 6], [6, -3, 4, 0, 0, 4, -3, 6], [8, -4, 7, 4, 4, 7, -4, 8], [-8, -24, -4, -3, -3, -4, -24, -8], [99, -8, 8, 6, 6, 8, -8, 99] ]


    value1, value2 = 0, 0
    for j in range(8):
        for k in range(8):
            if tempboard[j][k] == turn1:
                value1 += func[j][k]
            if tempboard[j][k] == opp:
                value2 += func[j][k]

    value = value1 - value2
    return value

def allvalidmoves(board, turn):

    valid_moves = []
   # print "In allvalid moves"

    for x in range(8):
        for y in range(8):
            if isvalidmove(board, turn, x, y) is True:
                valid_moves.append([x, y])

    return valid_moves

def checklimit(x, y):

    if 0 <= x <= 7 and 0 <= y <= 7:
        return True
    else:
        return False

def converttosquare(x, y):

    charlist = ["a", "b", "c", "d", "e", "f", "g", "h"]
    x = x + 1
    newy = str(x)
    newx = charlist[y]
    square = str(newx + newy)
    return square

def sortmylist(avm):

    newlist = sorted(avm, key=lambda k: [k[0], k[1]])
    return newlist

def outputqueue(node, depth, value, alpha, beta):

    if alpha == float('inf'):
        alpha = "Infinity"
    if alpha == float('-inf'):
        alpha = "-Infinity"
    if beta == float("inf"):
        beta = "Infinity"
    if beta == float("-inf"):
        beta = "-Infinity"
    if value == float("inf"):
        value = "Infinity"
    if value == float("-inf"):
       value = "-Infinity"

    #print (node+","+str(depth)+","+str(value)+","+str(alpha)+","+str(beta))
    mylist.append(node+","+str(depth)+","+str(value)+","+str(alpha)+","+str(beta))

def printbestmove(inputboard):


    outputboard = ["","","","","","","",""]

    for i in range(8):
        for j in range(8):
            if j == 0:
                outputboard[i] = str(inputboard[i][j])
            else:
                outputboard[i] = str(outputboard[i]) + str(inputboard[i][j])


    opfile = open("output.txt", "w")


    for i in range(8):
        #print outputboard[i]
        opfile.write(outputboard[i]+"\n")

    printalways = "Node,Depth,Value,Alpha,Beta"
    opfile.write(printalways+"\n")

    for i in range(len(mylist)):
        #print mylist[i]
        if i == len(mylist)-1:
            opfile.write(mylist[i])
        else:
            opfile.write(mylist[i]+"\n")

    opfile.close()

if __name__ == "__main__": main()

