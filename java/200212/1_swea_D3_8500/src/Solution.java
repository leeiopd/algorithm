import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(bf.readLine());
		
		for (int tc = 1; tc <= 10; tc++) {
			int N = Integer.parseInt(bf.readLine());
			
			StringTokenizer st = new StringTokenizer(bf.readLine());
			
			int[] nums = new int[N];
			
			for (int i = 0; i < N; i++) {
				nums[i] = Integer.parseInt(st.nextToken());
			}
			
			sol(nums, N);
			
		}
	}
	
	public static int sol(int[] input, int N) {
		int result = 0;
		for (int i = 0; i < N; i++) {
			num = Integer.parseInt(st.nextToken());
			
			if (i == 0) {
				result += num;
				temp = num;
				continue;
			}
			
			if (temp < num) {
				result += num;
				temp = num;
			}
			else {
				result += temp;
				temp = num;
			}
		}
		result += num+N;
		
		
		System.out.println(result);
		
	
	}
}
