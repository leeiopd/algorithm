import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
	public static void main(String[] args) throws Exception {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		int N,M, result;
		
		for(int tc=1; tc <11; tc++) {
			bf.readLine();
			
			StringTokenizer st = new StringTokenizer(bf.readLine());
			N = Integer.parseInt(st.nextToken());
			M = Integer.parseInt(st.nextToken());
			
			result = 1;
			
			for (int i = 0; i<M; i++) {
				result *= N;
			}
			
			System.out.println("#"+tc+" "+result);
		}
		
		
	}
}
