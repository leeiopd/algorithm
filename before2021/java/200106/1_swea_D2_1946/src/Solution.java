import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
	public static void main(String[] args) throws IOException{
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		int tc = Integer.parseInt(bf.readLine());
		int M;
		String alphabet, result;
		for (int i = 1; i <= tc; i++) {
			System.out.println("#"+i);
			int N = Integer.parseInt(bf.readLine());
			StringBuilder builder = new StringBuilder();
			for (int j = 0; j < N; j++) {
				StringTokenizer st = new StringTokenizer(bf.readLine());
				
				alphabet = st.nextToken();
				M = Integer.parseInt(st.nextToken());
				
				for (int x = 0; x < M; x++) {
					builder.append(alphabet);
				}
			}
			result = builder.toString();
			
			for (int j = 0; j < result.length(); j++) {
				System.out.print(result.charAt(j));
				if ((j+1)%10 == 0) {
					System.out.println();
				}
			}
			System.out.println();
		}
	}
}
