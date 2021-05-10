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
		
		for (int tc = 1; tc <= 10; tc++) {
			int N = Integer.parseInt(bf.readLine());
			
			ArrayList<String> nums = new ArrayList<String>();
			
			StringTokenizer st = new StringTokenizer(bf.readLine());
			
			for (int i = 0; i < N; i++) {
				nums.add(st.nextToken());
			}
			
			
			int M = Integer.parseInt(bf.readLine());
			
			st = new StringTokenizer(bf.readLine());
			
			while (st.countTokens() > 0){
				if (st.nextToken().equals("I"))	 {
					int x = Integer.parseInt(st.nextToken());
					int y = Integer.parseInt(st.nextToken());
					
					for (int i = 0; i < y; i++) {
						nums.add(x+i, st.nextToken());
					}
				}
				else {
					int x = Integer.parseInt(st.nextToken());
					int y = Integer.parseInt(st.nextToken());
					
					for (int i = 0; i < y; i++) {
						nums.remove(x);
					}
				}
			}
			
			bw.write("#"+tc);
			
			for (int i = 0; i < 10; i++) {
				bw.write(" "+nums.get(i));
			}
			bw.write("\n");
		}
		bw.flush();
		bw.close();
	}
}
