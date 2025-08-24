SELECT 
    Name AS MenuName
FROM 
    littlelemondb.menu
WHERE 
    MenuID = ANY (
        SELECT 
            om.MenuID
        FROM 
            littlelemondb.ordermenu om
        WHERE 
            om.Quantity > 2
    );
