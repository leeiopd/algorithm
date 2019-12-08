import java.util.*;

public class Solution {
	public static int maps[][];
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		int N, M, result, temp;
		for (int testCase=1; testCase<=T; testCase++) {
			N = sc.nextInt();
			M = sc.nextInt();
			result = 0;
			maps = new int[N][N];
			
			for (int y = 0; y < N; y++) {
				for (int x = 0; x < N; x++) {
					maps[y][x] = sc.nextInt();
				}
			}
			
			for (int y=0; y <= N-M; y++) {
				for (int x = 0; x <= N-M; x++) {
					temp = game(x, y, M);
					if (result < temp) {
						result = temp;
					}
				}
			}
			System.out.println("#"+testCase+" "+result);
		}
		sc.close();
	}
	
	
	public static int game(int x, int y, int M) {
		int result  = 0;
		for (int i = y ; i < y+M; i++) {
			for (int j = x; j < x+M; j++) {
				result += maps[i][j];
			}
		}
		 
		
		return result;
	}
}
