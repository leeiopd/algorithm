import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class Solution {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int T = Integer.parseInt(bf.readLine());
		
		for (int tc = 1; tc <= T; tc++) {
			int N = Integer.parseInt(bf.readLine());
			
			StringTokenizer st = new StringTokenizer(bf.readLine());
			
			ArrayList<Integer> nums = new ArrayList<Integer>();
			
			for (int i = 0; i < N; i++) {
				nums.add(Integer.parseInt(st.nextToken()));
			}
			
			Collections.sort(nums);
			
			int result = 0;
			for (int i = 0; i<N; i++) {
				result += nums.get(i);
			}
			
			result += nums.get(N-1) + N;
			
			bw.write("#"+tc+" "+result+"\n");
		}
		
		bw.flush();
		bw.close();
	}
}
