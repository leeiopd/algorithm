import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(bf.readLine());
		
		for (int tc = 1; tc <= T; tc++) {
			StringTokenizer st = new StringTokenizer(bf.readLine());
			
			int add = 0;
			
			for (int i = 0; i < 5; i++) {
				int temp = Integer.parseInt(st.nextToken());
				
				if (temp < 40) {
					add += 40;
				}
				else {
					add += temp;
				}
			}
			
			System.out.println("#"+tc+" "+add/5);
			
		}
	}
}
