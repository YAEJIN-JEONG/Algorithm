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
                dfs(i, j, 0, 0);
                visited[i][j] = false;
                check(i, j);
            }
        }
        System.out.println(result);
    }
    private static void check(int x, int y) {
        if (x >= 0 && x+2 < n && y >= 0 && y+1 < m) {
            result = Math.max(result, arr[x][y] + arr[x+1][y] + arr[x+1][y+1] + arr[x+2][y]);
        }
        if (x-1 >= 0 && x < n && y >= 0 && y+2 < m) {
            result = Math.max(result, arr[x][y] + arr[x-1][y+1] + arr[x][y+1] + arr[x][y+2]);
        }
        if (x >= 0 && x+2 < n && y-1 >= 0 && y < m) {
            result = Math.max(result, arr[x][y] + arr[x+1][y-1] + arr[x+1][y] + arr[x+2][y]);
        }
        if (x >= 0 && x+1 < n && y >= 0 && y+2 < m) {
            result = Math.max(result, arr[x][y] + arr[x][y+1] + arr[x+1][y+1] + arr[x][y+2]);
        }
    }
    private static void dfs(int x, int y, int depth, int sum) {
        if (depth == 4) {
            result = Math.max(result, sum);
            return;
        }
        sum += arr[x][y];
        int[][] d = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        for (int i=0; i<4; i++) {
            int nowX = x + d[i][0];
            int nowY = y + d[i][1];
            if (nowX < 0 || nowY < 0 || nowX >= n || nowY >= m) {
                continue;
            }
            if (!visited[nowX][nowY]) {
                visited[nowX][nowY] = true;
                dfs(nowX, nowY, depth + 1, sum);
                visited[nowX][nowY] = false;
            }
        }
    }
}
