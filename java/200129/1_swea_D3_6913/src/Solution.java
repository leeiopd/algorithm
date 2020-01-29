import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(bf.readLine());
		
		
		for (int tc = 1; tc <= T; tc++) {
			String[] nums = bf.readLine().split(" ");
			
			int N = Integer.parseInt(nums[0]);
			int M = Integer.parseInt(nums[1]);
			
			int[][] maps = new int[N][M+1];
			
			int PeopleCnt = 0;
			int ANSCnt = 0;
			for (int i = 0; i < N; i++) {
				StringTokenizer st = new StringTokenizer(bf.readLine());
				int cnt = 0;
				for (int j = 0; j < M; j++) {
					if (Integer.parseInt(st.nextToken()) == 1) {
						cnt++;
					}
				}
				maps[i][M] = cnt;
				
				if (cnt > ANSCnt) {
					ANSCnt = cnt;
				}
			}
			
			for (int i = 0; i < N; i++) {
				if (maps[i][M] == ANSCnt) {
					PeopleCnt++;
				}
			}
			
			System.out.println("#"+tc+" "+PeopleCnt+" "+ANSCnt);
			
			
		}
	}
}
