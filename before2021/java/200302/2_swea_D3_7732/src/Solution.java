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
			String[] nowString = bf.readLine().split(":");
			int[] now = new int[3];
			
			String[] atString = bf.readLine().split(":");
			int[] at = new int[3];
			
			for (int i = 0; i < 3; i++) {
				now[i] = Integer.parseInt(nowString[i]);
				at[i] = Integer.parseInt(atString[i]);
			}
			
			
			int[] result = new int[3];
			
			for (int i = 2; i > -1; i--) {
				result[i] = at[i] - now[i];
			}
			
			bw.write("#"+tc+" ");
			
			if (result[2] < 0) {
				result[2] += 60;
				result[1] -= 1;
			}
			
			
			if (result[1] < 0 ) {
				result[1] += 60;
				result[0] -= 1;
			}
			
			if (result[0] < 0) {
				result[0] += 24;
			}
			
			
			if (result[0] < 10) {
				bw.write("0"+result[0]+":");
			}
			else {
				bw.write(result[0]+":");
			}
			if (result[1] < 10) {
				bw.write("0"+result[1]+":");
			}
			else {
				bw.write(result[1]+":");
			}
			if (result[2] < 10) {
				bw.write("0"+result[2]+"\n");
			}
			else {
				bw.write(result[2]+"\n");
			}
			
		}
		bw.flush();
		bw.close();
	}
}
