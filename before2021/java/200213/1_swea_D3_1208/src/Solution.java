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
		
		
		for (int tc = 1; tc <= 10; tc++) {
			int N = Integer.parseInt(bf.readLine());
			
			ArrayList<Integer> maps = new ArrayList<Integer>();
			
			StringTokenizer st = new StringTokenizer(bf.readLine());
			
			for (int i = 0; i<100; i++) {
				maps.add(Integer.parseInt(st.nextToken()));
			}
			
			for (int i = 0; i < N; i++) {
				int max = Collections.max(maps);
				int min = Collections.min(maps);
				
				int max_index = maps.indexOf(max);
				int min_index = maps.indexOf(min);
				
				maps.set(max_index, max-1);
				maps.set(min_index, min+1);
;			}
			
			int result = Collections.max(maps)-Collections.min(maps);
			
			bw.write("#"+tc+" "+result+"\n");
			
		}
		bw.flush();
		bw.close();
	}
}
