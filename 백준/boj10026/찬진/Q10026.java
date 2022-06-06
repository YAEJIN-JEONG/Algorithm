package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

//https://www.acmicpc.net/problem/10026
public class Q10026 {
    static boolean[][] visited;
    static String[][] RGB;
    static String[][] RB;
    static int n;
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(reader.readLine());
        visited = new boolean[n][n];
        RGB = new String[n][n];
        RB = new String[n][n];
        for (int i=0; i<n; i++) {
            String strRGB = reader.readLine();
            String strRB = strRGB.replace("G", "R");
            for (int j=0; j<n; j++) {
                RGB[i][j] = String.valueOf(strRGB.charAt(j));
                RB[i][j] = String.valueOf(strRB.charAt(j));
            }
        }

        int cnt = 0;
        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++) {
                if (!visited[i][j]) {
                    bfs(i, j, RGB);
                    cnt++;
                }
            }
        }
        System.out.print(cnt + " ");

        cnt = 0;
        visited = new boolean[n][n];
        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++) {
                if (!visited[i][j]) {
                    bfs(i, j, RB);
                    cnt++;
                }
            }
        }
        System.out.print(cnt);
    }

    private static void bfs(int x, int y, String[][] res) {
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[] {x, y});
        visited[x][y] = true;

        int[] dx = {1, -1, 0, 0};
        int[] dy = {0, 0, 1, -1};

        while (!queue.isEmpty()) {
            int[] temp = queue.poll();

            for (int i=0; i<4; i++) {
                int nextX = temp[0] + dx[i];
                int nextY = temp[1] + dy[i];

                if (nextX < 0 || nextY < 0 || nextX >= n || nextY >= n) {
                    continue;
                }

                if (res[nextX][nextY].equals(res[x][y]) && !visited[nextX][nextY]) {
                    queue.offer(new int[] {nextX, nextY});
                    visited[nextX][nextY] = true;
                }
            }

        }
    }
}
