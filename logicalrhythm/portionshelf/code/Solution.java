import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t-- > 0) {
            int n = sc.nextInt();
            int[] a = new int[n];
            for (int i = 0; i < n; i++) a[i] = sc.nextInt();
            int max = Integer.MIN_VALUE;
            for (int v : a) max = Math.max(max, v);
            int second = Integer.MIN_VALUE; boolean found = false;
            for (int v : a) if (v < max) { second = Math.max(second, v); found = true; }
            System.out.println(found ? second : "NO BACKUP");
        }
    }
}