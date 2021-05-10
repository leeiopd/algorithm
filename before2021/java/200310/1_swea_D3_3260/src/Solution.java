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

			String[] A = st.nextToken().split("");
			String[] B = st.nextToken().split("");

			if (A.length < B.length) {
				String[] temp = B;
				B = A;
				A = temp;
			}

			int Alen = A.length;
			int Blen = B.length;

			int[] Anums = new int[Alen];
			for (int i = 0; i < Alen; i++) {
				Anums[i] = Integer.parseInt(A[Alen-(i+1)]);
			}

			int[] Bnums = new int[Alen];
			for (int i = 0; i < Blen; i++) {
				Bnums[i] = Integer.parseInt(B[Blen-(i+1)]);
			}
			int add = 0;
			
			for (int i = 0; i < Alen; i++) {
				int result = Anums[i] + Bnums[i] + add;
				
				if (result > 9) {
					add = 1;
					Anums[i] = result - 10;
				}else {
					add = 0;
					Anums[i] = result;
				}
			}
			
			bw.write("#"+tc+" ");
			
			if (add == 1) {
				bw.write("1");
			}
			for (int i = Alen-1; i >= 0; i--) {
				bw.write(String.valueOf(Anums[i]));
			}
			bw.write("\n");

		}
		bw.flush();
		bw.close();
	}

}
