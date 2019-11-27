package swea_1945;

import java.util.Scanner;

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		int N;
		int a, b, c, d, e;
		for (int testCase=1; testCase <= T; testCase++) {
			N = sc.nextInt();
			a = b = c = d = e = 0;
			while (N>1) {
				if (N%11==0) {
					e += 1;
					N /= 11;
				}
				else if(N%7==0) {
					d += 1;
					N /= 7;
				}
				else if(N%5==0) {
					c += 1;
					N /= 5;
				}
				else if(N%3==0) {
					b += 1;
					N /= 3;
				}
				else if(N%2==0) {
					a += 1;
					N /= 2;
				}
			}
			System.out.println("#"+testCase+" "+a+" "+b+" "+c+" "+d+" "+e);
		}
	}
}
