import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Solution {
	static int N;
	static int L;
	static int[][] bugerArg;
	static int result;
	public static void main(String[] args) throws IOException{
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int T = Integer.parseInt(bf.readLine());
		
		for (int tc = 1; tc <= T; tc++) {
			StringTokenizer st = new StringTokenizer(bf.readLine());
			
			N = Integer.parseInt(st.nextToken());
			L = Integer.parseInt(st.nextToken());
			
			bugerArg = new int[N][2];
			
			result = 0;
			
			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(bf.readLine());
				bugerArg[i][0] = Integer.parseInt(st.nextToken()); 
				bugerArg[i][1] = Integer.parseInt(st.nextToken()); 
			}
			
			int[] check = new int[N];
			perm(0, 0, 0);
			
			bw.write("#"+tc+" "+result+"\n");
		}
		bw.flush();
		bw.close();
	}
	
	static void perm(int cnt, int Cadd, int Tadd) {
		if(cnt == N) {
			if (Tadd > result) {
				result = Tadd;
			}
			return;
		}
		
		perm(cnt+1, Cadd, Tadd);
		if (Cadd + bugerArg[cnt][1] < L) {
			perm(cnt+1, Cadd+bugerArg[cnt][1], Tadd+bugerArg[cnt][0]);
		}
	}
}
