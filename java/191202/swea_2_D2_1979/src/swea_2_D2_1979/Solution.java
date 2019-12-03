package swea_2_D2_1979;

import java.util.*;

public class Solution {
	static int N, K;
	static int maps[][];
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		int result;
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
				for(int x = 0; x < N; x++) {
					if (maps[y][x] == 1) {
						result += rowCheck(x, y);						
					}
					
				}
			}
			
//			세로 체크
			for (int y = 0; y < N; y++) {
				for(int x = 0; x < N; x++) {
					if (maps[y][x] == 1) {						
						result += colCheck(x, y);
					}
				}
			}
			System.out.println(result);
		}
		sc.close();
	}
	
	static int rowCheck(int x, int y) {
		int cnt = 1;
		for (int i = 1; i < K; i++) {
			if (x+i >= N) {
				return 0;
			}
			if (maps[y][x+i] == 0) {
				return 0;
			}
			cnt ++;
		}
		if (cnt == K) {
			return 1;			
		}
		else {
			return 0;
		}
	}
	
	static int colCheck(int x, int y) {
		int cnt = 1;
		for (int i = 1; i < K; i++) {
			if (y+i >= N) {
				return 0;
			}
			if (maps[y+i][x] == 0) {
				return 0;
			}
			cnt ++;
		}
		if (cnt == K) {
			return 1;			
		}
		else {
			return 0;
		}
	}
}
