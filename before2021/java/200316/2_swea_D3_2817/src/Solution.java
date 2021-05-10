import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Solution {
	static int N;
	static int K;
	static int result;
	static ArrayList<Integer> nums;

	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int T = Integer.parseInt(bf.readLine());

		for (int tc = 1; tc <= T; tc++) {
			StringTokenizer st = new StringTokenizer(bf.readLine());

			N = Integer.parseInt(st.nextToken());
			K = Integer.parseInt(st.nextToken());

			nums = new ArrayList<Integer>();


			st = new StringTokenizer(bf.readLine());

			for (int i = 0; i < N; i++) {
				nums.add(Integer.parseInt(st.nextToken()));
			}


			result = 0;

			int[] list = new int[N];

			fnc(0, list, 0);


			bw.write("#"+tc+" "+result+"\n");
		}
		bw.flush();
		bw.close();
	}

	static void fnc(int cnt, int[] list, int add) {
		if (add > K) {
			return;
		}
		if (cnt == N) {
			if (add == K) {
				result++;
			}
			return;
		}


		fnc(cnt+1, list, add);
		list[cnt] = 1;
		fnc(cnt+1, list, add+nums.get(cnt));
		list[cnt] = 0;

	}


}
