import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		for (int tc = 1; tc <= 10; tc++) {
			bf.readLine();
			
			String find = bf.readLine();
			
			String temp = bf.readLine();
			
			int result = 0;
			
			for (int i = 0; i <= temp.length()-find.length(); i++) {
				int cnt = 0;
				for (int j = 0; j < find.length(); j++) {
					if (find.charAt(j) == temp.charAt(i+j)) {
						cnt++;
					}
					else {
						break;
					}
				}
				if (cnt == find.length()) {
					result++;
				}
			}
			
			System.out.println("#"+tc+" "+result);
		}
	}
}
