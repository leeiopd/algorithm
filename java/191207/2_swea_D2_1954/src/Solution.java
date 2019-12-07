import java.util.*;

public class Solution {
	
	public static int dx[] = {1, 0, -1, 0};
	public static int dy[] = {0, 1, 0, -1};
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int T = sc.nextInt();
		int N, cnt, x, y, temp, X, Y;
		for (int testCase = 1; testCase <= T; testCase++) {
			N = sc.nextInt();
			int maps[][] = new int[N][N];
			
			x = 0;
			y = 0;
			temp = 0;
			cnt = 0;

			while (true) {
				cnt ++;
				maps[y][x] = cnt;
				
				X = x + dx[temp];
				Y = y + dy[temp];
				if (X < 0 || X >= N || Y < 0 || Y >= N||maps[Y][X]!=0) {
					temp = (temp+1)%4;
				}				
				x = x + dx[temp];
				y = y + dy[temp];
				
				if (cnt == N*N) {
					break;
				}
			}
			System.out.println("#"+testCase);
			
			for(int i = 0; i < N; i++) {
				for(int j = 0; j<N; j++) {
					if (j == N-1) {
						System.out.print(maps[i][j]+"\n");
					}
					else {
						System.out.print(maps[i][j]+" ");						
					}
				}
			}
			
			
			
		}


		sc.close();
	}
}
