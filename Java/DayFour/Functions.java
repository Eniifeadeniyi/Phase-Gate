import java.util.Arrays;
public class Functions {

public static void main(String[] args) {

boolean[] answer = Palindrome(new String[] {"madam", "racecar", "length"});
System.out.print(Arrays.toString(answer));
}

public static boolean[] Palindrome(String[] words) {
	boolean[] output = new boolean[words.length];
	for(int point = 0; point < words.length; point++) {
		String word = words[point];
		String reverse = "";
		for(int count = 0; count < word.length(); count++) {
			reverse = word.charAt(count) + reverse;	
		}

		if(reverse.equalsIgnoreCase(word)) {
			output[point] = true;}		
	}
	return output;
}

		

}