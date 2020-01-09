import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution {
	public static int result;
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		for (int tc=1; tc < 11; tc++) {
			int N = Integer.parseInt(bf.readLine());
			result = 0;
			String maps[][] = new String[8][8];
			
			for (int y = 0; y < 8; y++) {
				String inputLine = bf.readLine();
				for (int x = 0; x < 8; x++) {
					maps[y][x] = String.valueOf(inputLine.charAt(x));
				}
			}
			
			colPalinCheck(maps, N);
			rowPalinCheck(maps, N);
			
			System.out.println("#"+tc+" "+result);
			
		}
	}
	
	public static void colPalinCheck(String maps[][], int N) {
		for (int start_y = 0; start_y < 8; start_y++) {
			for (int start_x = 0; start_x <= 8-N; start_x++) {
				StringBuilder builder = new StringBuilder();
				
				for (int j = 0; j < N; j++) {
					builder.append(maps[start_y][start_x+j]);
				}
				
				String check = builder.toString();
				String checkReverse = builder.reverse().toString();
				
				if (check.equals(checkReverse)) {
					result++;
				}
			}
		}
		return;
	}
	
	public static void rowPalinCheck(String maps[][], int N) {
		for (int start_x = 0; start_x < 8; start_x++) {
			for (int start_y = 0; start_y <= 8-N; start_y++) {
				StringBuilder builder = new StringBuilder();
				
				for (int j = 0; j < N; j++) {
					builder.append(maps[start_y+j][start_x]);
				}
				
				String check = builder.toString();
				String checkReverse = builder.reverse().toString();
				
				if (check.equals(checkReverse)) {
					result++;
				}
			}
		}
		return;
	}
}
