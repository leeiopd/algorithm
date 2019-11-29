package swea_1_D2_1986;

import java.util.*;

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		int N;
		int answer;
		for (int testCase = 1; testCase <= 10; testCase++) {
			N = sc.nextInt();
			answer = 0;
			for(int j = 1; j<=N; j++) {
				if (j%2!=0) {
					answer += j;
				}
				else {
					answer -= j;
				}
			}
			System.out.println("#"+testCase+" "+answer);
		}
	}
}
