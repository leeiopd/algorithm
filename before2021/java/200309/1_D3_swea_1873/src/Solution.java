import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Solution {	
	static int H;
	static int W;
	static int x;
	static int y;
	static char tank;
	static char[][] maps;
	static String commands;

	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int T = Integer.parseInt(bf.readLine());
		maps = new char[20][20];

		for (int tc = 1; tc <= T; tc++) {
			StringTokenizer st = new StringTokenizer(bf.readLine());

			H = Integer.parseInt(st.nextToken());
			W = Integer.parseInt(st.nextToken());

			
			
			for (int i = 0; i < H; i++) {
				String temp = bf.readLine();
				for (int j = 0; j < W; j++) {
					maps[i][j] = temp.charAt(j);
				}
			}
			
			findT();
			
			int N = Integer.parseInt(bf.readLine());

			commands = bf.readLine();


			for (int i = 0; i < N; i++) {
				game(commands.charAt(i), x, y);
			}
			
			bw.write("#"+tc+" ");
			
			for (int i = 0; i < H; i++) {
				for (int j = 0; j < W; j++) {
					bw.write(maps[i][j]);
				}
				bw.write("\n");
			}
			
		}
		bw.flush();
		bw.close();
	}
	static void findT() {
		for (int i = 0; i < H; i++) {
			for (int j = 0; j < W; j++) {
				if (maps[i][j] == '<' || maps[i][j] == '>' ||maps[i][j] == '^' ||maps[i][j] == 'v' ) {
					x = j;
					y = i;
					tank = maps[i][j];
					return;
				}
			}
		}
	}
	static void game(char command, int fncX, int fncY) {
		switch (command) {
		case 'U':
			tank = '^';

			if (fncY - 1 >= 0 && maps[fncY-1][fncX] == '.') {
				y = fncY-1;
				maps[fncY][fncX] = '.';
				maps[fncY-1][fncX] = tank;
			}else {
				maps[fncY][fncX] = tank;
			}

			break;

		case 'D':
			tank = 'v';

			if (fncY + 1 < H && maps[fncY+1][fncX] == '.') {
				y = fncY+1;
				maps[fncY][fncX] = '.';
				maps[fncY+1][fncX] = tank;
			}else {
				maps[fncY][fncX] = tank;
			}

			break;

		case 'L':
			tank = '<';

			if (fncX - 1 >= 0 && maps[fncY][fncX-1] == '.') {
				x = fncX-1;
				maps[fncY][fncX] = '.';
				maps[fncY][fncX-1] = tank;
			}else {
				maps[fncY][fncX] = tank;
			}

			break;

		case 'R':
			tank = '>';

			if (fncX + 1 < W && maps[fncY][fncX+1] == '.') {
				x = fncX+1;
				maps[fncY][fncX] = '.';
				maps[fncY][fncX+1] = tank;
			}else {
				maps[fncY][fncX] = tank;
			}

			break;

		case 'S':
			shoot();
			break;
		}
		return;
	}

	static void shoot() {
		switch (tank) {
		case '^':
			for (int i = y; i >= 0; i--) {
				if (maps[i][x]=='*' || maps[i][x] == '#') {
					if (maps[i][x] == '*') {
						maps[i][x] = '.';
					}
					return;
				}
			}
			break;
		case 'v':
			for (int i = y; i < H; i++) {
				if (maps[i][x]=='*' || maps[i][x] =='#') {
					if (maps[i][x] == '*') {
						maps[i][x] = '.';
					}
					return;
				}
			}
			break;
		case '<':
			for (int i = x; i >= 0; i--) {
				if (maps[y][i]=='*' || maps[y][i] == '#') {
					if (maps[y][i] == '*') {
						maps[y][i] = '.';
					}
					return;
				}
			}
			break;
		case '>':
			for (int i = x; i < W; i++) {
				if (maps[y][i]=='*' || maps[y][i] == '#') {
					if (maps[y][i] == '*') {
						maps[y][i] = '.';
					}
					return;
				}
			}
			break;

		}

		return;
	}
}
