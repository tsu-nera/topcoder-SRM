# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

from collections import deque

class MazeMaker:
    def longestPath(self, maze, startRow, startCol, moveRow, moveCol):
        width = len(maze[0])
        height = len(maze)
        board = []

        # ボードの初期化
        board = [[-1 for i in range(width)] for j in range(height)]

        # スタート地点のマーク
        board[startRow][startCol] = 0

        # キューの宣言
        queue = deque()
        queue.append([startCol, startRow])

        # キューが空になるまで、一つずつ取り出す
        while len(queue) > 0:
            now = queue.popleft()
            x = now[0]
            y = now[1]

            for i in range(len(moveRow)):
                nextX = x + moveCol[i]
                nextY = y + moveRow[i]

                if 0 <= nextX and nextX < width \
                   and 0 <= nextY and nextY < height \
                   and board[nextY][nextX] == -1 \
                   and maze[nextY][nextX] == ".":
                    # ボードに移動量を更新する
                    board[nextY][nextX] = board[y][x] + 1
                    # 末尾に次の移動点を挿入
                    queue.append([nextX, nextY])

        # 最大移動量の計算
        ret = 0
        for i in range(height):
            for j in range(width):
                # 移動できない点があったら、-1を返す
                if maze[i][j] == "." and board[i][j] == -1:
                    return -1
                ret = max(ret, board[i][j])
        return ret

# CUT begin
# TEST CODE FOR PYTHON {{{
import sys, time, math

def tc_equal(expected, received):
    try:
        _t = type(expected)
        received = _t(received)
        if _t == list or _t == tuple:
            if len(expected) != len(received): return False
            return all(tc_equal(e, r) for (e, r) in zip(expected, received))
        elif _t == float:
            eps = 1e-9
            d = abs(received - expected)
            return not math.isnan(received) and not math.isnan(expected) and d <= eps * max(1.0, abs(expected))
        else:
            return expected == received
    except:
        return False

def pretty_str(x):
    if type(x) == str:
        return '"%s"' % x
    elif type(x) == tuple:
        return '(%s)' % (','.join( (pretty_str(y) for y in x) ) )
    else:
        return str(x)

def do_test(maze, startRow, startCol, moveRow, moveCol, __expected):
    startTime = time.time()
    instance = MazeMaker()
    exception = None
    try:
        __result = instance.longestPath(maze, startRow, startCol, moveRow, moveCol);
    except:
        import traceback
        exception = traceback.format_exc()
    elapsed = time.time() - startTime   # in sec

    if exception is not None:
        sys.stdout.write("RUNTIME ERROR: \n")
        sys.stdout.write(exception + "\n")
        return 0

    if tc_equal(__expected, __result):
        sys.stdout.write("PASSED! " + ("(%.3f seconds)" % elapsed) + "\n")
        return 1
    else:
        sys.stdout.write("FAILED! " + ("(%.3f seconds)" % elapsed) + "\n")
        sys.stdout.write("           Expected: " + pretty_str(__expected) + "\n")
        sys.stdout.write("           Received: " + pretty_str(__result) + "\n")
        return 0

def run_tests():
    sys.stdout.write("MazeMaker (500 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("MazeMaker.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            maze = []
            for i in range(0, int(f.readline())):
                maze.append(f.readline().rstrip())
            maze = tuple(maze)
            startRow = int(f.readline().rstrip())
            startCol = int(f.readline().rstrip())
            moveRow = []
            for i in range(0, int(f.readline())):
                moveRow.append(int(f.readline().rstrip()))
            moveRow = tuple(moveRow)
            moveCol = []
            for i in range(0, int(f.readline())):
                moveCol.append(int(f.readline().rstrip()))
            moveCol = tuple(moveCol)
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(maze, startRow, startCol, moveRow, moveCol, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1449491132
    PT, TT = (T / 60.0, 75.0)
    points = 500 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
