import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Solution {
	static ArrayList<Integer> G;
	static ArrayList<Integer> I;
	
	static int[] mem;
	
	static int win;
	static int lose;
	
	
	public static void main(String[] args) throws IOException{
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int T = Integer.parseInt(bf.readLine());
		
		for (int tc = 1; tc <= T; tc++) {
			StringTokenizer st = new StringTokenizer(bf.readLine());
			
			G = new ArrayList<Integer>();
			
			for (int i = 0; i < 9; i++) {
				G.add(Integer.parseInt(st.nextToken()));
			}
			
			I = new ArrayList<Integer>();
			for (int i = 1; i <= 18; i++) {
				if (!G.contains(i)) {
					I.add(i);
				}
			}
			
			int[] permList = new int[9];
			mem  = new int[9];
			
			win = 0;
			lose = 0;
			
			fnc(0, permList);
			
			bw.write("#"+tc+" "+win+" "+lose+"\n");
			
			
		}
		bw.flush();
		bw.close();
	}
	
	static void fnc(int cnt, int[] permList) {
		if (cnt == 9) {
			int g = 0;
			int y = 0;
			for (int i = 0; i < 9; i++) {
				if (I.get(permList[i]) > G.get(i) ) {
					y += I.get(permList[i]);
					y += G.get(i);
				}else {
					g += I.get(permList[i]);
					g += G.get(i);
				}
			}
			if (g > y) {
				win++;
			}else {
				lose++;
			}
			return;
		}
		
		for (int i = 0; i < 9; i++) {
			if (mem[i] == 0) {
				permList[cnt] = i;
				mem[i] = 1;
				fnc(cnt+1, permList);
				mem[i] = 0;
			}
		}
	}
}
