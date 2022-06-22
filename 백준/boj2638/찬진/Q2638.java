package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

//https://www.acmicpc.net/problem/2638
public class Q2638 {
    static int n;
    static int m;
    static int[][] cheese;
    static int[][] cheese_melt;
    //치즈 방문
    static boolean[][] visited_cheese;
    //외부 공기 방문
    static boolean[][] visited_cheese_air;
    static int[][] d = {{-1, 0}, {1, 0}, {0, 1}, {0 ,-1}};
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String[] str = reader.readLine().split(" ");
        n = Integer.parseInt(str[0]);
        m = Integer.parseInt(str[1]);
        cheese = new int[n][m];
        cheese_melt = new int[n][m];
        for (int i=0; i<n; i++) {
            int[] ints = Arrays.stream(reader.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            for (int j=0; j<m; j++) {
                cheese[i][j] = ints[j];
                cheese_melt[i][j] = ints[j];
            }
        }
        int count = 0;
        boolean flag = true;
        while (flag) {
            flag = false;
            visited_cheese_air = new boolean[n][m];
            //외부 공기 체크
            for (int i=0; i<n; i++) {
                for (int j=0; j<m; j++) {
                    if (!visited_cheese_air[i][j] && cheese[i][j] == 0 && (i == 0 || i == n-1 || j == 0 || j == m-1)) {
                        bfs_cheese_air(i, j);
                    }
                }
            }
            visited_cheese = new boolean[n][m];
            for (int i=0; i<n; i++) {
                for (int j=0; j<m; j++) {
                    if (!visited_cheese[i][j] && cheese[i][j] == 1) {
                        bfs_cheese(i, j);
                        flag = true;
                    }
                }
            }
            //cheese_melt 배열 cheese에 저장
            for (int i=0; i<n; i++) {
                for (int j=0; j<m; j++) {
                    int a = cheese_melt[i][j];
                    cheese[i][j] = a;
                }
            }
            count++;

        }
        System.out.println(count-1);
    }

    private static void bfs_cheese_air(int x, int y) {
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[] {x, y});
        visited_cheese_air[x][y] = true;

        while (!q.isEmpty()) {
            int[] now = q.poll();

            for (int i=0; i<4; i++) {
                int nextX = now[0] + d[i][0];
                int nextY = now[1] + d[i][1];
                if (nextX < 0 || nextY < 0 || nextX >= n || nextY >= m) {
                    continue;
                }
                if (!visited_cheese_air[nextX][nextY] && cheese[nextX][nextY] == 0) {
                    q.offer(new int[] {nextX, nextY});
                    visited_cheese_air[nextX][nextY] = true;
                }

            }
        }
    }

    private static void bfs_cheese(int x, int y) {
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[] {x, y});
        visited_cheese[x][y] = true;
        int c = 0;
        for (int i=0; i<4; i++) {
            int nx = x + d[i][0];
            int ny = y + d[i][1];
            if (cheese[nx][ny] == 0 && visited_cheese_air[nx][ny]) {
                c++;
            }
        }
        if (c >= 2) {
            cheese_melt[x][y] = 0;
        }
        while (!q.isEmpty()) {
            int[] now = q.poll();

            for (int i=0; i<4; i++) {
                int nextX = now[0] + d[i][0];
                int nextY = now[1] + d[i][1];

                if (nextX < 0 || nextY < 0 || nextX >= n || nextY >= m) {
                    continue;
                }
                if (!visited_cheese[nextX][nextY] && cheese[nextX][nextY] == 1) {
                    int cnt = 0;
                    for (int j=0; j<4; j++) {
                        int nnX = nextX + d[j][0];
                        int nnY = nextY + d[j][1];
                        if (cheese[nnX][nnY] == 0 && visited_cheese_air[nnX][nnY]) {
                            cnt++;
                        }
                    }
                    if (cnt >= 2) {
                        cheese_melt[nextX][nextY] = 0;
                    }
                    q.offer(new int[] {nextX, nextY});
                    visited_cheese[nextX][nextY] = true;
                }
            }
        }
    }
}
