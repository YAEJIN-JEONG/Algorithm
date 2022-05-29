package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;

//https://www.acmicpc.net/problem/1780
public class Q1780 {
	
	private static int count = 0;
	private static int count1 = 0;
	private static int count2 = 0;
	private static int[][] matrix;
	
	public static void main(String[] args) throws Exception {
		
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(reader.readLine());
		matrix = new int[n+1][n+1];
		for (int i=0; i<n; i++) {
			String[] str = reader.readLine().split(" ");
			for (int j=0; j<str.length; j++) {
				matrix[i][j] = Integer.parseInt(str[j]);
			}
		}
		
		check(0, 0, n);
		System.out.println(count);
		System.out.println(count1);
		System.out.println(count2);
		
		
	}

	private static void check(int row, int col, int size) {
		
		if(checkcolor(row, col, size)) {
			
		} else {
			size = size / 3;
			check(row, col, size);
			check(row+size, col, size);
			check(row+(2*size), col, size);
			check(row, col+size, size);
			check(row, col+(2*size), size);
			check(row+size, col+size, size);
			check(row+(2*size), col+size, size);
			check(row+size, col+(2*size), size);
			check(row+(2*size), col+(2*size), size);
			
		}
		
		
	}

	private static boolean checkcolor(int row, int col, int size) {
		
		int start = matrix[row][col];
		for (int i=row; i<row+size; i++) {
			for (int j=col; j<col+size; j++) {
				if (start != matrix[i][j]) {
					return false;
				}
			}
		}
		
		if (start == -1) {
			count++;
		} else if (start == 0) {
			count1++;
		} else if (start == 1) {
			count2++;
		}
		return true;
		
	}

	

	

}
