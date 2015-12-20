# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class FarmvilleDiv2:
    def insertion_sort(self, time, cost, N):
        for i in range(1, N):
            v1 = time[i]
            v2 = cost[i]
            j = i - 1
            while j >= 0 and cost[j] > v2:
                time[j + 1] = time[j]
                cost[j + 1] = cost[j]
                j -= 1
            time[j + 1] = v1
            cost[j + 1] = v2
        return time, cost

    def minTime(self, time, cost, budget):
        time = list(time)
        cost = list(cost)
        time, cost = self.insertion_sort(time, cost, len(cost))

        ret = 0

        for t, c in zip(time, cost):
            for i in range(t):
                if budget - c >= 0:
                    budget -= c
                else:
                    ret += 1

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

def do_test(time2, cost, budget, __expected):
    startTime = time.time()
    instance = FarmvilleDiv2()
    exception = None
    try:
        __result = instance.minTime(time2, cost, budget);
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
    sys.stdout.write("FarmvilleDiv2 (250 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("FarmvilleDiv2.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            time2 = []
            for i in range(0, int(f.readline())):
                time2.append(int(f.readline().rstrip()))
            time2 = tuple(time2)
            cost = []
            for i in range(0, int(f.readline())):
                cost.append(int(f.readline().rstrip()))
            cost = tuple(cost)
            budget = int(f.readline().rstrip())
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(time2, cost, budget, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1450454446
    PT, TT = (T / 60.0, 75.0)
    points = 250 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
