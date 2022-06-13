package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Q1238 {
    static List<List<Node>> list = new ArrayList<>();
    static int n;
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String[] str = reader.readLine().split(" ");
        n = Integer.parseInt(str[0]);
        int m = Integer.parseInt(str[1]);
        int x = Integer.parseInt(str[2]);

        for (int i=0; i<n+1; i++) {
            list.add(new ArrayList<>());
        }
        for (int i=0; i<m; i++) {
            int[] input = Arrays.stream(reader.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            list.get(input[0]).add(new Node(input[1], input[2]));
        }

        List<Integer> max = new ArrayList<>();
        int[] disAll = dijkstra(x);
        for (int i=1; i<n+1; i++) {
            int[] dis =  dijkstra(i);
            max.add(dis[x] + disAll[i]);
        }
        System.out.println(Collections.max(max));


    }

    private static int[] dijkstra(int start) {
        int[] distances = new int[n+1];
        Arrays.fill(distances, Integer.MAX_VALUE);
        Queue<Node> q = new PriorityQueue<>();
        distances[start] = 0;
        q.offer(new Node(start, 0));

        while (!q.isEmpty()) {
            Node node = q.poll();
            int index = node.index;
            int dis = node.distance;

            if (distances[index] < dis) {
                continue;
            }

            for (Node n : list.get(index)) {
                int cost = distances[index] + n.distance;

                if (cost < distances[n.index]) {
                    distances[n.index] = cost;
                    q.offer(new Node(n.index, cost));
                }
            }
        }
        return distances;
    }

    static class Node implements Comparable<Node> {
        int index, distance;

        public Node(int index, int distance) {
            this.index = index;
            this.distance = distance;
        }

        public int compareTo(Node node) {
            return this.distance - node.distance;
        }
    }
}
