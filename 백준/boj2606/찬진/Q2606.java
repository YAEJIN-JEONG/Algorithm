package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;


public class Q2606 {

    private static int[][] computer;
    private static boolean[] check;
    private static int count = 0;

    public static void main(String[] args) throws Exception {

        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(reader.readLine());
        int m = Integer.parseInt(reader.readLine());
        computer = new int[n+1][n+1];
        check = new boolean[n+1];
        for (int i=0; i<m; i++) {
            String[] str = reader.readLine().split(" ");
            int x = Integer.parseInt(str[0]);
            int y = Integer.parseInt(str[1]);
            computer[x][y] = computer[y][x] = 1;
        }
        bfs(1);
        System.out.println(count);
    }
    private static void bfs(int start) {
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(start);
        check[start] = true;
        while (!queue.isEmpty()) {
            int temp = queue.poll();
            for (int i=1; i< check.length; i++) {
                if (!check[i] && computer[temp][i] == 1) {
                    queue.offer(i);
                    check[i] = true;
                    count++;
                }
            }
        }
    }
}
