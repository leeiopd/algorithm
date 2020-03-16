import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class Solution {
	static int N;
	static int M;
	static ArrayList<Integer> list = null;
	static int result;
	
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int T = Integer.parseInt(bf.readLine());
		
		for (int tc = 1; tc <= T; tc++) {
			StringTokenizer st = new StringTokenizer(bf.readLine());
			
			N = Integer.parseInt(st.nextToken());
			M = Integer.parseInt(st.nextToken());
		
			list = new ArrayList<Integer>();
			
			st = new StringTokenizer(bf.readLine());
			
			for (int i = 0; i < N; i++) {
				list.add(Integer.parseInt(st.nextToken()));
			}
			Collections.sort(list);
			Collections.reverse(list);
			
			result = -1;
			
			fnc();
			
			bw.write("#"+tc+" "+result+"\n");
			
		}
		bw.flush();
		bw.close();
		
	}
	
	static void fnc() {
		for (int i = 0; i < N; i++) {
			for (int j = i+1; j < N; j++) {
				int temp = list.get(i)+list.get(j);
				if (temp <= M && temp > result) {
					result = temp;
				}
			}
		}
	}
}