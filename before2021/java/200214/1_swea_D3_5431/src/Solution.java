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
			
			st = new StringTokenizer(bf.readLine());
			
			int[] nums = new int[N];
			
			for (int i = 0; i < M; i++) {
				nums[Integer.parseInt(st.nextToken())-1]++;
			}
			
			bw.write("#"+tc);
			
			for (int i = 0; i < N;i++) {
				if (nums[i]==0) {
					bw.write(" "+(i+1));
				}
			}
			bw.write("\n");
		}
		bw.flush();
		bw.close();
	}
}
