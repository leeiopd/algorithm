import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;

public class Solution {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int T = Integer.parseInt(bf.readLine());

		for (int tc = 1; tc <= T; tc++) {
			String words = bf.readLine();

			ArrayList<Integer> list = new ArrayList<Integer>();

			for (int i = 0; i < words.length(); i++) {
				if (words.charAt(i) == 'w'||words.charAt(i) == 'n') {
					if (words.charAt(i) == 'w') {
						list.add(90);
					}else { 
						list.add(-90);
					}
				}
			}

			int L = list.size();

			int mom = (int)Math.pow(2, L-1);
			int son = 90 * mom;
			
			
			if (list.get(L-1) < 0) {
				son = 0;
			}

			int cnt = 1;

			for (int i = 0; i < L-1; i++) {
				son += list.get(i)*cnt;
				cnt *= 2;
			}

			while (true) {
				if (mom == 1 || son % 2 != 0) {
					break;
				}

				mom /= 2;
				son /= 2;
			}
			
			
			bw.write("#"+tc+" "+son);
			if (mom == 1) {
				bw.write("\n");
			}else {
				bw.write("/"+mom+"\n");
			}
		}
		bw.flush();
		bw.close();
	}
}
