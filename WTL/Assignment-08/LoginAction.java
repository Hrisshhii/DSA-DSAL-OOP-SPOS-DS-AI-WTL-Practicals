package action;

import com.opensymphony.xwork2.ActionSupport;

public class LoginAction extends ActionSupport {

    private String name;
    private String mobile;
    private String email;

    // Getters & Setters
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }

    public String getMobile() { return mobile; }
    public void setMobile(String mobile) { this.mobile = mobile; }

    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }

    // Execute method
    public String execute() {
        return SUCCESS;
    }

    // Validation
    public void validate() {

        // Name validation
        if (name == null || name.trim().isEmpty()) {
            addFieldError("name", "Name is required");
        } else if (!name.matches("[a-zA-Z ]+")) {
            addFieldError("name", "Name should contain only alphabets");
        }

        // Mobile validation
        if (mobile == null || mobile.trim().isEmpty()) {
            addFieldError("mobile", "Mobile number is required");
        } else if (!mobile.matches("\\d{10}")) {
            addFieldError("mobile", "Mobile must be 10 digits");
        }

        // Email validation
        if (email == null || email.trim().isEmpty()) {
            addFieldError("email", "Email is required");
        } else if (!email.matches("^[A-Za-z0-9+_.-]+@(.+)$")) {
            addFieldError("email", "Invalid email format");
        }
    }
}
