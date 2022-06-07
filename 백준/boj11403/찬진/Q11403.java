package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class Q11403 {
    static int n;
    static int[][] graph;
    static boolean[] visited;
    static int[][] result;
    static boolean flag;
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(reader.readLine());
        graph = new int[n][n];
        result = new int[n][n];
        for (int i=0; i<n; i++) {
            String[] str = reader.readLine().split(" ");
            for (int j=0; j<n; j++) {
                graph[i][j] = Integer.parseInt(str[j]);
            }
        }
        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++) {
                visited = new boolean[n];
                flag = false;
                bfs(i, j);
                if (flag) {
                    result[i][j] = 1;
                }
            }
        }
        for (int i=0; i<n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(result[i][j] + " ");
            }
            System.out.println();
        }
    }

    private static void bfs(int start, int end) {
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(start);
        while (!queue.isEmpty()) {
            int now = queue.poll();
            if (now == end && visited[now]) {
                flag = true;
            }
            for (int i=0; i<n; i++) {
                if (graph[now][i] == 1 && !visited[i]) {
                    queue.offer(i);
                    visited[i] = true;
                }
            }
        }
    }
}
