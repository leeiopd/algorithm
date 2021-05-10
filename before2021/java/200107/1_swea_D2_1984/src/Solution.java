import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class Solution {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(bf.readLine());
		double result, temp;
		
		for (int tc = 1; tc <= T; tc++) {
			double total = 0;
			StringTokenizer st = new StringTokenizer(bf.readLine());
			
			ArrayList<Double> nums = new ArrayList<Double>();
			
			for (int i = 0; i < 10; i++) {
				temp = Double.parseDouble(st.nextToken());
				nums.add(i, temp);
				total += temp;
			}
			
			Collections.sort(nums);
			
			result = (total - (nums.get(0) + nums.get(9)))/8;
			
			System.out.println("#"+tc+" "+Math.round(result));
		}
	}
}
