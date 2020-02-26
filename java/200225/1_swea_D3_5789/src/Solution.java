import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Solution {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int T = Integer.parseInt(bf.readLine());
		
		for (int tc = 1; tc <= T; tc++) {
			StringTokenizer st = new StringTokenizer(bf.readLine());
			int N = Integer.parseInt(st.nextToken());
			int Q = Integer.parseInt(st.nextToken());
			
			ArrayList<Integer> nums = new ArrayList<Integer>();
			
			for (int i = 0; i < N; i++) {
				nums.add(0);
			}
			
			
			for (int i = 0; i < Q; i++) {
				st = new StringTokenizer(bf.readLine());
				int L = Integer.parseInt(st.nextToken());
				int R = Integer.parseInt(st.nextToken());
				
				for (int j = L-1; j < R; j++ ) {
					nums.set(j, i+1);
				}
			}
			bw.write("#"+tc);
			
			for (int i = 0; i < N; i++) {
				bw.write(" "+nums.get(i));
			}
			bw.write("\n");
		}
		bw.flush();
		bw.close();
	}
}
