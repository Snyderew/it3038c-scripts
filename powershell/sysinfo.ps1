function getIP{
    (get-netipaddress).ipv4address | Select-String "192*"
}

Write-Host(getIP)

$IP = getIP

Write-host("This machine's IP is $IP")

Write-Host("This machine's IP is {0}" -f $IP)