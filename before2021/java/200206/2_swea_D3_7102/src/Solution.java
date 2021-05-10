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
			int M = Integer.parseInt(st.nextToken());
			
			ArrayList<Integer> list = new ArrayList<Integer>();
			
			for (int i = 0; i <= M+N; i++) {
				list.add(0);
			}
			
			for (int f  = 1; f <= N ; f++) {
				for (int s = 1; s <= M ; s++) {
					list.set(f+s, list.get(f+s)+1);
				}
			}
			
			int max = Collections.max(list);
			
			bw.write("#"+tc);
			
			for (int i = 0; i <= M+N; i++) {
				if (list.get(i) == max) {
					bw.write(" "+i);
				}
			}
			bw.write("\n");
			
		}
		bw.flush();
		bw.close();
		
	}
}
