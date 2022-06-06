package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

public class Q11286 {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(reader.readLine());
        PriorityQueue<Integer> queue = new PriorityQueue<>((o1, o2) -> {
            if (Math.abs(o1) > Math.abs(o2)) {
                return Math.abs(o1) - Math.abs(o2);
            } else if (Math.abs(o1) == Math.abs(o2)) {
                return o1 - o2;
            } else {
                return -1;
            }
        });
        for (int i=0; i<n; i++) {
            int x = Integer.parseInt(reader.readLine());
            if (x == 0) {
                if (queue.isEmpty()) {
                    System.out.println(0);
                } else {
                    System.out.println(queue.poll());
                }
            } else {
                queue.offer(x);
            }
        }

    }
}
