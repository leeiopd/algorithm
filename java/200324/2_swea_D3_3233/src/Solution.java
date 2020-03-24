import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Solution {
	public static void main(String[] args) throws IOException{
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int T = Integer.parseInt(bf.readLine());
		
		for (int tc = 1;  tc <= T; tc++) {
			StringTokenizer st = new StringTokenizer(bf.readLine());
			
			long A = Integer.parseInt(st.nextToken());
			long B = Integer.parseInt(st.nextToken());
			
			long diff = (long)A/B;
			
			bw.write("#"+tc+" "+(diff*diff)+"\n");
			
		}
		bw.flush();
		bw.close();
	}
}
