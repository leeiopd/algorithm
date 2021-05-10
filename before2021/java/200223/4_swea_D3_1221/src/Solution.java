import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Solution {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int T = Integer.parseInt(bf.readLine());
		
		HashMap<Integer, String> mach = new HashMap<Integer, String>();
		mach.put(0, "ZRO");
		mach.put(1, "ONE");
		mach.put(2, "TWO");
		mach.put(3, "THR");
		mach.put(4, "FOR");
		mach.put(5, "FIV");
		mach.put(6, "SIX");
		mach.put(7, "SVN");
		mach.put(8, "EGT");
		mach.put(9, "NIN");

		for (int t = 1; t <= T; t++) {
			StringTokenizer st = new StringTokenizer(bf.readLine());
			String tc = st.nextToken();
			int len = Integer.parseInt(st.nextToken());

			st = new StringTokenizer(bf.readLine());

			int[] nums = new int[10];

			for (int i = 0; i < len; i++) {
				switch (st.nextToken()) {
				case "ZRO":
					nums[0]++;
					break;
				case "ONE":
					nums[1]++;
					break;
				case "TWO":
					nums[2]++;
					break;
				case "THR":
					nums[3]++;
					break;
				case "FOR":
					nums[4]++;
					break;
				case "FIV":
					nums[5]++;
					break;
				case "SIX":
					nums[6]++;
					break;
				case "SVN":
					nums[7]++;
					break;
				case "EGT":
					nums[8]++;
					break;
				case "NIN":
					nums[9]++;
					break;
				}
			}
			
			bw.write(tc+"\n");
			
			for (int i = 0; i < 10; i++) {
				for (int j = 0; j < nums[i]; j++) {
					bw.write(" "+mach.get(i));
				}
			}
			bw.write("\n");
		}
		bw.flush();
		bw.close();
	}
}
