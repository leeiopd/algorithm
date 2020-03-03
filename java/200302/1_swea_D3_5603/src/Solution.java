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

			int[] sList = new int[N];
			int add = 0;

			for (int i = 0; i < N; i++) {
				int n = Integer.parseInt(bf.readLine());
				sList[i] = n;
				add += n;
			}

			int avg = add/N;


			int result = 0;

			for (int i = 0; i < N; i++) {
				if (sList[i] > avg) {
					result += (sList[i] - avg);
				}
			}

			bw.write("#"+tc+" "+result+"\n");
		}
		bw.flush();
		bw.close();
	}
}
