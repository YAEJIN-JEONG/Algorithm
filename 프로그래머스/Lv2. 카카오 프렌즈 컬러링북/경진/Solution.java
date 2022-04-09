package programmers.coloring_book;

import java.util.LinkedList;
import java.util.Queue;

// https://programmers.co.kr/learn/courses/30/lessons/1829
public class Solution {

    private int count;              // 영역 개수
    private boolean[][] visited;    // 방문 여부

    public int[] solution(int m, int n, int[][] picture) {
        visited = new boolean[m][n];
        int area = 0;   // 영역 최대 넓이

        for(int x=0; x<m; x++) {
            for(int y=0; y<n; y++) {
                // 빈 곳이 아니고, 방문 하지 않은 곳이면 bfs
                if(picture[x][y] != 0 && !visited[x][y])
                    area = Math.max(area, bfs(picture, x, y, picture[x][y]));
            }
        }

        return new int[]{count, area};
    }

    // bfs 로 영역 탐색, 영역의 넓이 반환
    public int bfs(int[][] picture, int x, int y, int k) {
        int area = 1;   // 영역 넓이
        count++;        // 영역 개수 증가
        Queue<Integer> xq = new LinkedList<>();
        Queue<Integer> yq = new LinkedList<>();
        xq.add(x);
        yq.add(y);
        visited[x][y] = true;

        while(!xq.isEmpty()) {
            int cx = xq.poll();
            int cy = yq.poll();

            // 네 방향 탐색
            int[][] steps = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

            for(int[] step : steps) {
                int nx = cx + step[0];
                int ny = cy + step[1];
                // 범위 내, 같은 색으로 칠해진 곳이면 큐에 넣음
                if(nx>=0 && nx<picture.length && ny>=0 && ny<picture[0].length) {
                    if(picture[nx][ny] == k && !visited[nx][ny]) {
                        xq.add(nx);
                        yq.add(ny);
                        visited[nx][ny] = true;
                        area++;
                    }
                }
            }
        }

        return area;
    }
}
