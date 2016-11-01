import java.util.Scanner;

public class main {
	
	public static void main(String args[]){
		
		System.out.println("enter Number :");
		squares();
		
	}
	
	public static void squares(){
		
		Scanner keyboard = new Scanner(System.in);
		int n = keyboard.nextInt();
		int i =1;
		while(i<=n){
			System.out.print(((i*2)*(i*2))+" ");
			i++;
			
		}
	}
}
