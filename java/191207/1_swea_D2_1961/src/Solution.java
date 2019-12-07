import java.util.*;


public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		int N;
		for (int testCase = 1; testCase <= T; testCase++) {
			N = sc.nextInt();
			int maps[][] = new int[N][N];
			
			for (int y = 0; y < N; y++) {
				for (int x = 0; x < N; x++) {
					maps[y][x] = sc.nextInt();
				}
			}
			System.out.println("#"+testCase);
			for (int y = 0; y < N; y++) {
				for (int x = 0; x < N; x++) {
					System.out.print(maps[N-1-x][y]);
				}
				System.out.print(" ");
				for (int x = 0; x < N; x++) {
					System.out.print(maps[N-1-y][N-1-x]);
				}
				System.out.print(" ");
				for (int x = 0; x < N; x++) {
					System.out.print(maps[x][N-1-y]);
				}
				System.out.print("\n");
			} 
		}
		sc.close();
	}
}
