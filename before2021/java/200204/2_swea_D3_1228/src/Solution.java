import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Solution {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		for (int tc = 1; tc < 11; tc++) {
			int N = Integer.parseInt(bf.readLine());
			
			
			StringTokenizer st = new StringTokenizer(bf.readLine());
			
			ArrayList<Integer> pass = new ArrayList<Integer>();
			
			for (int i = 0; i < N; i++) {
				pass.add(Integer.parseInt(st.nextToken()));
			}
			
			int commandCnt = Integer.parseInt(bf.readLine());
			int cnt = 0;
			StringTokenizer st2 = new StringTokenizer(bf.readLine());
			
			while (cnt<commandCnt) {
				st2.nextToken();
				int position = Integer.parseInt(st2.nextToken())-1;
				int size = Integer.parseInt(st2.nextToken());
				
				for (int j = 0; j<size; j++) {
					position++;
					int insertNum = Integer.parseInt(st2.nextToken());
					
					pass.add(position, insertNum);
					
				}
				
				
				cnt++;
			}
			
			System.out.print("#"+tc);
			for(int i = 0; i<10; i++) {
				System.out.print(" "+pass.get(i));
			}
			System.out.print("\n");
			
		}
	}
}
