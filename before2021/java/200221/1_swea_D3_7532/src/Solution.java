import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Solution {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int T = Integer.parseInt(bf.readLine());

		for (int tc = 1; tc <= T; tc++) {
			StringTokenizer st = new StringTokenizer(bf.readLine());

			int S = Integer.parseInt(st.nextToken());
			int E = Integer.parseInt(st.nextToken());
			int M = Integer.parseInt(st.nextToken());

			int cnt =0;

			while (true) {
				if ((S == 365 & cnt % 365 == 0) | cnt % 365 == S) {
					if ((E == 24 & cnt % 24 == 0) | cnt % 24 == E) {
						if ((M == 29 & cnt %29 == 0)| cnt % 29 == M) {
							break;
						}
					}
				}
				cnt += 365;
			}
			bw.write("#"+tc+" "+cnt+"\n");
		}
		bw.flush();
		bw.close();
	}
}
