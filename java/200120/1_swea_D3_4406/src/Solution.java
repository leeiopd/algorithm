import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Solution {
	public static void main(String[] args) throws Exception {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		int T = Integer.parseInt(bf.readLine());
	
		for (int tc = 1; tc <= T; tc++) {
			String str = bf.readLine();
			sb.append("#"+tc+" ");
			for (int i = 0; i < str.length(); i++) {
				char check = str.charAt(i);

				if (check == 'a'||check == 'e' ||check == 'i' ||check == 'o' || check == 'u' ) {
					continue;
				}
				sb.append(check);
			}
			sb.append("\n");
			
		}
		System.out.println(sb.toString());
	}
}
