import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashMap;

public class Solution {
	public static int N;
	public static String[] words;
	public static boolean[] choice;
	public static int[] alphaMatch;
	public static HashMap<String, Integer> map = new HashMap<String, Integer>();
	public static int result;

	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		map.put("a", 1);
		map.put("b", 2);
		map.put("c", 3);
		map.put("d", 4);
		map.put("e", 5);
		map.put("f", 6);
		map.put("g", 7);
		map.put("h", 8);
		map.put("i", 9);
		map.put("j", 10);
		map.put("k", 11);
		map.put("l", 12);
		map.put("m", 13);
		map.put("n", 14);
		map.put("o", 15);
		map.put("p", 16);
		map.put("q", 17);
		map.put("r", 18);
		map.put("s", 19);
		map.put("t", 20);
		map.put("u", 21);
		map.put("v", 22);
		map.put("w", 23);
		map.put("x", 24);
		map.put("y", 25);
		map.put("z", 26);
		
		int T = Integer.parseInt(bf.readLine());

		for (int tc = 1; tc <= T;  tc++) {
			N  = Integer.parseInt(bf.readLine());
			words = new String[N];
			choice = new boolean[N];
			result = 0;
			
			for (int i = 0; i < N; i++) {
				words[i] = bf.readLine();
			}

			fnc(1, choice);
			choice[0] = true;
			fnc(1, choice);
			
			bw.write("#"+tc+" "+result+"\n");


		}
		bw.flush();
		bw.close();
	}

	public static void fnc(int cnt, boolean[] choice) {
		if (cnt == N) {
			reset();
			String temp = "";
			for (int i = 0; i < N; i++) {
				if (choice[i]) {
					temp += words[i];
				}
			}
			for (int i = 0; i < temp.length(); i++) {
				alphaMatch[map.get(String.valueOf(temp.charAt(i)))]++;
			}
			
			for (int i = 1; i < 27; i++) {
				if(alphaMatch[i] == 0) {
					return;
				}
			}
			result++;
			return;
		}
		fnc(cnt+1,choice);
		choice[cnt] = true;
		fnc(cnt+1,choice);
		choice[cnt] = false;
	}
	
	public static void reset() {
		alphaMatch = new int[27];
		return;
	}
}
