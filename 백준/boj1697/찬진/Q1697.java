package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

//https://www.acmicpc.net/problem/1697
public class Q1697 {
	
	private static boolean[] visited = new boolean[100001];
	private static int result = 0;
	public static void main(String[] args) throws Exception {
		
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		
		String[] str = reader.readLine().split(" ");
		int n = Integer.parseInt(str[0]);
		int k = Integer.parseInt(str[1]);
		
		bfs(n, k);
		System.out.println(result);
		
	}

	private static void bfs(int n, int k) {
		
		Queue<Integer> queue = new LinkedList<Integer>();
		queue.offer(n);
		visited[n] = true;
		
		int level = 0;
		while(!queue.isEmpty()) {
			int qsize = queue.size();
			for (int i=0; i<qsize; i++) {
				int temp = queue.poll();
				if (temp < k) {
					if (temp > 0 && !visited[temp-1]) {
						queue.offer(temp-1);
						visited[temp-1] = true;
					}
					if (temp*2 <= 100000 && !visited[temp*2]) {
						queue.offer(temp*2);
						visited[temp*2] = true;
					}
					if (temp+1 <= 100000 && !visited[temp+1]) {
						queue.offer(temp+1);
						visited[temp+1] = true;
					}
				} else if (temp == k) {
					result = level;
					return;
				} else {
					if (temp > 0 && !visited[temp-1]) {
						queue.offer(temp-1);
						visited[temp-1] = true;
					}
				}
				
			}
			level++;
		}
		
	}

}
