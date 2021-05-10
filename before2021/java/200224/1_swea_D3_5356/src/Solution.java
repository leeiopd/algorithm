import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;

public class Solution {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int T = Integer.parseInt(bf.readLine());

		for (int tc = 1; tc <= T; tc++) {
			List<String>[] list = new List[5];
			
			for (int i = 0; i < 5; i++) {
				String temp = bf.readLine();

				ArrayList<String> tempList = new ArrayList<String>();

				for (int j = 0; j < temp.length(); j++) {
					tempList.add(String.valueOf(temp.charAt(j)));
				}
				list[i] = tempList;
			}
			bw.write("#"+tc+" ");
			for (int x = 0; x<15; x++) {
				for (int y = 0; y < 5; y++) {
					if (list[y].size() <= x ) {
						continue;
					}
					else {						
						bw.write(list[y].get(x));
					}
				}
			}
			bw.write("\n");
		}
		bw.flush();
		bw.close();
	}
}
