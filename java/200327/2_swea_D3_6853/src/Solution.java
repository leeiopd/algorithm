import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Solution {
	static int X1;
	static int Y1;
	static int X2;
	static int Y2;
	static int result_in;
	static int result_on;
	static int result_out;
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int T = Integer.parseInt(bf.readLine());

		for (int tc = 1; tc <= T; tc++) {
			StringTokenizer st = new StringTokenizer(bf.readLine());

			X1 = Integer.parseInt(st.nextToken());
			Y1 = Integer.parseInt(st.nextToken());
			X2 = Integer.parseInt(st.nextToken());
			Y2 = Integer.parseInt(st.nextToken());

			result_in = 0;
			result_on = 0;
			result_out = 0;

			int N = Integer.parseInt(bf.readLine());

			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(bf.readLine());

				int x = Integer.parseInt(st.nextToken());
				int y = Integer.parseInt(st.nextToken());
				
				check(x, y);
			}
			bw.write("#"+tc+" "+result_in+" "+result_on+" "+result_out+"\n");
		}
		bw.flush();
		bw.close();
	}
	

	static void check(int x, int y) {
		if (X1 < x && x < X2 && Y1 < y && y < Y2) {
			result_in++;
		}else if(x == X1 && Y1 <= y && y <= Y2) {
			result_on++;
		}else if(x == X2 && Y1 <= y && y <= Y2) {
			result_on++;
		}else if(y == Y1 && X1 <= x && x <= X2) {
			result_on++;
		}else if(y == Y2 && X1 <= x && x <= X2) {
			result_on++;
		}else {
			result_out++;
		}
		
	}
}
