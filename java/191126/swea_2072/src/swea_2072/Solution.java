package swea_2072;

import java.util.Scanner;

public class Solution {
	static public void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		int answer= 0;
		int tmp = 0;
		for (int testCase = 1; testCase<=T; testCase++) {
			answer = 0;
			for (int i=0; i < 10; i++) {
				tmp = sc.nextInt();
				if (tmp%2 != 0) {
					answer += tmp;
				}
			}
			System.out.println("#"+testCase+" "+answer);
		}
	}
}
