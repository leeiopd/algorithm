import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution {
	public static void main(String[] args) throws IOException{
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

		for (int tc = 1; tc <= 10; tc++) {
			bf.readLine();

			String maps[][] = new String [100][];

			for (int i = 0; i < 100; i++) {
				String row[] = bf.readLine().split("");
				maps[i] = row;
			}

			int result = 0;

			for (int y = 0; y < 100; y++) {
				for (int start_x = 0 ; start_x < 100; start_x++) {
					String temp = "";
					for (int x = start_x; x < 100; x++) {
						temp += maps[y][x];
						StringBuffer sb = new StringBuffer(temp);
						String reversTemp = sb.reverse().toString();
						
						if (temp.equals(reversTemp)) {
							if (temp.length() > result) {
								result = temp.length();
							}
						}
					}
				}
			}
			for (int x = 0; x < 100; x++) {
				for (int start_y = 0 ; start_y < 100; start_y++) {
					String temp = "";
					
					for (int y = start_y; y < 100; y++) {
						temp += maps[y][x];
						StringBuffer sb = new StringBuffer(temp);
						String reversTemp = sb.reverse().toString();
						
						if (temp.equals(reversTemp)) {
							if (temp.length() > result) {
								result = temp.length();
							}
						}
					}
				}
			}
			System.out.println("#"+tc+" "+result);
		}
	}
}
