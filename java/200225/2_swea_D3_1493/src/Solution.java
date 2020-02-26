import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Solution {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int[][] maps = new int[82][82];
		
		maps[1][1] = 1;
		
		for (int x = 2; x <= 80; x++) {
			maps[1][x] = maps[1][x-1]+x; 
		}
		
		for (int y = 2; y <= 80; y++) {
			maps[y][1] = maps[y-1][1] + y-1;
			int cnt = y;
			for (int x = 2; x <= 80; x++) {
				cnt++;
				maps[y][x] = maps[y][x-1]+cnt;
			}
		}
		
		
		int T = Integer.parseInt(bf.readLine());
		
		for (int tc = 1; tc <= T; tc++) {
			StringTokenizer st = new StringTokenizer(bf.readLine());
			
			int p = Integer.parseInt(st.nextToken());
			int q = Integer.parseInt(st.nextToken());
			
			
			if (p > q) {
				int tmp = p;
				p = q;
				q = tmp;
			}
			
			int aX = 0;
			int aY = 0;
			int bX = 0;
			int bY = 0;
			
			int flag = 0;
			
			for(int Y = 1; Y <= 80; Y++) {
				if (flag == 1) {
					break;
				}
				for (int X = 1; X <= 80; X++) {
					if (maps[Y][X] == p) {
						aX = X;
						aY = Y;
					}
					
					if (maps[Y][X] == q) {
						bX = X;
						bY = Y;
						
						flag = 1;
						break;
					}
				}
			}
			
			int result = maps[aY+bY][aX + bX];
			
			bw.write("#"+tc+" "+result+"\n");
			
		}
		bw.flush();
		bw.close();
	}
}
