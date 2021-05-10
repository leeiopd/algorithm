import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Solution {
	public static void main(String[] args) throws Exception {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(bf.readLine());
		
		for (int tc = 1; tc <= T; tc++) {
			int N = Integer.parseInt(bf.readLine());
			
			StringTokenizer st = new StringTokenizer(bf.readLine());
			
			ArrayList<Integer> list = new ArrayList<Integer>();
			
			for (int i = 0; i < N; i++) {
				list.add(Integer.parseInt(st.nextToken()));
			}
			
			int Max = 0;
			int Min = 0;
			int temp = 0;
			for (int i = 1; i < N; i++) {
				temp = list.get(i) - list.get(i-1);
				
//				올라갈 때 
				if (temp > 0) {
					if (temp > Max) {
						Max = temp;
					}
				}
				
//				내려갈 때 
				if (temp < 0) {
					temp *= -1;
					if (temp > Min) {
						Min = temp;
					}
					
				}
		
			}
			
			System.out.println("#"+tc+" "+Max+" "+Min);
		}
	}
}
