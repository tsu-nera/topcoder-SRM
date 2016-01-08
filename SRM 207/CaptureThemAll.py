# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

knight_moves = [( -2, -1), ( -2, 1), (2, -1), (2, 1), ( -1, -2), (1, -2), ( -1, 2), (1, 2)]

def strToPos(p):
    return ord(p[0]) - ord('a'), int(p[1]) - 1

class CaptureThemAll:
    def fastKnight(self, knight, rook, queen):
        queue = collections.deque()

        rpos = strToPos(rook)
        qpos = strToPos(queen)
        kpos = strToPos(knight)
        visited = {}

        queue.append((kpos, False, False, 0))

        while len(queue) > 0:
            (k, haveR, haveQ, moves) = queue.popleft()
            if haveR and haveQ:
                return moves

            key = (k, haveR, haveQ)
            visited[key] = True
            moves += 1

            for (r, c) in knight_moves:
                p = (k[0] + r, k[1] + c)
                if p[0] < 0 or p[0] > 7 or p[1] < 0 or p[1] > 7 or (p, haveR, haveQ) in visited:
                    continue
                queue.append((p, haveR or p == rpos, haveQ or p == qpos, moves))
        return -1

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

def do_test(knight, rook, queen, __expected):
    startTime = time.time()
    instance = CaptureThemAll()
    exception = None
    try:
        __result = instance.fastKnight(knight, rook, queen);
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
    sys.stdout.write("CaptureThemAll (1000 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("CaptureThemAll.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            knight = f.readline().rstrip()
            rook = f.readline().rstrip()
            queen = f.readline().rstrip()
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(knight, rook, queen, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1452234281
    PT, TT = (T / 60.0, 75.0)
    points = 1000 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
