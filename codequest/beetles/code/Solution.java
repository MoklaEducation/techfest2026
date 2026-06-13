import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t-- > 0) {
            int n = sc.nextInt();
            LinkedHashSet<Integer> seen = new LinkedHashSet<>();
            for (int i = 0; i < n; i++) seen.add(sc.nextInt());
            System.out.println("Count: " + seen.size());
            StringBuilder sb = new StringBuilder();
            for (int v : seen) { if (sb.length() > 0) sb.append(' '); sb.append(v); }
            System.out.println(sb);
        }
    }
}