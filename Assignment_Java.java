import java.util.*;
public class Account {

	int accno;
	String name;
	long phoneno;
	float balance;
	Account()
	{
		balance=0;
	}
	void getinput()
	{
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter the accno,name,phoneno: ");
		accno=sc.nextInt();
		name=sc.next();
		phoneno=sc.nextLong();
	}
	void deposit()
	{
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter the deposit amt: ");
		int balance1=sc.nextInt();
		balance=balance+balance1;
		System.out.println("Withdrawn.Updated balance: "+balance);
	}
	void withdraw()
	{
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter the withdrawl amt: ");
		int withdraw1=sc.nextInt();
		balance=balance-withdraw1;
		System.out.println("Withdrawn.Updated balance: "+balance);
	}
	public static void main(String[] args) {
		
		// TODO Auto-generated method stub
		Account acc=new Account();
		while(true)
		{
			System.out.println("1.Enter details ");
			System.out.println("2.Deposit");
			System.out.println("3.Withdraw ");
			Scanner sc=new Scanner(System.in);
			System.out.println("Enter the option: ");
			int option=sc.nextInt();
			if (option==1)
			{
				acc.getinput();
			}
			else if (option==2)
			{
				acc.deposit();
			}
			else if (option==3)
			{
				acc.withdraw();
			}
			else
			{
				break;
			}
				
		}
		
		

	}

}
