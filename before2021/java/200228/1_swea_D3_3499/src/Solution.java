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
			int N = Integer.parseInt(bf.readLine());

			int half = N/2;
			String[] A;
			String[] B;
			if (N%2 == 1) {
				A = new String[half+1];
			}else {
				A = new String[half];
			}
			
			B = new String[half];

			StringTokenizer st = new StringTokenizer(bf.readLine());

			for (int i = 0; i < A.length; i++) {
				A[i] = st.nextToken();
			}

			for (int i = 0; i < B.length; i++) {
				B[i] = st.nextToken();
			}
			
			bw.write("#"+tc);

			for (int i = 0; i < N/2; i++) {
				bw.write(" "+A[i]);
				bw.write(" "+B[i]);
			}
			
			if (N%2 == 1) {
				bw.write(" "+A[half]);
			}
			bw.write("\n");
		}
		bw.flush();
		bw.close();
	}
}
