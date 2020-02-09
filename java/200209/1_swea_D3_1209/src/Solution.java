import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Solution {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
	
		for (int tc = 1; tc <= 10; tc++) {
			bf.readLine();
			int [][] maps = new int[100][100];
			
			
//			100x100 input 저장
			for (int i = 0; i < 100; i++) {
				StringTokenizer st = new StringTokenizer(bf.readLine());
				for (int j = 0; j < 100; j++) {
					maps[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			
			int max = 0;
			
//			가로/세로 합
			for (int y = 0; y < 100; y++) {
				int add_row = 0;
				int add_col = 0;
				for (int x = 0; x < 100; x++) {
					add_row += maps[y][x];
					add_col += maps[x][y];
				}
				if (add_row > max) {
					max = add_row;
				}
				if (add_col > max) {
					max = add_col;
				}
			}
			
			
//			대각선 계산
			int add_RtToLb = 0;
			int add_LtToRb = 0;
			for (int i = 0; i<100; i++) {
				add_RtToLb += maps[i][i];
				add_LtToRb += maps[i][99-i];
			}
			
			if (add_RtToLb > max) {
				max = add_RtToLb;
			}
			
			if (add_LtToRb > max) {
				max = add_LtToRb;
			}
			
			bw.write("#"+tc+" "+max+"\n");
		}
		bw.flush();
		bw.close();
	}
}
