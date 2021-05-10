package swea_2_D2_1284;

import java.util.Scanner;

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		
		int P, Q, R, S, W, A, B, result;
		
		
		for (int testCase = 1; testCase <= T; testCase++) {
			result = 0;
			P = sc.nextInt();
			Q = sc.nextInt();
			R = sc.nextInt();
			S = sc.nextInt();
			
			// 총 사용 량
			W = sc.nextInt();
			

			// A사 - 리터랑 P
			A = P * W;

			// B사 - 기본요금 Q, R 이하면 기본요금, R보다 많으면 초과량에대해 리터당 S원을 더 내야함
			if (W <= R) {
				B = Q;
			}
			else {
				B = Q + S * (W - R);
			}
			
			if (A < B) {
				result = A;
			}
			else {
				result = B;
			}
			
			System.out.println("#"+testCase+" "+result);
		}
	}
}
