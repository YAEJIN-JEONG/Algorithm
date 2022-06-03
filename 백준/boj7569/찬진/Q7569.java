package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

//https://www.acmicpc.net/problem/7569
public class Q7569 {

    static int m;
    static int n;
    static int h;
    static int[][][] tomato;
    static boolean[][][] visited;
    static Queue<int[]> queue = new LinkedList<>();


    public static void main(String[] args) throws IOException {

        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String[] str = reader.readLine().split(" ");
        m = Integer.parseInt(str[0]);
        n = Integer.parseInt(str[1]);
        h = Integer.parseInt(str[2]);

        //3차원 배열
        tomato = new int[h][n][m];
        visited = new boolean[h][n][m];
        int cnt = 0;
        for (int i=0; i<h; i++) {
            for (int j=0; j<n; j++) {
                String[] s = reader.readLine().split(" ");
                for (int k=0; k<m; k++) {
                    tomato[i][j][k] = Integer.parseInt(s[k]);
                    //한번에 진행해야 하기 때문에 다 익은 상태를 미리 넣어놓는다.
                    if (Integer.parseInt(s[k]) == 1) {
                        queue.offer(new int[] {i, j, k});
                        visited[i][j][k] = true;
                    //안익은 토마토가 없으면 1을 출력시켜야 해서 따로 카운트한다.
                    } else if (Integer.parseInt(s[k]) == 0) {
                        cnt++;
                    }
                }
            }
        }
        //안익은 토마토가 없으면 0을 출력시킨다.
        if (cnt == 0) {
            System.out.println(0);
            return;
        }
        //bfs를 실행시키고 며칠이 걸리는지 a에 저장시킨다.
        int a = bfs();
        for (int i=0; i<h; i++) {
            for (int j=0; j<n; j++) {
                for (int k=0; k<m; k++) {
                    //안익은 토마토가 있으면 -1을 출력시킨다.
                    if (tomato[i][j][k] == 0) {
                        System.out.println(-1);
                        return;
                    }
                }
            }
        }
        System.out.println(a);

    }

    private static int bfs() {

        //상하좌우앞뒤
        int[] dx = {1, -1, 0, 0, 0, 0};
        int[] dy = {0 ,0, 1, -1, 0, 0};
        int[] dz = {0, 0, 0, 0, 1, -1};

        int cnt = 0;
        while (!queue.isEmpty()) {
            int size = queue.size();
            //size만큼 돌았을때 하루가 지난다.
            for (int k=0; k<size; k++) {
                int[] temp = queue.poll();

                for (int i=0; i<6; i++) {
                    int nextX = temp[0] + dx[i];
                    int nextY = temp[1] + dy[i];
                    int nextZ = temp[2] + dz[i];

                    if (nextX < 0 || nextY < 0 || nextZ < 0 || nextX >= h || nextY >= n || nextZ >= m) {
                        continue;
                    }
                    if (tomato[nextX][nextY][nextZ] == 0) {
                        tomato[nextX][nextY][nextZ] = 1;
                        queue.offer(new int[] {nextX, nextY, nextZ});
                        visited[nextX][nextY][nextZ] = true;
                    }
                }
            }
            cnt++;
        }
        //며칠이 지났는지 반환
        return cnt-1;

    }
}
