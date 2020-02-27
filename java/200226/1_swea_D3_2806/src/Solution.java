import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Solution {
	static int[][] maps  = null;
	static int N = 0;
	static int result;

	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int T = Integer.parseInt(bf.readLine());

		for (int tc = 1; tc <= T; tc++) {
			N = Integer.parseInt(bf.readLine());

			maps = new int[N][N];
			result = 0;

			for (int x = 0; x < N; x++) {				
				game(1, 0, x);
			}

			bw.write("#"+tc+" "+result+"\n");

		}
		bw.flush();
		bw.close();
	}

	public static boolean check(int y, int x) {
		for (int L = x; L >= 0; L--) {
			if (maps[y][L] == 1) {
				return false;
			}
		}

		for (int U = y; U >= 0; U--) {
			if (maps[U][x] == 1) {
				return false;
			}
		}

		for (int R = x; R < N; R++) {
			if (maps[y][R] == 1) {
				return false;
			}
		}

		for (int D = y; D < N; D++) {
			if (maps[y][D] == 1) {
				return false;
			}
		}



		int UR = -1;
		while (true) {
			UR++;
			if (y - UR < 0 || x + UR >= N) {
				break;
			}
			if(maps[y-UR][x+UR] == 1) {
				return false;
			}
		}

		int UL = -1;
		while (true) {
			UL++;
			if (y - UL < 0 || x - UL < 0) {
				break;
			}
			if(maps[y-UL][x-UL] == 1) {
				return false;
			}
		}

		int DR = -1;
		while (true) {
			DR++;
			if (y + DR >= N || x + DR >= N) {
				break;
			}
			if(maps[y+DR][x+DR] == 1) {
				return false;
			}
		}

		int DL = -1;
		while (true) {
			DL++;
			if (y + DL >= N || x - DL < 0) {
				break;
			}
			if(maps[y+DL][x-DL] == 1) {
				return false;
			}
		}

		return true;
	}

	public static void game(int cnt, int y, int x) {
		if (cnt == N) {
			result ++;
			return;
		}
		maps[y][x] = 1;

		int X = x;
		int Y = y;
		while (true) {
			if (X+1 >= N) {
				if (Y+1 < N) { 
					X = 0;
					Y++;
					if (check(Y, 0)) {
						game(cnt+1, Y, 0);
						maps[Y][0] = 0;
					}
				}else {
					break;
				}
			}else {
				X++;
				if (check(Y, X)) {
					game(cnt+1, Y, X);					
					maps[Y][X] = 0;
				}
			}
		}
		maps[y][x] = 0;
	}
}
