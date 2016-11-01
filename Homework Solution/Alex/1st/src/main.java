import java.util.Scanner;

public class main{
	public static void main(String args[]){
		median();
	}
	public static void median(){
		int b =0;
		int s = 0;
		int i;
		System.out.println("i need a number: ");
		while(b < 2){
			
			Scanner keyboard = new Scanner(System.in);
			int a = keyboard.nextInt();
			s = s+a;
			i= s/2;
			System.out.println("The median is "+i+". Do you wanna ad one more?: ");
		}
	}
}