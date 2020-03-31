import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Solution {
	public static void main(String[] args) throws IOException{
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));


		HashMap<String, Integer> check = new HashMap<String, Integer>();

		check.put("A", 1);
		check.put("B", 2);
		check.put("D", 1);
		check.put("O", 1);
		check.put("P", 1);
		check.put("Q", 1);
		check.put("R", 1);


		int T = Integer.parseInt(bf.readLine());

		for (int tc = 1; tc<=T; tc++) {
			StringTokenizer st = new StringTokenizer(bf.readLine());
			String[] A = st.nextToken().split("");
			String[] B = st.nextToken().split("");

			String result = "SAME";

			if (A.length != B.length) {
				result = "DIFF";
			}else {

				for (int i = 0; i < A.length; i++) {
					if (check.containsKey(A[i]) && !check.containsKey(B[i])){
						result = "DIFF";
						break;
					}else if(!check.containsKey(A[i]) && check.containsKey(B[i])) {
						result = "DIFF";
						break;
					}

					if (check.containsKey(A[i]) && check.containsKey(B[i])) {
						if (check.get(A[i]) != check.get(B[i])) {
							result = "DIFF";
							break;
						}
					}
				}
			}

			bw.write("#"+tc+" "+result+"\n");
		}
		bw.flush();
		bw.close();
	}
}
