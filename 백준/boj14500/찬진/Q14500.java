package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

//https://www.acmicpc.net/problem/14500
public class Q14500 {
    static int n;
    static int m;
    static int[][] arr;
    static boolean[][] visited;
    static int result = 0;
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String[] input = reader.readLine().split(" ");
        n = Integer.parseInt(input[0]);
        m = Integer.parseInt(input[1]);
        arr = new int[n][m];
        visited = new boolean[n][m];
        for (int i=0; i<n; i++) {
            String[] str = reader.readLine().split(" ");
            for (int j=0; j<m; j++) {
                arr[i][j] = Integer.parseInt(str[j]);
            }
        }
        for (int i=0; i<n; i++) {
            for (int j=0; j<m; j++) {
                visited[i][j] = true;
                dfs(i, j, 1, arr[i][j]);
                visited[i][j] = false;
            }
        }
        System.out.println(result);
    }
    private static void dfs(int x, int y, int depth, int sum) {
        if (depth == 4) {
            result = Math.max(result, sum);
            return;
        }
        int[][] d = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        for (int i=0; i<4; i++) {
            int nowX = x + d[i][0];
            int nowY = y + d[i][1];
            if (nowX < 0 || nowY < 0 || nowX >= n || nowY >= m || visited[nowX][nowY]) {
                continue;
            }

            visited[nowX][nowY] = true;
            dfs(nowX, nowY, depth + 1, sum + arr[nowX][nowY]);
            if (depth == 2) {
                dfs(x, y, depth + 1, sum + arr[nowX][nowY]);
            }
            visited[nowX][nowY] = false;
        }
    }
}
