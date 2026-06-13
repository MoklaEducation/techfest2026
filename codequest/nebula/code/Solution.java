import java.util.*;
import java.io.*;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine().trim());
        StringBuilder sb = new StringBuilder();
        while (t-- > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken()), k = Integer.parseInt(st.nextToken());
            int[] a = new int[n];
            st = new StringTokenizer(br.readLine());
            for (int i=0;i<n;i++) a[i]=Integer.parseInt(st.nextToken());
            Deque<Integer> dq = new ArrayDeque<>();
            for (int i=0;i<n;i++) {
                while (!dq.isEmpty()&&dq.peekFirst()<i-k+1) dq.pollFirst();
                while (!dq.isEmpty()&&a[dq.peekLast()]<=a[i]) dq.pollLast();
                dq.addLast(i);
                if (i>=k-1) {
                    if (i>k-1) sb.append(' ');
                    sb.append(a[dq.peekFirst()]);
                }
            }
            sb.append('\n');
        }
        System.out.print(sb);
    }
}