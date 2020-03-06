import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashMap;
public class Solution {
	public static int[] check;
	public static HashMap<String, Integer> map = new HashMap<String, Integer>();
	public static int N;
	public static int result;
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		map.put("A", 0);
		map.put("B", 1);
		map.put("C", 2);
		map.put("D", 3);
		map.put("E", 4);
		map.put("F", 5);
		map.put("G", 6);
		map.put("H", 7);
		map.put("I", 8);
		map.put("J", 9);
		map.put("K", 10);
		map.put("L", 11);
		map.put("M", 12);
		map.put("N", 13);
		map.put("O", 14);
		map.put("P", 15);
		map.put("Q", 16);
		map.put("R", 17);
		map.put("S", 18);
		map.put("T", 19);
		map.put("U", 20);
		map.put("V", 21);
		map.put("W", 22);
		map.put("X", 23);
		map.put("Y", 24);
		map.put("Z", 25);
		int T = Integer.parseInt(bf.readLine());
		for (int tc = 1;  tc <= T; tc++) {
			N = Integer.parseInt(bf.readLine());
			result = 0;
			check = new int[26];
			for (int i = 0; i < N; i++) {
				check[map.get(String.valueOf(bf.readLine().charAt(0)))]++;
			}
			for (int i = 0; i < 26; i++) {
				if (check[i] == 0) {
					break;
				}
				result ++;
			}
			bw.write("#"+tc+" "+result+"\n");
		}
		bw.flush();
		bw.close();
	}
}
