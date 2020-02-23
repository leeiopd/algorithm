import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Solution {
	public static void main(String[] args) throws IOException {
		BufferedReader bf  = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw  = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int T = Integer.parseInt(bf.readLine());
		
		for (int tc = 1; tc <= T; tc++) {
			int N = Integer.parseInt(bf.readLine());
			
			String[] originStr = bf.readLine().split("");
			String[] copyStr = bf.readLine().split("");
			
			int result = 0;
			
			for (int i = 0; i < N; i++) {
				if (originStr[i].equals(copyStr[i])) {
					result++;
				}
			}
			
			bw.write("#"+tc+" "+result+"\n");
		}
		
		bw.flush();
		bw.close();
	}
}
