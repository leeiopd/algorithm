import java.util.*;

public class Solution {
	public static int maps[][] = new int[9][9];
	public static int check[] = new int[9];
	public static int boxs[] = {0, 3, 6};
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int T = sc.nextInt();
		for (int testCase = 1; testCase <= T; testCase++) {
			for (int y = 0; y < 9; y++) {
				for (int x = 0; x < 9; x++) {
					maps[y][x] = sc.nextInt();
				}
			}

			if (check()==true) {
				System.out.println("#"+testCase+" 1");

			}
			else {
				System.out.println("#"+testCase+" 0");
			}
		}
		sc.close();
	}
	public static boolean check() {
		if (checkRow()==false) {
			return false;
		}

		if (checkCol() == false) {
			return false;
		}

		for (int j = 0; j < 3; j++) {
			for (int i = 0; i< 3; i++) {	
				if (checkBox(boxs[j],boxs[i]) == false) {
					return false;
				}
			}				
		}


		return true;
	}


	public static boolean checkRow() {
		for(int y = 0; y < 9; y++) {
			for (int i = 0; i < 9; i++){
				check[i] = 1;
			}
			for(int x = 0; x < 9; x++) {
				check[maps[y][x]-1] = 0;
			}
			for (int i = 0; i < 9; i++) {
				if (check[i] == 1) {
					return false;
				}
			}
		}
		return true;
	}

	public static boolean checkCol() {
		for(int x = 0; x < 9; x++) {
			for (int i = 0; i < 9; i++){
				check[i] = 1;
			}
			for(int y = 0; y < 9; y++) {
				check[maps[y][x]-1] = 0;
			}
			for (int i = 0; i < 9; i++){
				if (check[i] == 1) {
					return false;
				}
			}
		}
		return true;
	}

	public static boolean checkBox(int X, int Y) {
		for (int i = 0; i < 9; i++){
			check[i] = 1;
		}
		for(int y = 0; y < 3; y++) {
			for(int x = 0; x < 3; x++) {
				check[maps[Y+y][X+x]-1] = 0;
			}
		}
		for (int i = 0; i < 9; i++){
			if (check[i] == 1) {
				return false;
			}
		}
		return true;
	}
}
