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
			
			float result = 0;
			StringTokenizer st = null;
			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(bf.readLine());
				
				float p = Float.parseFloat(st.nextToken());
				float x = Float.parseFloat(st.nextToken());
				
				result += p * x;
			}
			bw.write("#"+tc+" "+result+"\n");
		}
		bw.flush();
		bw.close();
	}
}
