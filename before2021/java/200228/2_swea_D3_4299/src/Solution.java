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
			
			int D = Integer.parseInt(st.nextToken());
			int H = Integer.parseInt(st.nextToken());
			int M = Integer.parseInt(st.nextToken());
			int breakTime = ((D*24)*60) + (H*60) + M;
			
			
			int setTime = ((11*24)*60) + (11*60) + 11;
			
			int result = breakTime - setTime;
			
			if (result < 0) {
				result = -1;
			}
			
			bw.write("#"+tc+" "+result+"\n");
		}
		bw.flush();
		bw.close();
	}
}
