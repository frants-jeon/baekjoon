import java.util.Scanner;

public class baekjoon_10430 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int A = Integer.parseInt(scanner.next());
        int B = Integer.parseInt(scanner.next());
        int C = Integer.parseInt(scanner.next());
        System.out.println((A + B) % C);
        System.out.println(((A % C) + (B % C)) % C);
        System.out.println(A * B % C);
        System.out.println(((A % C) * (B % C)) % C);
    }
}