import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashMap;


public class Solution {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int T = Integer.parseInt(bf.readLine());
		
		for (int tc = 1; tc <= T; tc++) {
			String cards = bf.readLine();
			
			HashMap<String, int[]> map = new HashMap<String, int[]>();
			
			map.put("S", new int[14]);
			map.put("D", new int[14]);
			map.put("H", new int[14]);
			map.put("C", new int[14]);
			
			boolean flag = true;
			
			for (int i = 0; i < (cards.length()/3); i++) {
				String card = cards.substring(i*3, (i+1)*3);
				String shape = card.substring(0, 1);
				int num = Integer.parseInt(card.substring(1));
				
				int[] cardList = map.get(shape);
				
				if (cardList[num] != 0) {
					flag = false;
					break;
				}else {
					cardList[num] ++;
					map.replace(shape, cardList);
				}
			}
			
			if(flag) {
				int S = 13;
				int D = 13;
				int H = 13;
				int C = 13;
				
				for (int i = 0; i < 14; i++) {
					S -= map.get("S")[i];
					D -= map.get("D")[i];
					H -= map.get("H")[i];
					C -= map.get("C")[i];
				}
				bw.write("#"+tc+" "+S+" "+D+" "+H+" "+C+"\n");
			}else {
				bw.write("#"+tc+" ERROR\n");
				
			}
		}
		bw.flush();
		bw.close();
	}
}
