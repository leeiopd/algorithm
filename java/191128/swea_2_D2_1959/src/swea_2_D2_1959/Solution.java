package swea_2_D2_1959;

import java.util.Scanner;

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		int N, M;
		
		int result;
		int add;
		
		for (int testCase = 1; testCase <= T; testCase++) {
			N = sc.nextInt();
			M = sc.nextInt();
			
			result = 0;
			
			
			int arrN[] = new int[N];
			int arrM[] = new int[M];
			
			for(int i = 0; i < N; i++) {
				arrN[i] = sc.nextInt();
			}
			
			for(int j = 0; j < M; j++) {
				arrM[j] = sc.nextInt();
			}
			
			if (N > M) {
				int changeTemp = N;
				N = M;
				M = changeTemp;
				
				int changeArr[] = new int[N];
				changeArr = arrN;
				arrN = arrM;
				arrM = changeArr;
			}
			
			for (int k = 0; k<(M-N)+1; k++ ) {
				add = 0;
				for (int w=0; w<N; w++) {
					int hh = arrN[w] * arrM[w+k];
					add += arrN[w] * arrM[w+k];
				}
				if (add > result) {
					result = add;
				}
			}
			
			System.out.println("#"+testCase+" "+result);
		}
		
		sc.close();
	}
}