import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;

public class Solution{
	public static List<String>[] resultList = null;
	public static String[] nums = null;
	
	
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int T = Integer.parseInt(bf.readLine());
		
		for (int tc = 1; tc <= T; tc++) {
			int K = Integer.parseInt(bf.readLine());
			
			nums = bf.readLine().split(" ");
			
			resultList = new List[K];
			
			for (int i = 0; i < K; i++) {
				resultList[i] = new ArrayList<String>();
			}
			
			fcn(0, K-1, 0, nums.length-1);
			
			bw.write("#"+tc+" ");
			
			for (int i = 0; i < K; i++) {
				for (int j = 0; j < resultList[i].size(); j++) {					
					bw.write(resultList[i].get(j)+" ");
				}
				bw.write("\n");
			}
			
		
		}
		bw.flush();
		bw.close();
	}
	
	public static void fcn(int cnt, int K, int st, int end) {
		int mid = st+(end-st)/2;
		resultList[cnt].add(nums[mid]);
		if (cnt == K) {
			return;
		}
		else {
			fcn(cnt+1, K, st, mid-1);
			fcn(cnt+1, K, mid+1, end);
		}
	}
}