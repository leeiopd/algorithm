import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
	public static void main(String[] args) throws Exception{
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(bf.readLine());
		
		for (int tc = 1; tc <= T; tc++) {
			String[] MandN = bf.readLine().split(" ");
			int M = Integer.parseInt(MandN[0]);
			int N = Integer.parseInt(MandN[1]);
			
			int[] nums = new int[M];
			
			int Max = 0;
			
			
			for (int y = 0; y<M; y++) {
				StringTokenizer st = new StringTokenizer(bf.readLine());
				int temp = 0;
				for (int x = 0; x<N; x++) {
					temp += Integer.parseInt(st.nextToken());
				}
				nums[y] = temp;
				
				if (temp > Max) {
					Max = temp;
				}
			}
			
			
			int result = 0;
			
			for (int y = 0; y<M; y++) {
				if (nums[y] == Max) {
					result++;
				}
			}
			
			System.out.println("#"+tc+" "+result+" "+Max);
			
		}
	}
}
