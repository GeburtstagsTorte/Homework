import java.util.Scanner;

public class main {
	public static void main(String args[]){
		
		isItPrime();
	}
	public static void isItPrime(){
		Scanner keyboard = new Scanner(System.in);
		int n = keyboard.nextInt();
		System.out.println(primes(n) <= 2);
	}
	public static int primes(int n){
		int a=0;
		int i=1;
		while(i <= n){
			int b = n%i;
			if(b == 0){
				a++;
			}
			i++;
		}
		return a;
	}
}
