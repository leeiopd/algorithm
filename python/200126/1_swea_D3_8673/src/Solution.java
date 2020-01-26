import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(bf.readLine());
		
		for (int tc = 1; tc <= T; tc++) {
			int N = Integer.parseInt(bf.readLine());
			
			int[] nums = new int[(int) Math.pow(2, N)];
			
			StringTokenizer st = new StringTokenizer(bf.readLine());
			
			for (int i = 0; i < nums.length; i++) {
				nums[i] = Integer.parseInt(st.nextToken());
			}
			
			int result = 0;
			
			while (N > 0) {
				N--;
				
				int[] temp = new int[(int) Math.pow(2, N)];
				
				for (int j = 0; j < ((int) Math.pow(2, N)); j++) {
					int f = nums[j*2];
					int b = nums[j*2+1];
					
					if (f > b) {
						temp[j] = f;
						result += (f-b);
					}
					else {
						temp[j] = b;
						result += (b-f);
					}
				}
				
				nums = temp;
			}
			
			System.out.println("#"+tc+" "+result);
		}
	}
}
