import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Solution {
	static int N;
	static ArrayList<int[]> nums;
	static boolean[] visited;
	static int[] list;
	static long result;

	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int T = Integer.parseInt(bf.readLine());

		for (int tc = 1; tc <= T; tc++) {
			N = Integer.parseInt(bf.readLine());
			result = Long.MAX_VALUE;

			nums = new ArrayList<int[]>();
			StringTokenizer st;
			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(bf.readLine());
				int x = Integer.parseInt(st.nextToken());
				int y = Integer.parseInt(st.nextToken());

				int[] temp = {x, y}; 
				nums.add(temp);
			}

			visited = new boolean[N];
			list = new int[N];

			fnc(0, visited, list);
			bw.write("#"+tc+" "+result+"\n");
		}
		bw.flush();
		bw.close();

	}

	static void fnc(int cnt, boolean[] visited, int[] list) {
		if (cnt == N) {
			long V = 0;
			long addX = 0;
			long addY = 0;
			for (int i = 0; i < N; i++) {
				if (i%2==0) {
					addX += nums.get(list[i])[0];
					addY += nums.get(list[i])[1];
				}else {
					addX -= nums.get(list[i])[0];
					addY -= nums.get(list[i])[1];
				}
			}
			V = (addX * addX) + (addY * addY);
			if (V < result) {
				result = V;
			}
			return;
		}

		for (int i = 0; i < N; i++) {
			if(visited[i]) {
				continue;
			}

			visited[i] = true;
			list[cnt] = i;

			fnc(cnt+1, visited, list);

			visited[i] = false;
		}

	}
}