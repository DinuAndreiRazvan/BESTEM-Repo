/* Penguin Squad */

import java.util.*;

public class Problema_3 {
    static int n;
    static ArrayList<TreeSet<Integer>> allSets;

    public static int isInASet(int a) {
        for (int i = 0; i < allSets.size(); i++) {
            if (allSets.get(i).contains(a)) {
                return i;
            }
        }

        return -1;
    }

    public static int findInSets(int a, int b) {
        for (int i = 0; i < allSets.size(); i++) {
            if (deleteSet(a, b, i)) return 1;

            if (deleteSet(b, a, i)) return 1;
        }
        return 0;
    }

    private static boolean deleteSet(int a, int b, int i) {
        if (allSets.get(i).contains(a)) {
            int index = isInASet(b);
            if (index != -1) {
                if (index != i) {
                    allSets.get(i).addAll(allSets.get(index));
                    allSets.remove(index);
                }
            } else {
                allSets.get(i).add(b);
                n--;
            }
            return true;
        }
        return false;
    }public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        int t, a, b;

        Scanner scanner = new Scanner(System.in);
        allSets = new ArrayList<>();

        n = scanner.nextInt();
        t = scanner.nextInt();

        a = scanner.nextInt();
        b = scanner.nextInt();

        TreeSet<Integer> set = new TreeSet<>();
        set.add(a);
        set.add(b);
        allSets.add(set);
        n -= 2;

        for (int i = 0; i < t - 1; i++) {
            a = scanner.nextInt();
            b = scanner.nextInt();

            if (findInSets(a, b) == 0) {
                TreeSet<Integer> newset = new TreeSet<>();
                newset.add(a);
                newset.add(b);
                allSets.add(newset);
                n -= 2;
            }

        }

        int result = 0;

        for (int i = 0; i < allSets.size() - 1; i++) {
            for (int j = i + 1; j < allSets.size(); j++) {
                result += allSets.get(i).size() * allSets.get(j).size();
            }
            result += allSets.get(i).size() * n;
        }

        result += allSets.get(allSets.size() - 1).size() * n;

        result += n * (n - 1) / 2;

        System.out.println(result);
    }
}