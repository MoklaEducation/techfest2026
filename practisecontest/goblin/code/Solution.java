import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();

        for (int caseNum = 0; caseNum < t; caseNum++) {
            int n = sc.nextInt();
            int[] boxes = new int[n];

            for (int i = 0; i < n; i++) {
                boxes[i] = sc.nextInt();
            }

            int m = sc.nextInt();

            long evenTotal = 0;
            int bigBoxes = 0;

            for (int value : boxes) {
                if (value % 2 == 0) {
                    evenTotal += value;
                }
                if (value >= m) {
                    bigBoxes++;
                }
            }

            System.out.print("Even total = " + evenTotal + ", Big boxes = " + bigBoxes);
            if (caseNum < t - 1) {
                System.out.println();
            }
        }
    }
}
