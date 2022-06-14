package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

//https://www.acmicpc.net/problem/1799
public class Q1799 {
    static int[][] arr, check;
    static boolean[][] visited;
    static List<int[]> list = new ArrayList<>();
    static int result, n;
    static boolean[] slash, back;
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(reader.readLine());
        arr = new int[n][n];
        visited = new boolean[n][n];
        check = new int[n][n];
        slash = new boolean[2*n+1];
        back = new boolean[2*n+1];
        for (int i=0; i<n; i++) {
            int[] input = Arrays.stream(reader.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            for (int j=0; j<input.length; j++) {
                arr[i][j] = input[j];
                if (input[j] == 1) {
                    list.add(new int[] {i, j});
                }
                if ((i % 2 == 0 && j % 2 == 0) || (i % 2 != 0 && j % 2 != 0)) {
                    check[i][j] = 1;
                } else {
                    check[i][j] = 0;
                }
            }
        }
        int sum = 0;
        backtrack(0, 0, 1);
        sum += result;
        result = 0;
        backtrack(0, 0, 0);
        sum += result;
        System.out.println(sum);
    }
    private static void backtrack(int start, int depth, int black) {
        result = Math.max(result, depth);
        for (int i=start; i<list.size(); i++) {
            int x = list.get(i)[0];
            int y = list.get(i)[1];
            if (check[x][y] == black && !slash[x+y] && !back[x-y+n]) {
                slash[x+y] = back[x-y+n] = visited[x][y] = true;
                backtrack(i + 1, depth + 1, black);
                slash[x+y] = back[x-y+n] = visited[x][y] = false;
            }
        }
    }
}
