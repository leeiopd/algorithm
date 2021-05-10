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

		int T = Integer.parseInt(bf.readLine());

		for (int tc = 1; tc <= T; tc++) {
			StringTokenizer st = new StringTokenizer(bf.readLine());
			int N = Integer.parseInt(st.nextToken());
			int D = Integer.parseInt(st.nextToken());
			int[] map = new int[N];
			int result = 0;

			st = new StringTokenizer(bf.readLine());

			for (int i = 0 ; i <N ; i++) {
				map[i] = Integer.parseInt(st.nextToken());
			}
			
			int cnt = 0;
			int zero = 0;
			while (cnt < N) {
				if (map[cnt] == 0) {
					int i;
					for (i = cnt; i < N; i++) {
						if (map[i] == 1) {
							break;
						}
						zero++;
					}
					
					result += zero/D;
					zero = 0;
					cnt = i;
				}
				cnt++;
			}
			
			bw.write("#"+tc+" "+result+"\n");
		}
		bw.flush();
		bw.close();
	}
}
