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
			
			// �� ��� ��
			W = sc.nextInt();
			

			// A�� - ���Ͷ� P
			A = P * W;

			// B�� - �⺻��� Q, R ���ϸ� �⺻���, R���� ������ �ʰ��������� ���ʹ� S���� �� ������
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
