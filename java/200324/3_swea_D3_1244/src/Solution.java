import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Solution {
	static int N;
	static String[]  list;
	static int result;
	static int L;
	public static void main(String[] args) throws IOException{
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int T = Integer.parseInt(bf.readLine());

		for (int tc = 1; tc <= T; tc++) {
			StringTokenizer st = new StringTokenizer(bf.readLine());

			String nums = st.nextToken();
			N = Integer.parseInt(st.nextToken());

			list = new String[nums.length()];

			for (int i = 0; i < nums.length(); i++) {
				list[i] = String.valueOf(nums.charAt(i));
			}

			L = list.length;

			if (L < N) {

			}

			bw.write("#"+tc+" "+result+"\n");

		}
		bw.flush();
		bw.close();
	}

	static void fnc(int cnt) {
		if (N == cnt) {
			return;
		}


		int maxPosition = 0;
		int max = 0;
		for (int j = cnt+1; j < L; j++) {
			if (Integer.parseInt(list[cnt]) > max){
				max = Integer.parseInt(list[cnt]);
				maxPosition = j;
			}
		}

		swap(cnt, maxPosition);
		fnc(cnt+1);



	}

	static void swap(int i, int j) {
		String temp = list[i];
		list[i] = list[j];
		list[j] = temp;

		return;
	}

}
