import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Solution {
	public static void main(String[] args) throws Exception{
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		for (int tc = 1; tc <= 10; tc++) {
			bf.readLine();
			
			StringTokenizer st = new StringTokenizer(bf.readLine());
			
			ArrayList<Integer> list = new ArrayList<> ();
			
			for (int i = 0; i < 8; i++) {
				list.add(Integer.parseInt(st.nextToken()));
			}
			
			int cnt = -1;
			int minusValue = 0;
			
			while (true) {
				cnt = (cnt+1)%8;
				minusValue = minusValue%5;
				minusValue++;
				
				
				int num = list.get(cnt);
				
				num -= minusValue;
				
				if (num <= 0) {
					list.set(cnt, 0);
					break;
				}
				list.set(cnt, num);
			}
			System.out.print("#"+tc+" ");
			
			for (int i = 0; i < 8; i++) {
				cnt = (cnt+1)%8;
				System.out.print(list.get(cnt)+" ");
				
			}
			System.out.println();
			
		}
	}
}
