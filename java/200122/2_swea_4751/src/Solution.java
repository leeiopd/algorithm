import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Solution {
	public static void main(String[] args) throws Exception{
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int T = Integer.parseInt(bf.readLine());
		
		for (int tc = 1; tc <= T; tc++) {
			StringBuilder sb = new StringBuilder();
			String input = bf.readLine();
			int N = input.length();
			
			for (int i = 0; i < N ; i++) {
				sb.append("..#.");
				
			}
			sb.append(".\n");
			
			
			for (int i = 0; i < N; i++) {
				sb.append(".#.#");
			}
			sb.append(".\n");
			
			sb.append("#");		
			for (int i = 0; i < N; i++) {
				sb.append("."+input.charAt(i)+".#");
			}
			sb.append("\n");
			
			for (int i = 0; i < N ; i++) {
				sb.append(".#.#");
				
			}
			sb.append(".\n");
			
			for (int i = 0; i < N; i++) {
				sb.append("..#.");
			}
			sb.append(".\n");
			
			bw.write(sb.toString());
		}
		bw.close();
	}
}
