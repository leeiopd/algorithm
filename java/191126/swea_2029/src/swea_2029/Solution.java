package swea_2029;

import java.util.Scanner;

public class Solution {
	static public void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for (int testCase = 1; testCase <= T; testCase++) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			
			System.out.println("#"+testCase+" "+a/b+" "+a%b);
			
		}
	}
}
