package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
//https://www.acmicpc.net/problem/2630
public class Q2630 {

    private static int white = 0;
    private static int blue = 0;

    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(reader.readLine());
        int[][] matrix = new int[n][n];
        for (int i=0; i<n; i++) {
            String[] str = reader.readLine().split(" ");
            for (int j=0; j<str.length; j++) {
                matrix[i][j] = Integer.parseInt(str[j]);
            }
        }

        divide(matrix, 0, 0, matrix.length);
        System.out.println(white);
        System.out.println(blue);
    }

    private static void divide(int[][] matrix, int x, int y, int size) {
        if(check(matrix, x, y, size)) {
            if (matrix[x][y] == 1) {
                blue++;
            } else {
                white++;
            }
        } else {
            size = size / 2;
            divide(matrix, x, y, size);
            divide(matrix, x+size, y, size);
            divide(matrix, x, y+size, size);
            divide(matrix, x+size, y+size, size);
        }
    }

    private static boolean check(int[][] matrix, int x, int y, int size) {
        int start = matrix[x][y];
        for (int i=x; i<x+size; i++) {
            for (int j=y; j<y+size; j++) {
                if (start != matrix[i][j]) {
                    return false;
                }
            }
        }
        return true;
    }
}
