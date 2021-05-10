import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Solution {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int T = Integer.parseInt(bf.readLine());
		
		for (int tc = 1; tc <= T; tc++) {
			int N = Integer.parseInt(bf.readLine());
			String[][] maps = new String[N][];
			
			for (int y = 0; y < N; y++) {
				maps[y] = bf.readLine().split("");
			}
			
			int center = N/2;
			int result = 0;
			
			for (int y = 0; y < N/2; y++) {
				for (int x = center-y; x <= center+y; x++) {
					result += Integer.parseInt(maps[y][x]);
				}
			}
			
			for (int y = 0; y <= N/2; y++) {
				for (int x = y; x < N-y; x++) {
					result += Integer.parseInt(maps[y+N/2][x]);
				}
			}
			
			bw.write("#"+tc+" "+result+"\n");
		}
		bw.flush();
		bw.close();
	}
}
