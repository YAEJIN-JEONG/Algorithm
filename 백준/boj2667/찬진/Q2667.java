package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

//https://www.acmicpc.net/problem/2667
public class Q2667 {

    private static int[][] house;
    private static boolean[][] visited;
    private static int count = 0;
    private static List<Integer> list = new ArrayList<>();

    public static void main(String[] args) throws Exception {

        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(reader.readLine());
        house = new int[n][n];
        visited = new boolean[n][n];
        for (int i=0; i<n; i++) {
            String str = reader.readLine();
            for (int j=0; j<n; j++) {
                house[i][j] = str.charAt(j) - '0';
            }
        }

        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++) {
                if (house[i][j] != 0 && !visited[i][j]) {
                    bfs(i, j);
                    count++;
                }
            }
        }
        System.out.println(count);
        Collections.sort(list);
        for (int i : list) {
            System.out.println(i);
        }

    }

    private static void bfs(int startX, int startY) {
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[] {startX, startY});
        visited[startX][startY] = true;

        int[] x = {1, -1, 0, 0};
        int[] y = {0, 0, 1, -1};

        int cnt = 1;
        while (!queue.isEmpty()) {
            int[] temp = queue.poll();
            int nowX = temp[0];
            int nowY = temp[1];

            for (int i=0; i<4; i++) {
                int nextX = nowX + x[i];
                int nextY = nowY + y[i];

                if (nextX < 0 || nextY < 0 || nextX >= house.length || nextY >= house.length) {
                    continue;
                }
                if (house[nextX][nextY] != 0 && !visited[nextX][nextY]) {
                    queue.offer(new int[] {nextX, nextY});
                    visited[nextX][nextY] = true;
                    cnt++;
                }
            }
        }
        list.add(cnt);

    }
}
