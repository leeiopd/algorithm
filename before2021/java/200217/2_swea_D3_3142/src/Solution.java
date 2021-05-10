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
			int N = Integer.parseInt(st.nextToken());
			int M = Integer.parseInt(st.nextToken());
			
			int uni = 0;
			int twin = 0;
			
			while(true){
				if (N < 2*M) {
					uni++;
					N--;
					M--;
					continue;
				}
				else {
					twin = M;
					break;
				}
			}
			
			bw.write("#"+tc+" "+uni+" "+twin+"\n");
		}
		bw.flush();
		bw.close();
	}
}
