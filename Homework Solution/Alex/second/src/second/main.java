
package second;
import java.util.Scanner;

public class Main {
	public static void main(String args[]){
		
	}
	
	public static void evens(){
		Scanner keyboard = new Scanner(System.in);
		System.out.println("what is n?:");
		int i=0;
		int n = keyboard.nextInt();
		System.out.println("the numbers are: "+0+" ");
		while(i < n-1){
			System.out.println(i*2+" ");
			i--;
		}
		/*or
		 * while(n!=0){
		 * 	System.out.println(n*2);
		 * 	n--;
		 * }
		 * */
	}
}
