[Setup]
AppName=Aplicativo CSC
AppVersion=3.0.1
DefaultDirName={autopf}\Aplicativo CSC
DefaultGroupName=Aplicativo CSC
OutputDir=Output
OutputBaseFilename=setup_v1.0.0
Compression=lzma
SolidCompression=yes
ArchitecturesInstallIn64BitMode=x64
PrivilegesRequired=lowest
SetupIconFile=app_icon.ico

[Tasks]
Name: "desktopicon"; Description: "Crear un acceso directo en el escritorio"; GroupDescription: "Iconos adicionales:"

[Files]
Source: "dist\Aplicativo_CSC.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "app_icon.ico"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\Aplicativo CSC"; Filename: "{app}\Aplicativo_CSC.exe"; IconFilename: "{app}\app_icon.ico"
Name: "{group}\Desinstalar Aplicativo CSC"; Filename: "{uninstallexe}"
Name: "{autodesktop}\Aplicativo CSC"; Filename: "{app}\Aplicativo_CSC.exe"; IconFilename: "{app}\app_icon.ico"; Tasks: desktopicon

[Run]
Filename: "{app}\Aplicativo_CSC.exe"; Description: "Lanzar Aplicativo CSC"; Flags: nowait postinstall
