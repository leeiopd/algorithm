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
			StringTokenizer st = new StringTokenizer(bf.readLine());
			int N = Integer.parseInt(st.nextToken());
			int K = Integer.parseInt(st.nextToken());
			
			st = new StringTokenizer(bf.readLine());
			
			ArrayList<Integer> list = new ArrayList<Integer>();
			
			for (int i = 0; i < N; i++) {
				list.add(Integer.parseInt(st.nextToken()));
			}
			
			Collections.sort(list);
			Collections.reverse(list);
			
			int result = 0;
			
			for (int i = 0; i < K; i++) {
				result += list.get(i);
			}
			
			bw.write("#"+tc+" "+result+"\n");
		}
		bw.flush();
		bw.close();
	}
}
