import java.util.*;
public class Solution2 {
	static int sharp(int x, int y) {
		return ((x+y)*(x+y-1)/2)+1-y;
	}
	static int[] amp(int n) {
		int sum, sharp = 0;
		for(sum=2; sum<=20000; sum++) {
			sharp = sharp(sum-1,1);
			if( n <= sharp ) break;
		}
		int y = sharp - n + 1;
		int x = sum - y;
		int[] result = {x,y};
		return result;
	}
	static int star(int n1, int n2) {
		int[] point1 = amp(n1);
		int[] point2 = amp(n2);
		return sharp(point1[0]+point2[0], point1[1]+point2[1]);
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int tc=1; tc<=T; tc++) {
			int p = sc.nextInt();
			int q = sc.nextInt();
			System.out.format("#%d %d\n", tc, star(p, q));
		}
		sc.close();
	}
}