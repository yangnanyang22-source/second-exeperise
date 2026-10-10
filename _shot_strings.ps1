$wshell = New-Object -ComObject wscript.shell
$activated = $wshell.AppActivate('exeperise2')
Write-Host "activated: $activated"
Start-Sleep -Milliseconds 800

# Ctrl+Shift+N 打开文件
$wshell.SendKeys('^+n')
Start-Sleep -Milliseconds 1200

# 输入文件名
$wshell.SendKeys('strings.xml')
Start-Sleep -Milliseconds 800

# 回车
$wshell.SendKeys('~')
Start-Sleep -Milliseconds 2000

# 截图
Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing
$bounds = [System.Windows.Forms.Screen]::PrimaryScreen.Bounds
$bmp = New-Object System.Drawing.Bitmap $bounds.Width, $bounds.Height
$g = [System.Drawing.Graphics]::FromImage($bmp)
$g.CopyFromScreen($bounds.Location, [System.Drawing.Point]::Empty, $bounds.Size)
$out = 'E:\Android exeperise\exeperise2\_shots\02_strings_xml.png'
$bmp.Save($out, [System.Drawing.Imaging.ImageFormat]::Png)
$g.Dispose(); $bmp.Dispose()
Write-Host "saved $out"
