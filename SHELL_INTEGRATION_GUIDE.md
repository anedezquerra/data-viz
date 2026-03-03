# Shell Integration Setup Guide

## Overview

Shell integration has been configured to improve command detection, execution, and terminal experience in VS Code. This enables better PowerShell integration, improved Python environment handling, and enhanced command resolution.

## What's Been Configured

### 1. **VS Code Settings (.vscode/settings.json)**

#### Terminal Shell Integration Features
- ✅ `terminal.integrated.shellIntegration.enabled` - Main integration feature
- ✅ `terminal.integrated.shellIntegration.decorationsEnabled` - Visual command status indicators
- ✅ `terminal.integrated.detectLocale` - Automatic locale detection
- ✅ `terminal.integrated.fastPtyDetection` - Faster terminal detection

#### PowerShell Configuration
- **Default Profile**: PowerShell (not CMD)
- **Automation Shell**: `pwsh` (PowerShell Core if available)
- **Environment Inheritance**: Full inheritance from system environment
- **Command Detection**: Enhanced with environment change indicators

#### Python Integration
- Proper interpreter path detection
- Direct file execution support
- Module path configuration for dataviz package

### 2. **Workspace Configuration (data-viz.code-workspace)**

Central workspace file containing:
- Folder structure definition
- Shared settings across all VS Code windows
- Launch configurations for debugging
- Python testing setup (pytest)
- Recommended extensions list

### 3. **PowerShell Profile (.vscode/profile.ps1)**

Loaded automatically on terminal startup to:
- Enable PSReadLine enhancements (history, intellisense)
- Set up Python virtual environment helpers
- Configure custom aliases (`ll`, `clear`, `cd..`)
- Enhance prompt with admin indicator and colors
- Display Python and PowerShell versions on startup
- Enable shell integration markers for better command tracking

### 4. **Debug Configuration (.vscode/launch.json)**

Pre-configured launch profiles:
- **Python: Current File** - Debug active Python script
- **Python: Module** - Debug as module
- **Pytest: Current File** - Run tests for current file
- **Pytest: All Tests** - Full test suite execution

## Benefits

### Command Detection Improvements
✅ Commands now properly detected in terminal output
✅ Command completion status tracked visually
✅ Error and exit codes properly captured
✅ PowerShell command resolution enhanced

### Terminal Experience
✅ Better integration with VS Code features
✅ Python virtual environment auto-detection
✅ Git integration helpers built-in
✅ Colored output and formatted prompts

### Python Development
✅ Automatic venv detection
✅ Direct pytest execution
✅ Integrated debugging support
✅ Package import path configuration

## Usage

### Terminal Integration
Simply open a terminal in VS Code (Ctrl+\`) and:
- Commands will be properly tracked
- Exit codes displayed
- Error decorations shown inline
- PowerShell aliases available

### Python Environment
```powershell
# Activate virtual environment
Activate-Venv
# or
Activate-Venv c:\path\to\venv

# Run tests
python -m pytest tests/ -v

# Use Python directly with shell integration
python your_script.py
```

### Quick Navigation
```powershell
# List files
ll

# Go to parent directory
cd..

# Clear screen properly
clear
```

### Git Integration
```powershell
# Formatted git status
gst
```

## Verifying Setup

### Check Terminal Integration Status
1. Open terminal (Ctrl+`)
2. Look for PowerShell profile message confirming load
3. Verify Python version displays correctly
4. Run a command and observe command decoration indicators

### Test Command Detection
```powershell
# This should be properly detected
python -c "print('Hello from shell integration')"

# Error should be properly captured
pwsh -Command "exit 1"
```

### Verify Python Environment
```powershell
python --version
pip list | Select-Object -First 5
```

## Troubleshooting

### Issue: Profile Not Loading
**Solution**: Check if PowerShell execution policy allows scripts
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Issue: Commands Not Detected
**Solution**: Reload VS Code window
- Press `Ctrl+Shift+P`
- Type "Developer: Reload Window"
- Press Enter

### Issue: Virtual Environment Not Recognized
**Solution**: Explicitly call activation
```powershell
./venv/Scripts/Activate.ps1
```

### Issue: Python Not Found in Terminal
**Solution**: Verify Python in PATH or use full path
```powershell
& "C:\Users\YourUsername\AppData\Local\Programs\Python\Python310\python.exe" --version
```

## Next Steps

1. **Close and Reopen VS Code** - Required to load workspace file
2. **Reload Window** - Ensures all settings are applied
3. **Open Terminal** - Verify shell integration is working
4. **Run Tests** - Test Python environment detection

## Configuration Files Structure

```
.vscode/
├── settings.json          # Main VS Code settings
├── launch.json            # Debug configurations
├── profile.ps1            # PowerShell profile
└── extensions.json        # Extension recommendations (auto-generated)

data-viz.code-workspace    # Workspace configuration (root level)
```

## References

- [VS Code Terminal Integration](https://code.visualstudio.com/updates/v1_80#_terminal-shell-integration)
- [PowerShell in VS Code](https://code.visualstudio.com/docs/languages/powershell)
- [Python in VS Code](https://code.visualstudio.com/docs/languages/python)

---

**Configuration Date**: 2026-03-03
**PowerShell Version Required**: 5.1+ (Windows PowerShell) or 7.0+ (PowerShell Core)
**VS Code Version Required**: 1.80+
