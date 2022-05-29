package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

//https://www.acmicpc.net/problem/1927
public class Q1927 {
	
	public static void main(String[] args) throws Exception {
		
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(reader.readLine());
		PriorityQueue<Integer> pqueue = new PriorityQueue<Integer>();
		
		for (int i=0; i<n; i++) {
			int x = Integer.parseInt(reader.readLine());
			if (x == 0) {
				if (pqueue.isEmpty()) {
					System.out.println(0);
				} else {
					System.out.println(pqueue.poll());
				}
			} else {
				pqueue.offer(x);
			}
		}
	}

}
