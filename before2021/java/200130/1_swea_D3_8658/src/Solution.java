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
			
			int Max = 0;
			int Min = 100;
			
			for (int i = 0; i < 10; i++) {
				String num = st.nextToken();
				
				int temp = 0;
				
				for (int j = 0; j < num.length(); j++) {
					temp += Integer.parseInt(String.valueOf(num.charAt(j)));
				}
				
				if (temp > Max) {
					Max = temp;
				}
				
				if (temp < Min) {
					Min = temp;
				}
			}
			
			System.out.println("#"+tc+" "+Max+" "+Min);
		}
	}
}
