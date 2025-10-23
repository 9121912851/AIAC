public class CheckNumber {
  public static String checkNumber(int num) {
    if (num > 0) return "positive";
    else if (num < 0) return "negative";
    else return "zero";
  }

  public static void main(String[] args) {
    int[] tests = { -5, 0, 7 };
    for (int n : tests) {
      System.out.println(n + " -> " + checkNumber(n));
    }
  }
}
