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

			int A = Integer.parseInt(st.nextToken());
			int B = Integer.parseInt(st.nextToken());
			int C = Integer.parseInt(st.nextToken());
			
			if (A > B) {
				int temp = A;
				A = B;
				B = temp;
			}
			
			int result = 0;

			while (C >= A) {
				C -= A;
				result ++;
			}
			
			while (C >= B) {
				C -= B;
				result ++;
			}
			
			
			bw.write("#"+tc+" "+result+"\n");
			
		}
		bw.flush();
		bw.close();
	}
}
