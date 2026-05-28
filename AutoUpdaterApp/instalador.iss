[Setup]
AppName=Aplicativo CSC
AppVersion=1.6.9
DefaultDirName={autopf}\Aplicativo CSC
DefaultGroupName=Aplicativo CSC
OutputDir=C:\Users\AFCASTROM\Documents\! COMPENSAR\01. DESARROLLOS\09. Venta aplicativo CSC\AutoUpdaterApp\Output
OutputBaseFilename=setup_v1.6.9
Compression=lzma
SolidCompression=yes
ArchitecturesInstallIn64BitMode=x64
PrivilegesRequired=lowest
SetupIconFile=C:\Users\AFCASTROM\Documents\! COMPENSAR\01. DESARROLLOS\09. Venta aplicativo CSC\AutoUpdaterApp\app_icon.ico

[Tasks]
Name: "desktopicon"; Description: "Crear un acceso directo en el escritorio"; GroupDescription: "Iconos adicionales:"

[Files]
Source: "C:\Users\AFCASTROM\Documents\! COMPENSAR\01. DESARROLLOS\09. Venta aplicativo CSC\AutoUpdaterApp\dist\Aplicativo_CSC.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\Aplicativo CSC"; Filename: "{app}\Aplicativo_CSC.exe"
Name: "{group}\Desinstalar Aplicativo CSC"; Filename: "{uninstallexe}"
Name: "{autodesktop}\Aplicativo CSC"; Filename: "{app}\Aplicativo_CSC.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\Aplicativo_CSC.exe"; Description: "Lanzar Aplicativo CSC"; Flags: nowait postinstall skipifsilent
