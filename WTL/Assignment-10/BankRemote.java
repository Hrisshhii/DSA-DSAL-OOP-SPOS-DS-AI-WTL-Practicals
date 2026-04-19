package ejb; 
import javax.ejb.Remote; 
@Remote 
public interface BankRemote { 
    double deposit(double amount); 
    double withdraw(double amount); 
    double getBalance(); 
} 
