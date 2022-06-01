package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;

//https://www.acmicpc.net/problem/1992
public class Q1992 {
	
	private static String result = "";
	
	public static void main(String[] args) throws Exception {
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(reader.readLine());
		int[][] tree = new int[n][n];
		for (int i=0; i<n; i++) {
			String str = reader.readLine();
			for (int j=0; j<str.length(); j++) {
				tree[i][j] = str.charAt(j) - '0';
			}
		}
		
		quad(tree, 0, 0, tree.length);
		System.out.println(result);
		
	}

	private static void quad(int[][] tree, int i, int j, int size) {
		
		if (valid(tree, i, j, size)) {
			result += tree[i][j];
		} else {
			result += "(";
			size = size / 2;
			quad(tree, i, j, size);
			quad(tree, i, j+size, size);
			quad(tree, i+size, j, size);
			quad(tree, i+size, j+size, size);
			result += ")";
			
		}
		
	}

	private static boolean valid(int[][] tree, int x, int y, int size) {
		
		for (int i=x; i<x+size; i++) {
			for (int j=y; j<y+size; j++) {
				if (tree[x][y] != tree[i][j]) {
					return false;
				}
			}
		}
		
		return true;
	}

}
