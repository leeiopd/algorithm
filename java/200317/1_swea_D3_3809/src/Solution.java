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
			String temp = "";
			StringTokenizer st;
			
			
			while (true) {
				if (N == temp.length()) {
					break;
				}
				
				st = new StringTokenizer(bf.readLine());
				int L = st.countTokens();
				
				for (int i = 0; i < L; i++) {
					temp+=st.nextToken();
				}
			}
			
			int cnt = -1;
			boolean flag;
			int result = -1;
			
			while (true) {
				cnt++;
				
				String cntStr = String.valueOf(cnt);
				flag = false;
				for (int i = 0; i <= (N-cntStr.length()); i++) {
					String check = temp.substring(i, i+cntStr.length());
					if (check.equals(cntStr)) {
						flag = true;
						break;
					}
				}
				if (flag == false) {
					result = cnt;
					break;
				}
			}
			
			bw.write("#"+tc+" "+result+"\n");
		}
		bw.flush();
		bw.close();
	}
}
