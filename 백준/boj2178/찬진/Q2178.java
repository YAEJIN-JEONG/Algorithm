package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

//https://www.acmicpc.net/problem/2178
public class Q2178 {
	
	private static int[][] maze;
	private static int n;
	private static int m;
	
	public static void main(String[] args) throws Exception {
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		String[] str = reader.readLine().split(" ");
		n = Integer.parseInt(str[0]);
		m = Integer.parseInt(str[1]);
		maze = new int[n][m];
		for (int i=0; i<n; i++) {
			String num = reader.readLine();
			for (int j=0; j<num.length(); j++) {
				maze[i][j] = num.charAt(j) - '0';
			}
		}
		
		bfs(0, 0);
		System.out.println(maze[n-1][m-1]);
		
		
	}

	private static void bfs(int startX, int startY) {
		Queue<int[]> queue = new LinkedList<int[]>();
		queue.offer(new int[] {startX, startY});
		int[] x = {1, -1, 0, 0};
		int[] y = {0, 0, 1, -1};
		
		while(!queue.isEmpty()) {
			int[] temp = queue.poll();
			int nowX = temp[0];
			int nowY = temp[1];
			
			for (int i=0; i<4; i++) {
				int nextX = nowX + x[i];
				int nextY = nowY + y[i];
				
				if (nextX < 0 || nextY < 0 || nextX >= n || nextY >= m) {
					continue;
				}
				
				if (maze[nextX][nextY] == 1) {
					queue.offer(new int[] {nextX, nextY});
					maze[nextX][nextY] = maze[nowX][nowY] + 1;
				}
			}
		}
		
		
		
	}



}
