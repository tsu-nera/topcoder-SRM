# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class CrazyBot:
    def __init__(self):
        self.grid = [[False for i in range(100)] for j in range(100)]
        self.vx = [1, -1, 0, 0]
        self.vy = [0, 0, 1, -1]
        self.prob = [0.0, 0.0, 0.0, 0.0]

    def dfs(self, x, y, n):
        # 一度通った場所は確率0
        if self.grid[x][y]:
            return 0
        if n == 0:
            return 1

        # 通った場所にフラグを立てる
        self.grid[x][y] = True
        ret = 0.0

        for i in range(4):
            ret += self.dfs(x + self.vx[i],
                            y + self.vy[i],  n - 1) * self.prob[i]

        self.grid[x][y] = False
        return ret

    def getProbability(self, n, east, west, south, north):
        self.prob[0] = east / 100.0
        self.prob[1] = west / 100.0
        self.prob[2] = south / 100.0
        self.prob[3] = north / 100.0

        return self.dfs(50, 50, n)

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

def do_test(n, east, west, south, north, __expected):
    startTime = time.time()
    instance = CrazyBot()
    exception = None
    try:
        __result = instance.getProbability(n, east, west, south, north);
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
    sys.stdout.write("CrazyBot (500 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("CrazyBot.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            n = int(f.readline().rstrip())
            east = int(f.readline().rstrip())
            west = int(f.readline().rstrip())
            south = int(f.readline().rstrip())
            north = int(f.readline().rstrip())
            f.readline()
            __answer = float(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(n, east, west, south, north, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1449403316
    PT, TT = (T / 60.0, 75.0)
    points = 500 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
