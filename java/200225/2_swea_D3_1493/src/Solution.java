import java.util.ArrayList;
import java.util.Scanner;

public class Solution {
	
	public static ArrayList<Integer> maps = new ArrayList<Integer>();
	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		maps.add(0);
		for (int y = 1; y < 81; y++) {
			maps.add(((y*(y-1))/2) + 1);
		}
		
		
		int T = sc.nextInt();
		
		for (int tc = 1; tc <= T; tc++) {
			
			int p = sc.nextInt();
			int q = sc.nextInt();
			
			System.out.println("#"+tc+" "+star(p, q));
		}
	}
	
	static int star(int p, int q) {
		int result = shap(add(and(p), and(q)));
		return result;
	}
	
	static int shap(int[] add) {
		int y = add[0];
		int x = add[1];
		
		return maps.get(y+x-1)+x-1;
	}
	
	static int[] and(int p) {
		int Y = 0;
		int X = 0;
		
//		for (int y = 0; y < 81; y++) {
//			if (maps.contains(p-y)) {
//				Y = maps.indexOf(p-y)-y;
//				X = 1+y;
//				break;
//			}
//		}
		
		
		
		int[] nums = {Y, X};
		return nums;
	}
	
	static int[] add(int[] p, int[] q) {
		int[] result  = new int[2];
		result[0] = p[0]+q[0];
		result[1] = p[1]+q[1];
		return result;
	}
	
}
