import java.io.*;
import java.util.*;

public class KiwiJuiceEasy {
	public int[] thePouring(int[] capacities, int[] bottles, int[] fromId, int[] toId) {

		for (int i = 0; i < fromId.length; i++) {
			int f = fromId[i];
			int t = toId[i];

			int vol = Math.min(bottles[f],  capacities[t] - bottles[t]);

			bottles[f] -= vol;
			bottles[t] += vol;			
		}
		
		return bottles;
	}

// CUT begin
	public static void main(String[] args){
		System.err.println("KiwiJuiceEasy (250 Points)");
		System.err.println();
		HashSet<Integer> cases = new HashSet<Integer>();
        for (int i = 0; i < args.length; ++i) cases.add(Integer.parseInt(args[i]));
        runTest(cases);
	}

	static void runTest(HashSet<Integer> caseSet) {
	    int cases = 0, passed = 0;
	    while (true) {
	    	String label = Reader.nextLine();
	    	if (label == null || !label.startsWith("--"))
	    		break;

            int[] capacities = new int[Integer.parseInt(Reader.nextLine())];
            for (int i = 0; i < capacities.length; ++i)
                capacities[i] = Integer.parseInt(Reader.nextLine());
            int[] bottles = new int[Integer.parseInt(Reader.nextLine())];
            for (int i = 0; i < bottles.length; ++i)
                bottles[i] = Integer.parseInt(Reader.nextLine());
            int[] fromId = new int[Integer.parseInt(Reader.nextLine())];
            for (int i = 0; i < fromId.length; ++i)
                fromId[i] = Integer.parseInt(Reader.nextLine());
            int[] toId = new int[Integer.parseInt(Reader.nextLine())];
            for (int i = 0; i < toId.length; ++i)
                toId[i] = Integer.parseInt(Reader.nextLine());
            Reader.nextLine();
            int[] __answer = new int[Integer.parseInt(Reader.nextLine())];
            for (int i = 0; i < __answer.length; ++i)
                __answer[i] = Integer.parseInt(Reader.nextLine());

            cases++;
            if (caseSet.size() > 0 && !caseSet.contains(cases - 1))
                continue;
    		System.err.print(String.format("  Testcase #%d ... ", cases - 1));

            if (doTest(capacities, bottles, fromId, toId, __answer))
                passed++;
	    }
	    if (caseSet.size() > 0) cases = caseSet.size();
        System.err.println(String.format("%nPassed : %d/%d cases", passed, cases));

        int T = (int)(System.currentTimeMillis() / 1000) - 1432566648;
        double PT = T / 60.0, TT = 75.0;
        System.err.println(String.format("Time   : %d minutes %d secs%nScore  : %.2f points", T / 60, T % 60, 250 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))));
	}

	static boolean doTest(int[] capacities, int[] bottles, int[] fromId, int[] toId, int[] __expected) {
		long startTime = System.currentTimeMillis();
		Throwable exception = null;
		KiwiJuiceEasy instance = new KiwiJuiceEasy();
		int[] __result = new int[0];
		try {
			__result = instance.thePouring(capacities, bottles, fromId, toId);
		}
		catch (Throwable e) { exception = e; }
		double elapsed = (System.currentTimeMillis() - startTime) / 1000.0;

		if (exception != null) {
			System.err.println("RUNTIME ERROR!");
			exception.printStackTrace();
			return false;
		}
		else if (equals(__result, __expected)) {
			System.err.println("PASSED! " + String.format("(%.2f seconds)", elapsed));
			return true;
		}
		else {
			System.err.println("FAILED! " + String.format("(%.2f seconds)", elapsed));
			System.err.println("           Expected: " + toString(__expected));
			System.err.println("           Received: " + toString(__result));
			return false;
		}
	}

	static boolean equals(int[] a, int[] b) {
		if (a.length != b.length) return false;
		for (int i = 0; i < a.length; ++i) if (a[i] != b[i]) return false;
		return true;
	}

	static String toString(int[] arr) {
		StringBuffer sb = new StringBuffer();
		sb.append("[ ");
		for (int i = 0; i < arr.length; ++i) {
			if (i > 0) sb.append(", ");
			sb.append(arr[i]);
		}
		return sb.toString() + " ]";
	}

	static class Reader {
        private static final String dataFileName = "KiwiJuiceEasy.sample";
	    private static BufferedReader reader;

	    public static String nextLine() {
	        try {
                if (reader == null) {
                    reader = new BufferedReader(new InputStreamReader(new FileInputStream(dataFileName)));
                }
                return reader.readLine();
	        }
	        catch (IOException e) {
	            System.err.println("FATAL!! IOException");
	            e.printStackTrace();
	            System.exit(1);
	        }
	        return "";
	    }
	}
// CUT end
}
