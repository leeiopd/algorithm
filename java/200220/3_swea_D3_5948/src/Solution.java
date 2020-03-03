import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class Solution {
	public static int N;
	public static ArrayList<Integer> list;
	public static int[] nums;
	public static int[] mem;
	
	
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int T = Integer.parseInt(bf.readLine());
		
		for (int tc = 1; tc <= T; tc++) {
			StringTokenizer st = new StringTokenizer(bf.readLine());
			
			N = st.countTokens();
			
			list = new ArrayList<Integer>();
			
			nums = new int[N];
			mem = new int[N];
			
			for (int i = 0; i < N; i++) {
				nums[i] = Integer.parseInt(st.nextToken());
			}
			
			game(0, 0, mem);
			
			Collections.sort(list);
			Collections.reverse(list);
			
			
			bw.write("#"+tc+" "+list.get(4)+"\n");
		}
		bw.flush();
		bw.close();
	}
	
	public static void game(int cnt, int add, int[] mem) {
		if (cnt == 3) {
			if (!list.contains(add)) {
				list.add(add);
			}
			return;
		}
		
		for (int i = 0; i < N; i++) {
			if (mem[i] == 0) {
				mem[i] = 1;
				game(cnt+1, add+nums[i], mem);
				mem[i] = 0;
			}
		}
	}
}
