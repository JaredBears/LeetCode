package leetCode;

public class UniquePaths {

  public static void main(String[] args) {
    System.out.println(uniquePaths(3, 7) == 28);

  }
  
  /* TODO: Is not fast enough for all test cases on LeetCode
   *       Need to learn dynamic programming
   */
  static int uniquePaths(int m, int n) {
    if (m == 1 || n == 1) {
      return 1;
    }
    return uniquePaths(m - 1, n) + uniquePaths(m, n - 1);
  }

}
