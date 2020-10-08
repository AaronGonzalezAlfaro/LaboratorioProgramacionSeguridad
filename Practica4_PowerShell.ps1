$PerfilNet = Get-NetConnectionProfile
$ConfigNet = Get-NetIPConfiguration
do
{
     cls
     Write-Host "-----MENU----" -ForegroundColor DarkYellow  
     Write-Host "[1]Informacion (General) de Coneccion" -ForegroundColor DarkGreen
     Write-Host "[2]Ver Perfil de la Red" -ForegroundColor DarkGreen
     Write-Host "[3]Ver Perfil de la Red" -ForegroundColor DarkGreen 
     Write-Host "[4]Ver Conexiones TCP" -ForegroundColor DarkGreen
     Write-Host "[5]Obtener la IP del Equipo" -ForegroundColor DarkGreen
     Write-Host "[6]Obtener la IP del Modem" -ForegroundColor DarkGreen
     Write-Host "[s]Salir" -ForegroundColor DarkCyan
     Write-Host "-------------" -ForegroundColor DarkYellow
     $opcion = Read-Host "Elegir una opcion: " 
     switch ($opcion) 
     { 
           '1' {
                cls
                Get-NetConnectionProfile | Format-List
                } 
           '2' { 
                cls  
                Write-Host "Nombre de la Red: " $PerfilNet.Name
                } 
           '3' { 
                cls
                Write-Host "Perfil de la Red: " $PerfilNet.NetworkCategory
                } 
           '4' {
                cls
                Get-NetTCPConnection | Format-Table -AutoSize
                } 
           '5' {
                cls
                Write-Host "IP del Equipo: " $ConfigNet.IPv4Adress.IPAdress
                }
           '6' {
                cls
                Write-Host "IP del Modem: " $ConfigNet.IPv4DefaultGateway.NextHop
                }
           's'{
                cls
                return
              }
           default{
               'Opcion No Encontrada'
           }
     }
     pause 
}
until ($opcion -eq 's')