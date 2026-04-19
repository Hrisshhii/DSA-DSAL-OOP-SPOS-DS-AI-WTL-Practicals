package servlet; 
 
import ejb.BankRemote; 
import java.io.IOException; 
import javax.ejb.EJB; 
import javax.servlet.*; 
import javax.servlet.http.*; 

public class BankServlet extends HttpServlet { 
    @EJB 
    private BankRemote bank; 
    protected void doPost(HttpServletRequest request, HttpServletResponse response) 
            throws ServletException, IOException { 

        String action = request.getParameter("action"); 
        double amount = Double.parseDouble(request.getParameter("amount")); 
        double balance = 0; 


        if (action.equals("deposit")) { 
            balance = bank.deposit(amount); 

        } else if (action.equals("withdraw")) { 
            if (amount > bank.getBalance()) { 
                request.setAttribute("message", "Insufficient Balance"); 
                request.getRequestDispatcher("error.jsp").forward(request, response); 
                return; 
            } 
            balance = bank.withdraw(amount); 
        } 
        request.setAttribute("balance", balance); 
        request.getRequestDispatcher("result.jsp").forward(request, response); 
    } 
} 
