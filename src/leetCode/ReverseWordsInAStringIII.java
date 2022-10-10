package leetCode;

/*
 * Given a string s, reverse the order of characters in each word within a sentence while still
 * preserving whitespace and initial word order.
 */

public class ReverseWordsInAStringIII {

  public static void main(String[] args) {
    String testOne = "Let's take LeetCode contest";
    String testTwo = "God Ding";
    String resultOne = "s'teL ekat edoCteeL tsetnoc";
    String resultTwo = "doG gniD";
    
    System.out.println(reverseWords(testOne).equals(resultOne));
    System.out.println(reverseWords(testTwo).equals(resultTwo));
  }
  
  static String reverseWords(String s) {
    String[] strArray = s.split(" ");
    StringBuilder answer = new StringBuilder();
    for(int i = 0; i < strArray.length; i++){
        StringBuilder wordbuilder = new StringBuilder();
        wordbuilder.append(strArray[i]);
        wordbuilder.reverse();
        answer.append(wordbuilder);
        if(i < strArray.length - 1){
            answer.append(" ");
        }  
    }
    
    return answer.toString();
}

}
