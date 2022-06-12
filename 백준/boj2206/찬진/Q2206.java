package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

//https://www.acmicpc.net/problem/2206
public class Q2206 {
    static int n;
    static int m;
    static char[][] arr;
    static int[][][] count;

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String[] str = reader.readLine().split(" ");
        n = Integer.parseInt(str[0]);
        m = Integer.parseInt(str[1]);
        arr = new char[n][m];
        // count[0] 이면 안부쉈을때 count[1] 이면 부쉈을때 상황
        count = new int[2][n][m];
        for (int i=0; i<n; i++) {
            arr[i] = reader.readLine().toCharArray();
        }
        System.out.println(bfs());
    }

    private static int bfs() {
        Queue<int[]> queue = new LinkedList<>();
        // queue에서 int[0] 은 0일때 안부쉈고 1일때 부순 상황
        queue.offer(new int[] {0, 0, 0});

        int[][] d = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while (!queue.isEmpty()) {
            int[] now = queue.poll();
            if (now[1] == n-1 && now[2] == m-1) {

                return count[now[0]][now[1]][now[2]] + 1;
            }
            for (int i=0; i<4; i++) {
                int nextX = now[1] + d[i][0];
                int nextY = now[2] + d[i][1];

                if (nextX < 0 || nextY < 0 || nextX >= n || nextY >= m) {
                    continue;
                }
                // 다음 배열에서 1일때 now[0] != 0 이면 부순적이 있는 상황이기 때문에 제외한다.
                if (arr[nextX][nextY] == '1') {
                    if (now[0] == 0 && count[1][nextX][nextY] == 0) {
                        queue.offer(new int[] {1, nextX, nextY});
                        count[1][nextX][nextY] = count[0][now[1]][now[2]] + 1;
                    }
                } else {
                    if (count[now[0]][nextX][nextY] == 0) {
                        queue.offer(new int[] {now[0], nextX, nextY});
                        count[now[0]][nextX][nextY] = count[now[0]][now[1]][now[2]] + 1;
                    }
                }
            }
        }
        return -1;
    }
}
