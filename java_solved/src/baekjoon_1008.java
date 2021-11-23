// 단계별 1-8 A / B
import java.util.Scanner;

public class baekjoon_1008 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String A = scanner.next();
        String B = scanner.next();
        System.out.println(Integer.parseInt(A) + Integer.parseInt(B));
        System.out.println(Integer.parseInt(A) - Integer.parseInt(B));
        System.out.println(Integer.parseInt(A) * Integer.parseInt(B));
        System.out.println(Integer.parseInt(A) / Integer.parseInt(B));
        System.out.println(Integer.parseInt(A) % Integer.parseInt(B));
    }
}
