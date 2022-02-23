Function GetIP {

    $IP = Get-NetIPAddress | where-Object {$_.IPv4Address -like '192*'}

    return $IP.IPv4Address

    }