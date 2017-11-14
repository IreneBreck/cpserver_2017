<!doctype html>
<html>

<head>
<meta charset="UTF-8">
<title>Attendance</title>
</head>

<body>

<%
    rows = [[v for v in range(0,10)] for row in range(0,10)]
%>
<table>
    % for row in rows:
        ${makerow(row)}
    % endfor
</table>

<%def name="makerow(row)">
    <tr>
        <td>fname</td>\
        <td>lname</td>\
        <td>email</td>\
        <td>phone</td>\
        <td>agent_q</td>\
        <td>seminar_q</td>\
        <td>land_q</td>\
        <td>when</td>\
        <td>where</td>
    </tr>
    <tr>
    % for name in row:
        <td>${name}</td>\
    % endfor
    </tr>
</%def>

</body>
</html>

