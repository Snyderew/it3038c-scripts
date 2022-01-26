function getIP{
    (get-netipaddress).ipv4address | Select-String "192*"
}

$IP = getIP

$User = $env:Username

$CN = $env:ComputerName

function getVer{
    ($HOST.version).Major
}

$ver = getver

function getDMY{
    get-date -format "dddd, MMMM dd, yyyy"
}

$DMY = getDMY

$BODY = "This machine's IP is $IP. User is $User. Hostname is $CN. PowerShell $ver. Today's Date is $DMY."

Send-MailMessage -To "leonardf@ucmail.uc.edu" -From "edsnyder99@gmail.com" -Subject "IT3038C Windows SysInfo" -Body $BODY -SmtpServer smtp.gmail.com -port 587 -UseSSL -Credential (Get-Credential)
