import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.io.BufferedReader;

public class Solution {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(bf.readLine());
		
		for (int tc = 1; tc <= T; tc++) {
			bf.readLine();
			int result = -1;
			int Max = 0;
			
			StringTokenizer st = new StringTokenizer(bf.readLine());
			
			int scores[] = new int[101];
			
			for (int i = 0; i < 1000; i++) {
				scores[Integer.parseInt(st.nextToken())]++;
			}
			
			for(int i =0; i < 101; i++) {
				if (scores[i] >= Max) {
					Max = scores[i];
					result = i;
				}
			}
			
			System.out.println("#"+tc+" "+result);
		}
		
	}
}
