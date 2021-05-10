import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Solution {
	public static void main(String[] args) throws IOException{
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int T = Integer.parseInt(bf.readLine());
		
		for (int tc = 1; tc <= T; tc++) {
			int N = Integer.parseInt(bf.readLine());
			int result = 0;
			int[] list = new int[N];
			
			for (int i = 0; i < N; i++) {
				list[i] = Integer.parseInt(bf.readLine());
			}
			
			for (int i = 1; i < N; i++) {
				if (list[i] == 0) {
					continue;
				}
				
				int check = list[i] - 1;
				
				for (int j = i+1; j < N; j++) {
					if (list[j] == 0) {
						continue;
					}
					if ((list[j]-1)%check == 0) {
						list[j] = 0;
					}
				}
			}
			
			for (int i = 1; i < N; i++) {
				if (list[i] != 0) {
					result++;
				}
			}
			
			bw.write("#"+tc+" "+result+"\n");
			
		}
		bw.flush();
		bw.close();
	}
}
