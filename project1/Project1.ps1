function getDiskspace{
    [math]::Round((Get-PSDrive C).Free/1GB,2) 
}

$Diskspace = getDiskspace 

Write-host("You have $Diskspace GB of remaining disk space.")