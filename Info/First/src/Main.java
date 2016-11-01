import java.util.Scanner;
import java.io.*;

public class Main {
	
	
	public static void main(String args[]){

		// CODE HERE
	}
	
	public static int readInt(){
		Scanner keyboard = new Scanner(System.in);
		System.out.println("Your number: ");

		int nr = keyboard.nextInt();
		return nr;
	}
	
	@SuppressWarnings("resource")
	public static int readArrayFromKeyboard(int[] a){
		Scanner keyboard = new Scanner(System.in);
		System.out.println("The length of your array: ");
		int len = keyboard.nextInt();
		
		for(int i=1;i<=len;i++){
			System.out.println(new String("array[" + i + "]= "));
			a[i] = keyboard.nextInt();
		}
		
		return len;
	}
	
	public static int readArrayFromFile(int a[]){
		
		int len = 0;
		
		try (BufferedReader br = new BufferedReader(new FileReader("text.txt")))
		{

			String line = br.readLine();
			String[] numbers = line.split(" ");
			
			for(int i=0;i<=numbers.length - 1;i++)
				a[i+1] = Integer.parseInt(numbers[i]);
			
			len = numbers.length;
			
			
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		return len;
	}
	
	public static void printArray(int[] a, int len){
		for(int i=1;i<=len;i++)
			System.out.print(new String(a[i] + " "));
		System.out.println();
	}
	
	
}
