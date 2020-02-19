import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Solution {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int T = Integer.parseInt(bf.readLine());
		int[] dayOfMonth = {0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
		HashMap<Integer, Integer> numOfweek = new HashMap<Integer, Integer>();
		numOfweek.put(0, 4);
		numOfweek.put(1, 5);
		numOfweek.put(2, 6);
		numOfweek.put(3, 0);
		numOfweek.put(4, 1);
		numOfweek.put(5, 2);
		numOfweek.put(6, 3);
		
		for (int tc = 1; tc <= T; tc++){
			StringTokenizer st = new StringTokenizer(bf.readLine());
			int m = Integer.parseInt(st.nextToken());
			int d = Integer.parseInt(st.nextToken());
			
			int dayDiff = 0;
			
			for (int i = 0; i <= m-1; i++) {
				dayDiff += dayOfMonth[i];
			}
			
			dayDiff += d-1;
			
			bw.write("#"+tc+" "+numOfweek.get(dayDiff%7)+"\n");
		}
		bw.flush();
		bw.close();
	}
}
