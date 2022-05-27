package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;

import java.util.Queue;

public class Q1260 {

	private static int[][] check;
	private static boolean[] visited;
	private static int n;
	private static int m;
	private static int v;

	public static void main(String[] args) throws Exception {

		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		String[] str = reader.readLine().split(" ");
		n = Integer.parseInt(str[0]);
		m = Integer.parseInt(str[1]);
		v = Integer.parseInt(str[2]);
		
		check = new int[n+1][n+1];
		visited = new boolean[n+1];
		
		for (int i=0; i<m; i++) {
			str = reader.readLine().split(" ");
			int x = Integer.parseInt(str[0]);
			int y = Integer.parseInt(str[1]);
			
			check[x][y] = check[y][x] = 1;
		}
		
		dfs(v);
		System.out.println();
		visited = new boolean[n+1];
		bfs(v);

	}

	private static void bfs(int i) {
		Queue<Integer> queue = new LinkedList<Integer>();
		queue.offer(i);
		visited[i] = true;
		while (!queue.isEmpty()) {
			int temp = queue.poll();
			System.out.print(temp + " ");
			
			for (int j=1; j<=n; j++) {
				if (check[temp][j] == 1 && visited[j] == false) {
					queue.offer(j);
					visited[j] = true;
				}
			}
		}
		
		
	}

	private static void dfs(int i) {
		visited[i] = true;
		System.out.print(i + " ");
		for (int j=1; j<=n; j++) {
			if (check[i][j] == 1 && visited[j] == false) {
				dfs(j);
			}
		}
		
		
	}

}
