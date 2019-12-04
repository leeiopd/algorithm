package swea_2_D2_1979;

import java.util.*;

public class Solution {
	static int N, K;
	static int maps[][];
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int T = sc.nextInt();
		int result, colCnt, rowCnt;
		for (int testCase = 1; testCase <= T; testCase++) {
			N = sc.nextInt();
			K = sc.nextInt();
			maps = new int[N][N];
			result = 0;

			for (int y = 0; y < N; y++) {
				for(int x = 0; x < N; x++) {
					maps[y][x] = sc.nextInt();
				}
			}

			//			가로 체크
			for (int y = 0; y < N; y++) {
				colCnt = 0;
				for(int x = 0; x < N; x++) {
					if (maps[y][x] == 1) {
						colCnt ++;
					}
					else {
						if (colCnt == K) {
							result ++;
						}
						colCnt = 0;
					}
				}
				if (colCnt == K) {
					result ++;
				}
			}

			//			세로 체크
			for (int x = 0; x < N; x++) {
				rowCnt = 0;
				for(int y = 0; y < N; y++) {
					if (maps[y][x] == 1) {
						rowCnt ++;
					}
					else {
						if (rowCnt == K) {
							result ++;
						}
						rowCnt = 0;

					}
				}
				if (rowCnt == K) {
					result ++;
				}
			}
			System.out.println("#"+testCase+" "+result);
		}
		sc.close();
	}
}