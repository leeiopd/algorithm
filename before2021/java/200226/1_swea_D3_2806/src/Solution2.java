import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Solution2 {
	static int[] maps  = null;
	static int N = 0;
	static int result;

	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int T = Integer.parseInt(bf.readLine());

		for (int tc = 1; tc <= T; tc++) {
			N = Integer.parseInt(bf.readLine());

			maps = new int[N];
			result = 0;

			for (int x = 0; x < N; x++) {
				maps[0] = x;
				game(1);
			}

			bw.write("#"+tc+" "+result+"\n");

		}
		bw.flush();
		bw.close();
	}

	public static void game(int cnt) {
		if (cnt == N) {
			result++;
			return;
		}
		
		for (int X = 0; X < N; X++) {
			boolean next = true;
			for (int j = 0; j < cnt; j++) {
				if (X == maps[j] || X == maps[j]+(cnt-j)|| X==maps[j]-(cnt-j) ) {
					next = false;
					break;
				}	
			}
			if (next) {
				maps[cnt] = X;
				game(cnt+1);				
			}
		}
	}
}
