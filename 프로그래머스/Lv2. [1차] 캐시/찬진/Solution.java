package programmers.p17680;

import java.util.Deque;
import java.util.LinkedList;

class Solution {
	
	public static void main(String[] args) {
		Solution a = new Solution();
		int cacheSize = 3;
		String[] cities = {"Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"};
		System.out.println(a.solution(cacheSize, cities));
		
	}
    public int solution(int cacheSize, String[] cities) {
        int answer = 0;
        
        Deque<String> deque = new LinkedList<String>();
        if (cacheSize == 0) {
        	return cities.length * 5;
        }
        for (String s : cities) {
        	String str = s.toUpperCase();
        	if (deque.size() == cacheSize) {
        		if (deque.contains(str)) {
        			deque.remove(str);
        			deque.add(str);
        			answer += 1;
        		} else {
        			deque.poll();
        			deque.add(str);
        			answer += 5;
        		}
        	} else {
        		if (deque.contains(str)) {
        			deque.remove(str);
        			deque.add(str);
        			answer += 1;
        		} else {
        			deque.add(str);
        			answer += 5;
        		}
        	}
        }
        
        return answer;
    }
}