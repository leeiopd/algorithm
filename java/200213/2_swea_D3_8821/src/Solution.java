import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;

public class Solution {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int T = Integer.parseInt(bf.readLine());

		for (int tc = 1; tc <= T; tc++) {
			String[] input = bf.readLine().split("");
			int[] nums = new int[10];
			int result = 0;
			
			for (int i = 0; i < input.length; i++) {
				nums[Integer.parseInt(input[i])]++;
			}
			
			for (int i = 0; i < 10; i++) {
				if (nums[i]%2 == 1) {
					result++;
				}
			}
			
			bw.write("#"+tc+" "+result+"\n");
			
		}
		bw.flush();
		bw.close();
	}
}
