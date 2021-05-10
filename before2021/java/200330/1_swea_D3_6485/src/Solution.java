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
		
		for (int tc = 1; tc <= T; tc++) {
			int N = Integer.parseInt(bf.readLine());
			
			int[][] busList = new int[N][2];
			
			StringTokenizer st;
			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(bf.readLine());
				busList[i][0] = Integer.parseInt(st.nextToken());
				busList[i][1] = Integer.parseInt(st.nextToken());
			}
			
			
			int P = Integer.parseInt(bf.readLine());
			int[] busStop = new int[5001];
			
			
			
			for (int i = 0; i < N; i++) {
				for (int j = busList[i][0]; j <= busList[i][1]; j++) {
					busStop[j]++;
				}
				
			}
			
			bw.write("#"+tc);
			for (int i = 0; i < P; i++) {
				int j = Integer.parseInt(bf.readLine());
				bw.write(" "+busStop[j]);
			}
			
			bw.write("\n");
			
		}
		bw.flush();
		bw.close();
		
	}
}
