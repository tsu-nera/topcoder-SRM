# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class ShortestPathWithMagic:
    def getTime(self, adj, k):

        n = len(adj)
        d = [[0 for i in range(n)] for j in range(n)]

        # convert string to number
        for row in range(n):
            for col in range(n):
                d[row][col] = int(adj[row][col])

        minCost = [[float('inf') for j in range(k + 1)] for i in range(n)]

        pq = []
        heapq.heappush(pq, (0, 0, 0))

        while len(pq) != 0:
            cost, ind, cnt = heapq.heappop(pq)

            if minCost[ind][cnt] > cost:
                minCost[ind][cnt] = cost

                for i in range(n):
                    if i == ind:
                        continue
                    heapq.heappush(pq, (d[ind][i] + cost, i, cnt))
                    if cnt < k:
                        heapq.heappush(pq, (d[ind][i] * 0.5 + cost, i, cnt + 1))

        ret = float('inf')
        for i in range(k + 1):
            ret = min(ret, minCost[1][i])

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

def do_test(dist, k, __expected):
    startTime = time.time()
    instance = ShortestPathWithMagic()
    exception = None
    try:
        __result = instance.getTime(dist, k);
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
    sys.stdout.write("ShortestPathWithMagic (500 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("ShortestPathWithMagic.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            dist = []
            for i in range(0, int(f.readline())):
                dist.append(f.readline().rstrip())
            dist = tuple(dist)
            k = int(f.readline().rstrip())
            f.readline()
            __answer = float(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(dist, k, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1449749792
    PT, TT = (T / 60.0, 75.0)
    points = 500 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
