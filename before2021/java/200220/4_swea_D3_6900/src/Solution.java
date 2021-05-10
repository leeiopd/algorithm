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

		for (int tc = 1; tc <= T; tc++) {
			StringTokenizer st = new StringTokenizer(bf.readLine());

			int N = Integer.parseInt(st.nextToken());
			int M = Integer.parseInt(st.nextToken());
			
			int result = 0;
			
			HashMap<String, Integer> map = new HashMap<String, Integer>();
			
			String[] lottos = new String[N];
			
			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(bf.readLine());
				
				String lotto = st.nextToken();
				int price =  Integer.parseInt(st.nextToken());
				
				lottos[i] = lotto;
				map.put(lotto, price);
			}
			
			for (int i = 0; i < M; i++) {
				String myNum = bf.readLine();
				
				for (int j = 0; j < N; j++) {
					boolean flag = true;
					for (int k = 0; k < myNum.length(); k++) {
						if (lottos[j].charAt(k)=='*') {
							continue;
						}
						else if (lottos[j].charAt(k) != myNum.charAt(k)) {
							flag = false;
						}
					}
					if (flag) {
						result += map.get(lottos[j]);
					}
				}
			}
			
			bw.write("#"+tc+" "+result+"\n");
		}
		bw.flush();
		bw.close();
	}
}
