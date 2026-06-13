import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t-- > 0) {
            int n = sc.nextInt(), k = sc.nextInt();
            int[] a = new int[n];
            for (int i = 0; i < n; i++) a[i] = sc.nextInt();
            long[] prefix = new long[n + 1], suffix = new long[n + 1];
            for (int i = 0; i < n; i++) prefix[i+1] = prefix[i] + a[i];
            for (int i = 0; i < n; i++) suffix[i+1] = suffix[i] + a[n-1-i];
            long best = Long.MIN_VALUE;
            for (int left = 0; left <= k; left++)
                best = Math.max(best, prefix[left] + suffix[k - left]);
            System.out.println(best);
        }
    }
}