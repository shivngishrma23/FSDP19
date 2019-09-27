use task1
go

select * from ['Fact  Employee Central Table$']

select p1.[Position_ID],
stuff( (SELECT ','+BU_SSU_Description 
FROM ['Fact  Employee Central Table$'] p2
WHERE p2.[Position_ID] = p1.[Position_ID]
ORDER BY BU_SSU_Description
FOR XML PATH(''), TYPE).value('.', 'varchar(max)'),1,1,'')
AS stuffed
FROM ['Fact  Employee Central Table$'] p1
GROUP BY [Position_ID] ;
------------------------------------------------------------------------
select * from ['Fact  Employee Central Table$']
select p1.[Position_ID],
stuff( (SELECT ','+BU_SSU_Description 
FROM ['Fact  Employee Central Table$'] p2
WHERE p2.[Position_ID] = p1.[Position_ID]
ORDER BY BU_SSU_Description
FOR XML PATH(''), TYPE).value('.', 'varchar(max)'),1,1,'')
AS stuffed
FROM ['Fact  Employee Central Table$'] p1
GROUP BY [BU_SSU_Description] ;
  

