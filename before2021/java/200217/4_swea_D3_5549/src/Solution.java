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
			String N = bf.readLine();
			
			bw.write("#"+tc+" ");
			
			
			if (Integer.parseInt(String.valueOf(N.charAt(N.length()-1)))%2 == 0) {
				bw.write("Even\n");
			}
			else {
				bw.write("Odd\n");
			}
			
			
			
		}
		bw.flush();
		bw.close();
	}
}
