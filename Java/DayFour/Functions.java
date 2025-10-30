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
	String reverse = "";
	for(int point = 0; point < words.length; point++) {
		String word = words[point];
		//System.out.println(word);
		reverse = "";
		System.out.print(reverse);
		for(int count = 0; count < word.length(); count++) {
			System.out.printf("%d %d", word.length(), count);
			reverse = word.charAt(count) + reverse;		
			int counter = 0;

			while(counter < output.length) {
	
				if(reverse.equalsIgnoreCase(word)) {
					output[counter] = true;}
				else if(!reverse.equalsIgnoreCase(word)) {
					output[counter] = false;}
			counter++;	
			}
			
			
	}	


	
	
	}

	System.out.print(output[0]);
	/*
	for(int index = 0; index < output.length; index++) {
		System.out.print(output[index]);
	}
	*/	
}

}