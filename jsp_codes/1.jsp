<%@ page import="java.util.*" %>
<HTML>
    <BODY>
        <%
        // This scriptlet declares and initializes "date"
        System.out.println( "Evaluating date now" );
        java.util.Date date = new java.util.Date();
        %>
        Hello!  The time is now
        <%
        out.println( date );
        out.println( "<br>Her machine's address is " );
        out.println( request.getRemoteHost());
        %>
    </BODY>
</HTML>