SELECT 
    c.CustomerID,
    c.Name AS FullName,
    o.OrderID,
    o.TotalCost AS Cost,
    m.Name AS MenuName,
    m.Category AS CourseName
FROM 
    littlelemondb.orders o
    JOIN littlelemondb.bookings b ON o.BookingID = b.BookingID
    JOIN littlelemondb.customers c ON b.CustomerID = c.CustomerID
    JOIN littlelemondb.ordermenu om ON o.OrderID = om.OrderID
    JOIN littlelemondb.menu m ON om.MenuID = m.MenuID
WHERE 
    o.TotalCost > 150
ORDER BY 
    o.TotalCost ASC;
