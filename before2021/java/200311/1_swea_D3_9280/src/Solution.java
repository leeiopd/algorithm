import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Solution {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int T = Integer.parseInt(bf.readLine());

		for (int tc = 1; tc<= T; tc++) {
			StringTokenizer st = new StringTokenizer(bf.readLine());

			int n = Integer.parseInt(st.nextToken());
			int m = Integer.parseInt(st.nextToken());

			int[] parkZone = new int[n+1];
			
			int result = 0;

			//			주차 공간별 단위 무게당 요금
			HashMap<Integer, Integer> R = new HashMap<Integer, Integer>();

			// 			차량 번호당 차량 무게
			HashMap<Integer, Integer> W = new HashMap<Integer, Integer>();

			for (int i = 1; i < n+1; i++) {
				R.put(i, Integer.parseInt(bf.readLine()));
			}

			for (int i = 1; i < m+1; i++) {
				W.put(i, Integer.parseInt(bf.readLine()));
			}

			ArrayList<Integer> stay = new ArrayList<Integer>();

			for (int i = 0; i < 2*m; i++) {
				if (!stay.isEmpty()) {
					int zone = 0;
					for (int j = 1; j < n+1; j++) {
						if (parkZone[j] == 0) {
							zone = j;
						}
					}

					if (zone != 0) {
						parkZone[zone] = stay.get(0);
						stay.remove(0);
					}

				}
				int car = Integer.parseInt(bf.readLine());
				if (car > 0) {
					int zone = 0;

					for (int j = 1; j < n+1; j++) {
						if (parkZone[j] == 0) {
							zone = j;
							break;
						}
					}

					if (zone == 0) {
						stay.add(car);
						continue;
					}
					
					parkZone[zone] = car;
					
					
				} else {
					int zone = 0;
					car *= -1;

					for (int j = 1; j < n+1; j++) {
						if (parkZone[j] == car) {
							zone = j;
							break;
						}
					}
					
					parkZone[zone] = 0;
					
					result += (R.get(zone) * W.get(car));
					
				}



			}
			
			bw.write("#"+tc+" "+result+"\n");


		}
		bw.flush();
		bw.close();
	}
}
