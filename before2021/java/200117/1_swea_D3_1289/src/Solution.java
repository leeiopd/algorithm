import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Solution {
	public static void main(String[] args) throws Exception {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

		int T = Integer.parseInt(bf.readLine());

		for (int tc=1; tc <= T; tc++) {
			int result = 0;
			String bits = bf.readLine();
			ArrayList<Integer> tempList = new ArrayList<>();
			ArrayList<Integer> initList = new ArrayList<>();
			for (int i = 0; i<bits.length(); i++) {
				tempList.add(Integer.parseInt(String.valueOf(bits.charAt(i))));
				initList.add(0);
			}

			for (int i = 0; i<bits.length(); i++) {
				if (tempList.get(i).equals(initList.get(i))) {
					continue;
				}
				else {
					result ++;
					int flag = 0;
					if (tempList.get(i)==1) {
						flag = 1;
					}
					for (int j = i; j < bits.length(); j++) {
						initList.set(j, flag);
					}
				}
			}
			
			System.out.println("#"+tc+" "+result);
		}

	}

}