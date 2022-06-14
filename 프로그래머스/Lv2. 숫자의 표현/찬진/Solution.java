package programmers.p12924;

//https://programmers.co.kr/learn/courses/30/lessons/12924?language=java
class Solution {
    public static void main(String[] args) {
        Solution a = new Solution();
        int n = 15;
        System.out.println(a.solution(n));
    }
    public int solution(int n) {
        int count = 0;
        for (int i=1; i<n; i++) {
            int sum = i+1;
            for (int j=i+2; sum+i<=n; j++) {
                if (i+sum == n) {
                    count++;
                }
                sum += j;
            }
        }
        return count+1;
    }
}