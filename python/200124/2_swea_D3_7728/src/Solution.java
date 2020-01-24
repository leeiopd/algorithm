import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Solution {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int T = Integer.parseInt(bf.readLine());
		
		for (int tc = 1; tc <= T; tc++) {
			String nums = bf.readLine();
			
			int[] check = new int[10];
			
			for (int i = 0; i < nums.length(); i++) {
				check[Integer.parseInt(String.valueOf(nums.charAt(i)))]++;
			}
			
			int result = 0;
			
			for (int i = 0; i < 10; i++) {
				if (check[i] > 0) {
					result++;
				}
			}
			
			bw.write("#"+tc+" "+result+"\n");
		}
		bw.close();
	}
}
