import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Solution {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int T = Integer.parseInt(bf.readLine());
		
		for (int tc = 1; tc<=T; tc++) {
			StringTokenizer st = new StringTokenizer(bf.readLine());
			
//			N 명으로 구성된 조 K 개 
			int N = Integer.parseInt(st.nextToken());
			int K = Integer.parseInt(st.nextToken());
			
			int cnt = 1;
			
			int list[] = new int[K];
			
			while (cnt <= N) {
				if (cnt%2 == 1) {
					for (int i = 0; i < K; i++) {
						list[i] += ((cnt-1)*K)+i+1;
					}
				}else {
					for (int i = 0; i < K ;i++) {
						list[K-1-i] += ((cnt-1)*K)+i+1;
					}
				}
				cnt++;
			}
			
			bw.write("#"+tc);
			
			for (int i = 0; i<K; i++) {
				bw.write(" "+list[i]);
			}
			bw.write("\n");
		}
		bw.flush();
		bw.close();
	}
}
