import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Solution2 {
//	throws IOException - BufferedReader의 메소드인 readLine()은 IOException을 발생 시킴
	public static void main(String[] args) throws IOException {
//		입력 방법 설정
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
//		출력 방법 설정
		StringBuilder builder = new StringBuilder();
		
//		학점 목록 배열
		String[] grade = {"A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"}; 
		
//		테스트 케이스의 갯수인 "10"을 string으로 받아 오기 때문에
//		int형 변환 메소드를 사용
		int tc = Integer.parseInt(bf.readLine());
		
		for (int i = 1; i <= tc; i++) {
			
//			"총 인원수, 특정 학생 번호 줄" 한 줄 입력 전체를 읽어 옴
			String str = bf.readLine();
			
//			읽어온 한줄을 " " 단위로 끊어서 st에 저장
			StringTokenizer st = new StringTokenizer(str, " ");
			
//			nextToken() - 메소드를 이용하여 끊어진 단위 차례로 읽어옴
			int studentNum[] = new int[Integer.parseInt(st.nextToken())];
			int checkNum = Integer.parseInt(st.nextToken());
			
			
			int A, B, C;
			
//			key를 이용하여 value를 읽어 오기 위해 HashMap 자료구조를 선택
			HashMap<Integer, Double> scoreMap = new HashMap<Integer, Double>();
			
			for(int j = 0; j < studentNum.length; j++) {
				str = bf.readLine();
				st = new StringTokenizer(str, " ");
				
				A = Integer.parseInt(st.nextToken());
				B = Integer.parseInt(st.nextToken());
				C = Integer.parseInt(st.nextToken());
				
//				scoreMap 에 학생번호를 key로 점수를 value로 갖도록 저장
				scoreMap.put((j+1), A*0.35+B+0.45+C*0.2);
			}
			
//			정렬하기 위해 ArrayList 에 scoreMap의 value값들을 뽑아 저장
			ArrayList<Double> list = new ArrayList<Double>(scoreMap.values());
//			정렬
			Collections.sort(list);
//			뒤집기
			Collections.reverse(list);
			
//			대상 학생의 점수가 몇번째 인지 확인
//			1. 학생의 점수 찾기
//			2. 점수의 index Number 찾기
			int index = list.indexOf(scoreMap.get(checkNum));
			
//			builder 변수에 string을 append() 메소드를 이용하여 추가
			builder.append("#").append(i).append(" ").append(grade[index/(studentNum.length/10)]).append("\n");
		}
		System.out.println(builder);
	}
}
