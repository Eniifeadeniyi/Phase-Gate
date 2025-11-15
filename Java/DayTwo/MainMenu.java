public class MainMenu {

public static void main(String[] args) {
/*
//1
String word =  "abcdefd";
String ch = "d";
int position = word.indexOf(ch);
String reverse = "";
String letters = word.substring(0,position+1);
for(int i = 0; i < letters.length(); i++) {
reverse = letters.charAt(i) + reverse;
}
reverse += word.substring(position+1,word.length());
System.out.print(reverse);
*/


//5
String word = "OpenAI";
String ch = "a";
char[] characters = word.toCharArray();
int counter = 0;
String[] letters = new String[characters.length];
for (int i = 0; i < characters.length; i++) {
    letters[i] = String.valueOf(characters[i]);
}
for(String letter : letters) {
	if(letter.equalsIgnoreCase(ch)) {
		counter += 1;
	}
}
System.out.print(counter);



/*
int[] unique = new int[numbers.length];
for(int number : numbers) {
	int count = numbers.indexOf(number);
	int counter = numbers.lastIndexOf(number);
	if(count == counter) unique[0] = number;	}

}

public static String[] split(String word) {
	String[] unique = new String[word.length()];
	for(int count = 0; count < word.length(); count++) {
		unique[count] = word.charAt(count);
	}
	return unique;
}
	
*/

}
}