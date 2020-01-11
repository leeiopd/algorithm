import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

		int maps[][];
		int N;
		for (int tc = 1; tc < 11; tc++) {
			N = Integer.parseInt(bf.readLine());
			maps = new int[N][N];

			for (int y = 0; y < N; y++) {
				StringTokenizer st = new StringTokenizer(bf.readLine());
				
				for (int x = 0; x < N; x++) {
					maps[y][x] = Integer.parseInt(st.nextToken());
				}	
			}
			
			
			
			int result=0;
			for (int y = 0; y<N; y++) {
				for (int x = 0; x < N; x++) {
					if (maps[y][x] == 1) {
						int next = 1;
						maps[y][x] = 0;
						while (true) {
							if (y+next >= N) {
								break;
							}

							if (maps[y+next][x] == 2) {
								result++;
								maps[y+next][x] = 0;
								break;
							}
							else if(maps[y+next][x] == 1) {
								maps[y+next][x] = 0;
							}
							next++;
						}
					}
				}
			}
			System.out.println("#"+tc+" "+result);
		}
	}
}