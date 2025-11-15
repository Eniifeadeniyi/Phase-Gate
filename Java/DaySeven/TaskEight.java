public class TaskEight {
public static void main(String[] args) {

int total = 0;
for(int count = 1; count <= 10; count++){
	if(count % 4 == 0) {
		int number = count;
		int sum = 0;
		for(int counter = 1; counter <= 5; counter++) {
			sum += number;
			number *= count;	
			}
		total += sum;
		
	
}
}
System.out.print(total);
}
}