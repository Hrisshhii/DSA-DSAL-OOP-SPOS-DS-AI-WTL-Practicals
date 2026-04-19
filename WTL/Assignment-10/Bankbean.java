package ejb; 
import javax.ejb.Stateless; 
@Stateless 
public class BankBean implements BankRemote { 
    private double balance = 1000; 
    public double deposit(double amount) { 
        balance += amount; 
        return balance; 
    } 
  
    public double withdraw(double amount) { 
        if (amount <= balance) { 
            balance -= amount; 
        } 
        return balance; 
    } 
  
    public double getBalance() { 
        return balance; 
    } 
} 
