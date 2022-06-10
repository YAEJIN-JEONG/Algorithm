package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

//https://www.acmicpc.net/problem/16928
public class Q16928 {

    static int[] ladder;
    static boolean[] visited;
    static int[] count;

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String[] str = reader.readLine().split(" ");
        int n = Integer.parseInt(str[0]);
        int m = Integer.parseInt(str[1]);
        ladder = new int[101];
        visited = new boolean[101];
        count = new int[101];
        count[1] = 0;
        for (int i=0; i<n+m; i++) {
            str = reader.readLine().split(" ");
            int a = Integer.parseInt(str[0]);
            int b = Integer.parseInt(str[1]);
            ladder[a] = b;
        }

        bfs();
    }
    private static void bfs() {
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(1);
        visited[1] = true;

        while (!queue.isEmpty()) {
            int now = queue.poll();

            if (now == 100) {
                System.out.println(count[now]);
                return;
            }

            for (int i=1; i<=6; i++) {
                int next = now + i;
                if (next > 100) continue;
                if (visited[next]) continue;
                visited[next] = true;
                if (ladder[next] != 0) {
                    if (!visited[ladder[next]]) {
                        queue.offer(ladder[next]);
                        visited[ladder[next]] = true;
                        count[ladder[next]] = count[now] + 1;
                    }
                } else {
                    queue.offer(next);
                    visited[next] = true;
                    count[next] = count[now] + 1;
                }
            }
        }
    }
}
