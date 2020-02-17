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
			String[] inputs = bf.readLine().split(" ");
			
			
			bw.write("#"+tc+" ");
			
			for (int i = 0; i < inputs.length; i++) {
				String temp = inputs[i].toUpperCase();
				bw.write(temp.codePointAt(0));
			}
			bw.write("\n");
		}
		bw.flush();
		bw.close();
	}
}
