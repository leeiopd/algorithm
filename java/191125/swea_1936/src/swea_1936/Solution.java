package swea_1936;

import java.util.*;

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int A = sc.nextInt();
		int B = sc.nextInt();
		char winner = 0;
//		1 = 가위
//		2 = 바위
//		3 = 보
		if (A == 1) {
			if (B==2) {
				winner = 'B';
			}
			else if(B==3) {
				winner = 'A';
			}
		}
		
		else if(A == 2) {
			if (B == 1) {
				winner = 'A';
			}
			else if (B == 3) {
				winner = 'B';
			}
		}
		
		else if (A == 3) {
			if (B == 1) {
				winner = 'B';
			}
			else if (B == 2) {
				winner = 'A';
			}
		}
		
		System.out.println(winner);
		
	}

}
