package swea_1_D2_1984;

import java.util.*;

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		int A_month, A_day, B_month, B_day, answer;
		int monthArr[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
		for (int testCase = 1; testCase <= T; testCase++) {
			A_month = sc.nextInt();
			A_day = sc.nextInt();
			B_month = sc.nextInt();
			B_day = sc.nextInt();
			answer = 1;
			for (int i = A_month-1; i < B_month-1; i++) {
				answer += monthArr[i];
			}
			answer -= A_day;
			answer += B_day;
			
			System.out.println("#"+testCase+" "+answer);
		}
		sc.close();
	}

}
