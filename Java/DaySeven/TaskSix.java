public class TaskSix {
public static void main(String[] args) {

for(int count = 1; count <= 10; count++){
	if(count % 4 == 0) {
		int number = count;
		for(int counter = 1; counter <= 5; counter++) {
			System.out.printf("%d ", number);
			number *= count;			
			}
}
}

}
}