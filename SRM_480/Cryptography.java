import java.io.*;
import java.util.*;

public class Cryptography {
	long multiple(int a, int b) { return (long) a * b; }
	
	public long encrypt(int[] numbers) {

		List list = Arrays.asList(numbers);

		return (long) list.stream()
			.reduce(Bitdicimal::ONE, Bitdicimal::multiple);
		
// 		long ans = 0;
// 
// 		for (int i = 0; i < numbers.length; i++) {
// 			long seki = 1;
// 			for (int j = 0; j < numbers.length; j++) {
// 				if (i == j) {
// 					seki *= (numbers[j] + 1);
// 				}
// 				else {
// 					seki *= numbers[j];
// 				}
// 			}
// 			ans = Math.max(ans, seki);
// 		}
// 		return ans;
 	}

// CUT begin
	public static void main(String[] args){
		System.err.println("Cryptography (250 Points)");
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

            int[] numbers = new int[Integer.parseInt(Reader.nextLine())];
            for (int i = 0; i < numbers.length; ++i)
                numbers[i] = Integer.parseInt(Reader.nextLine());
            Reader.nextLine();
            long __answer = Long.parseLong(Reader.nextLine());

            cases++;
            if (caseSet.size() > 0 && !caseSet.contains(cases - 1))
                continue;
    		System.err.print(String.format("  Testcase #%d ... ", cases - 1));

            if (doTest(numbers, __answer))
                passed++;
	    }
	    if (caseSet.size() > 0) cases = caseSet.size();
        System.err.println(String.format("%nPassed : %d/%d cases", passed, cases));

        int T = (int)(System.currentTimeMillis() / 1000) - 1432623628;
        double PT = T / 60.0, TT = 75.0;
        System.err.println(String.format("Time   : %d minutes %d secs%nScore  : %.2f points", T / 60, T % 60, 250 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))));
	}

	static boolean doTest(int[] numbers, long __expected) {
		long startTime = System.currentTimeMillis();
		Throwable exception = null;
		Cryptography instance = new Cryptography();
		long __result = 0;
		try {
			__result = instance.encrypt(numbers);
		}
		catch (Throwable e) { exception = e; }
		double elapsed = (System.currentTimeMillis() - startTime) / 1000.0;

		if (exception != null) {
			System.err.println("RUNTIME ERROR!");
			exception.printStackTrace();
			return false;
		}
		else if (__result == __expected) {
			System.err.println("PASSED! " + String.format("(%.2f seconds)", elapsed));
			return true;
		}
		else {
			System.err.println("FAILED! " + String.format("(%.2f seconds)", elapsed));
			System.err.println("           Expected: " + __expected);
			System.err.println("           Received: " + __result);
			return false;
		}
	}

	static class Reader {
        private static final String dataFileName = "Cryptography.sample";
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
