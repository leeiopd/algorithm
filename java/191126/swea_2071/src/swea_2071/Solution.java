package swea_2071;

import java.util.*;

public class Solution {
	static public void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		int result;
		for (int testCase = 1; testCase <= T; testCase++) {
			result = 0;
			for (int i = 0; i < 10; i++) {
				result += sc.nextInt();
			}
			result = (int) Math.round(result/10.0);
			System.out.println("#"+testCase+" "+result);
		}
	}
}
