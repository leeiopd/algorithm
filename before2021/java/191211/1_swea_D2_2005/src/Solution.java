import java.util.*;
public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		int N;
		int tri[][];
		for (int testCase = 1; testCase <= T; testCase++) {
			N = sc.nextInt();
			tri = new int[N][N];
			
			for (int i = 0; i < N; i++) {
				tri[i][0] = 1;
				tri[i][i] = 1;
			}
			
			for (int i = 2; i < N; i++) {
				for (int j = 1; j < i; j++ ) {
					tri[i][j] = tri[i-1][j-1] + tri[i-1][j]; 
				}
			}
			
			System.out.println("#"+testCase);
			
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < i+1; j++) {
					System.out.print(tri[i][j]+" ");
				}
				System.out.println();
			}
			
		}
		sc.close();
	}
}
