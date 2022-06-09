package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

//https://www.acmicpc.net/problem/16236
public class Q16236 {
    static int n;
    static int[][] arr;
    static boolean[][] visited;
    static int size = 2;
    static int eat;
    static int time;
    static List<int[]> list;
    static int[] start = new int[2];

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(reader.readLine());
        arr = new int[n][n];
        for (int i = 0; i < n; i++) {
            String[] str = reader.readLine().split(" ");
            for (int j = 0; j < n; j++) {
                if (str[j].equals("9")) {
                    start[0] = i;
                    start[1] = j;
                }
                arr[i][j] = Integer.parseInt(str[j]);
            }
        }
        arr[start[0]][start[1]] = 0;
        while (true) {
            list = new ArrayList<>();
            visited = new boolean[n][n];
            bfs(start[0], start[1]);
            if (list.size() == 0) {
                break;
            }
            list.sort((o1, o2) -> {
                int a = (o1[0] * 100) + (o1[1] * 10) + (o1[2]);
                int b = (o2[0] * 100) + (o2[1] * 10) + (o2[2]);
                return a - b;
            });
            start[0] = list.get(0)[1];
            start[1] = list.get(0)[2];
            time += list.get(0)[0];
            arr[start[0]][start[1]] = 0;
            eat++;
            if (size == eat) {
                size++;
                eat = 0;
            }
        }
        System.out.println(time);

    }

    private static void bfs(int x, int y) {
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{x, y});
        visited[x][y] = true;

        int[][] d = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        int dis = 1;
        while (!queue.isEmpty()) {
            int s = queue.size();
            for (int i=0; i<s; i++) {
                int[] now = queue.poll();
                for (int[] j : d) {
                    int nowX = now[0] + j[0];
                    int nowY = now[1] + j[1];
                    if (nowX >= 0 && nowY >= 0 && nowX < n && nowY < n) {
                        if (arr[nowX][nowY] > 0 && arr[nowX][nowY] < size) {
                            list.add(new int[]{dis, nowX, nowY});
                        }
                        if (!visited[nowX][nowY] && arr[nowX][nowY] <= size) {
                            queue.offer(new int[] {nowX, nowY});
                            visited[nowX][nowY] = true;
                        }
                    }
                }
            }
            dis++;
        }
    }
}
