# PowerShell script to apply Quantum Merlin branding to HTML files

$files = @(
    "chinese-zodiac-calculator.html",
    "moon-phase-calculator.html",
    "element-calculator.html",
    "birthstone-finder.html",
    "birth-flower-finder.html",
    "age-calculator.html",
    "aura-color-test.html",
    "birthday-countdown.html",
    "brain-type-test.html",
    "coin-flip.html",
    "color-generator.html",
    "color-personality-test.html",
    "crystal-ball.html",
    "daily-fortune.html",
    "decision-wheel.html",
    "dice-roller.html",
    "fortune-cookie.html",
    "life-progress.html",
    "lucky-numbers.html",
    "password-generator.html",
    "random-fact.html",
    "random-name-picker.html",
    "time-until.html",
    "yes-no-oracle.html"
)

$workingDir = "C:\Users\WIPED\funtools"

# Tool-card and input styles to replace
$oldToolCardBlock = @'
        .tool-card {
            background: white;
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0 15px 40px rgba(0, 0, 0, 0.2);
            margin-bottom: 30px;
        }
        .input-group { margin-bottom: 25px; }
        label { display: block; font-weight: 600; margin-bottom: 8px; color: #333; }
        input[type="text"], input[type="number"], input[type="date"], select {
            width: 100%;
            padding: 15px;
            border: 2px solid #e0e0e0;
            border-radius: 10px;
            font-size: 16px;
            transition: border-color 0.3s;
        }
        input:focus, select:focus { outline: none; border-color: #667eea; }
        button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 15px 40px;
            font-size: 18px;
            font-weight: 600;
            border-radius: 10px;
            cursor: pointer;
            transition: transform 0.3s, box-shadow 0.3s;
            width: 100%;
        }
        button:hover { transform: translateY(-2px); box-shadow: 0 10px 20px rgba(102, 126, 234, 0.4); }
'@

$newToolCardBlock = @'
        .tool-card {
            background: rgba(17, 24, 39, 0.7);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(6, 182, 212, 0.3);
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0 15px 40px rgba(0, 0, 0, 0.4);
            margin-bottom: 30px;
        }
        .input-group { margin-bottom: 25px; }
        label { 
            display: block; 
            font-family: 'Cinzel', serif;
            font-weight: 600; 
            margin-bottom: 8px; 
            color: #fbbf24;
        }
        input[type="text"], input[type="number"], input[type="date"], select {
            width: 100%;
            padding: 15px;
            background: rgba(17, 24, 39, 0.8);
            border: 2px solid rgba(6, 182, 212, 0.3);
            border-radius: 10px;
            font-size: 16px;
            font-family: 'Cormorant Garamond', serif;
            color: #e0e0e0;
            transition: all 0.3s;
        }
        input:focus, select:focus { 
            outline: none; 
            border-color: #06b6d4; 
            box-shadow: 0 0 20px rgba(6, 182, 212, 0.4);
        }
        button {
            background: linear-gradient(135deg, #06b6d4 0%, #8b5cf6 100%);
            color: white;
            border: none;
            padding: 15px 40px;
            font-size: 18px;
            font-family: 'Cinzel', serif;
            font-weight: 600;
            border-radius: 10px;
            cursor: pointer;
            transition: transform 0.3s, box-shadow 0.3s;
            width: 100%;
        }
        button:hover { transform: translateY(-2px); box-shadow: 0 10px 20px rgba(6, 182, 212, 0.4); }
'@

# Result styles to replace
$oldResultBlock = @'
        .result {
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            color: white;
            padding: 30px;
            border-radius: 15px;
            margin-top: 25px;
            display: none;
        }
        .result.show { display: block; animation: fadeIn 0.5s; }
        .result h3 { font-size: 2em; margin-bottom: 15px; }
        .result p { font-size: 1.1em; line-height: 1.6; }
        .back-btn { background: rgba(255, 255, 255, 0.2); margin-top: 20px; }
        .back-btn:hover { background: rgba(255, 255, 255, 0.3); }
'@

$newResultBlock = @'
        .result {
            background: rgba(17, 24, 39, 0.9);
            border: 2px solid transparent;
            border-image: linear-gradient(135deg, #fbbf24 0%, #ec4899 100%);
            border-image-slice: 1;
            border-radius: 15px;
            padding: 30px;
            margin-top: 25px;
            display: none;
            box-shadow: 0 0 30px rgba(251, 191, 36, 0.3);
        }
        .result.show { display: block; animation: fadeIn 0.5s; }
        .result h3 { 
            font-family: 'Cinzel Decorative', serif;
            font-size: 2em; 
            margin-bottom: 15px; 
            background: linear-gradient(135deg, #fbbf24 0%, #ec4899 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        .result p { 
            font-size: 1.1em; 
            line-height: 1.6; 
            color: #e0e0e0;
        }
        .back-btn { 
            background: rgba(6, 182, 212, 0.2); 
            border: 1px solid rgba(6, 182, 212, 0.3);
            margin-top: 20px; 
        }
        .back-btn:hover { 
            background: rgba(6, 182, 212, 0.3); 
            box-shadow: 0 0 20px rgba(6, 182, 212, 0.4);
        }
'@

# Share buttons
$oldShareBlock = @'
        .share-buttons { display: flex; gap: 10px; margin-top: 20px; justify-content: center; }
        .share-btn { background: #f0f0f0; color: #333; padding: 10px 20px; border-radius: 8px; cursor: pointer; transition: all 0.3s; }
        .share-btn:hover { background: #e0e0e0; }
'@

$newShareBlock = @'
        .share-buttons { display: flex; gap: 10px; margin-top: 20px; justify-content: center; }
        .share-btn { 
            background: rgba(6, 182, 212, 0.2); 
            border: 1px solid rgba(6, 182, 212, 0.3);
            color: #e0e0e0; 
            padding: 10px 20px; 
            border-radius: 8px; 
            cursor: pointer; 
            transition: all 0.3s; 
        }
        .share-btn:hover { 
            background: rgba(6, 182, 212, 0.3); 
            box-shadow: 0 0 15px rgba(6, 182, 212, 0.4);
        }
'@

# Back button text
$oldBackBtn = '← Back to All Tools'
$newBackBtn = '← Quantum Merlin Hub'

$successCount = 0
$errorCount = 0

foreach ($file in $files) {
    $filePath = Join-Path $workingDir $file
    
    if (Test-Path $filePath) {
        try {
            $content = Get-Content $filePath -Raw -Encoding UTF8
            
            # Apply replacements
            $content = $content.Replace($oldToolCardBlock, $newToolCardBlock)
            $content = $content.Replace($oldResultBlock, $newResultBlock)
            $content = $content.Replace($oldShareBlock, $newShareBlock)
            $content = $content.Replace($oldBackBtn, $newBackBtn)
            
            # Save file
            $content | Set-Content $filePath -Encoding UTF8 -NoNewline
            
            Write-Host "✓ Updated: $file" -ForegroundColor Green
            $successCount++
        }
        catch {
            Write-Host "✗ Error updating $file : $_" -ForegroundColor Red
            $errorCount++
        }
    }
    else {
        Write-Host "✗ File not found: $file" -ForegroundColor Yellow
        $errorCount++
    }
}

Write-Host "`nSummary:" -ForegroundColor Cyan
Write-Host "Successfully updated: $successCount files" -ForegroundColor Green
if ($errorCount -eq 0) {
    Write-Host "Errors: $errorCount files" -ForegroundColor Green
} else {
    Write-Host "Errors: $errorCount files" -ForegroundColor Red
}
