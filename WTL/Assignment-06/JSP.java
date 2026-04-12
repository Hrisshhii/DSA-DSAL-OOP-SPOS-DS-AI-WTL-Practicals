<%@ page import="java.sql.*" %>
<html>
<body>

<h2>Students Information</h2>

<table border="1">
    <tr>
        <th>ID</th>
        <th>Name</th>
        <th>Class</th>
        <th>Division</th>
        <th>City</th>
    </tr>

<%
try {
    Class.forName("com.mysql.cj.jdbc.Driver");
    Connection con = DriverManager.getConnection(
        "jdbc:mysql://localhost:3306/college_db",
        "root",
        "Root@123"
    );

    Statement stmt = con.createStatement();
    ResultSet rs = stmt.executeQuery("SELECT * FROM students_info");

    while(rs.next()) {
%>
    <tr>
        <td><%=rs.getInt(1) %></td>
        <td><%=rs.getString(2) %></td>
        <td><%=rs.getString(3) %></td>
        <td><%=rs.getString(4) %></td>
        <td><%=rs.getString(5) %></td>
    </tr>
<%
    }
    con.close();
}
catch(Exception e) {
    out.println(e);
}
%>
</table>

</body>
</html>
