package leetCode;

public class PalindromeNum {

  public static void main(String[] args) {
    System.out.println(isPalindrome(1234321));
    System.out.println(isPalindrome(-1));
    System.out.println(isPalindrome(28));

  }
  
  static boolean isPalindrome(int x) {
    int rev = 0;
    for(int temp = x, remainder = x % 10; temp > 0; temp /= 10, remainder = temp % 10){
        rev = (rev * 10) + remainder;
    }
    
    return x == rev;
}

}
