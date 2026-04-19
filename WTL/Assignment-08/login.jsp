<%@ taglib prefix="s" uri="/struts-tags" %>

<html>
<head>
<title>Login Page</title>

<style>
body {
    font-family: Arial;
    background: linear-gradient(to right, #74ebd5, #ACB6E5);
}

.container {
    width: 350px;
    margin: 100px auto;
    padding: 25px;
    background: white;
    border-radius: 10px;
    text-align: center;
}

h2 {
    margin-bottom: 20px;
}

input {
    width: 90%;
    padding: 10px;
    margin: 8px 0;
}

.error {
    color: red;
    font-size: 14px;
}

button {
    padding: 10px 20px;
    background: #2c3e50;
    color: white;
    border: none;
    cursor: pointer;
}

button:hover {
    background: #34495e;
}
</style>

</head>

<body>

<div class="container">
    <h2>Login Form</h2>

    <s:form action="login">

        <s:textfield name="name" placeholder="Enter Name"/>
        <div class="error">
            <s:fielderror fieldName="name"/>
        </div>

        <s:textfield name="mobile" placeholder="Enter Mobile Number"/>
        <div class="error">
            <s:fielderror fieldName="mobile"/>
        </div>

        <s:textfield name="email" placeholder="Enter Email"/>
        <div class="error">
            <s:fielderror fieldName="email"/>
        </div>

        <button type="submit">Login</button>

    </s:form>
</div>

</body>
</html>
