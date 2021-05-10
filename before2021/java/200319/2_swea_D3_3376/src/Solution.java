import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Solution {
	static long[] list = new long[101];
	public static void main(String[] args) throws IOException{
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int T = Integer.parseInt(bf.readLine());
		
		list[1] = 1;
		list[2] = 1;
		list[3] = 1;
		list[4] = 2;
		list[5] = 2;
		
		for (int i = 6; i<101; i++) {
			list[i] = list[i-3] + list[i-2];
		}
		
		for (int tc = 1; tc <= T; tc++) {
			int N = Integer.parseInt(bf.readLine());
			
			bw.write("#"+tc+" "+list[N]+"\n");
		}
		bw.flush();
		bw.close();
	}
}
