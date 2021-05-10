import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Solution {
	static int N;
	static int result;
	static int L;
	static ArrayList<String> set;
	public static void main(String[] args) throws IOException{
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int T = Integer.parseInt(bf.readLine());

		for (int tc = 1; tc <= T; tc++) {
			StringTokenizer st = new StringTokenizer(bf.readLine());

			String[] list = st.nextToken().split("");
			N = Integer.parseInt(st.nextToken());
			L = list.length;
			result = 0;
			set = new ArrayList<String>();

			fnc(0, 0, list);

			bw.write("#"+tc+" "+result+"\n");

		}
		bw.flush();
		bw.close();
	}

	static void fnc(int cnt, int cur, String[] list) {

		String num = "";
		for (int i = 0; i < L; i++) {
			num += list[i];
		}

		if (set.contains(""+num+cnt)) {
			return;
		}else {
			set.add(""+num+cnt);
		}

		if (N == cnt) {
			if(Integer.parseInt(num) > result) {
				result = Integer.parseInt(num);
			}
			return;
		}

		for (int i = cur; i < L; i++) {
			for (int j = i+1; j < L; j++) {
				swap(i, j, list);
				fnc(cnt+1, i, list);
				swap(i, j, list);			

			}

		}




	}

	static void swap(int i, int j, String[] list) {
		String temp = list[i];
		list[i] = list[j];
		list[j] = temp;

		return;
	}

}
