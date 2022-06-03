package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class Q7576 {

    static int m;
    static int n;
    static int[][] tomato;
    static boolean[][] visited;
    static Queue<int[]> queue = new LinkedList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String[] s = reader.readLine().split(" ");
        m = Integer.parseInt(s[0]);
        n = Integer.parseInt(s[1]);
        tomato = new int[n][m];
        visited = new boolean[n][m];

        for (int i=0; i<n; i++) {
            String[] str = reader.readLine().split(" ");
            for (int j=0; j<m; j++) {
                tomato[i][j] = Integer.parseInt(str[j]);
                if (Integer.parseInt(str[j]) == 1) {
                    queue.offer(new int[] {i, j});
                    visited[i][j] = true;
                }
            }
        }

        int a = bfs();
        for (int i=0; i<n; i++) {
            for (int j=0; j<m; j++) {
                if (tomato[i][j] == 0) {
                    System.out.println(-1);
                    return;
                }
            }
        }
        System.out.println(a);

    }

    private static int bfs() {

        int[] dx = {1, -1, 0, 0};
        int[] dy = {0 ,0, 1, -1};

        int cnt = 0;
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i=0; i<size; i++) {
                int[] temp = queue.poll();
                for (int j=0; j<4; j++) {
                    int nextX = temp[0] + dx[j];
                    int nextY = temp[1] + dy[j];

                    if (nextX < 0 || nextY < 0 || nextX >= n || nextY >= m) {
                        continue;
                    }
                    if (tomato[nextX][nextY] == 0) {
                        tomato[nextX][nextY] = 1;
                        queue.offer(new int[] {nextX, nextY});
                        visited[nextX][nextY] = true;
                    }
                }
            }
            cnt++;
        }
        return cnt-1;

    }
}
