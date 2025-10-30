public class Functions {

public static void main(String[] args) {


/*
public static boolean[] Palindrome(String[] words) {



boolean[] result = new boolean[3];
result = Palindrome(new String[] {"madm", "racecar"});
for(int index = 0; index < result.length; index++) {
	System.out.print(result[index] + ",");
}
*/

String[] words = {"madam", "racecar", "length"};
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
	for(int index = 0; index < output.length; index++) {
		System.out.println(output[index]);}


		
}

}