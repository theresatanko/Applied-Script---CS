### Description
This exercise tests how antivirus and EDR systems respond to the EICAR standard test signature to verify that security protections function correctly. The script serves as a safe, controlled verification tool for Windows systems, using the completely harmless EICAR test string that is designed to trigger antivirus detection without causing any system harm.


### Script Functionality
- Confirms Windows operating system environment
- Creates test file with EICAR signature on Desktop
- Pauses briefly for AV/EDR scanning detection window
- Verifies file status: Remains accessible and unmodified & removed or isolated by security software
- Detects file modifications or access restrictions
- Displays protection status with success/failure indicators

### Tools
- Programming Language: Python 3
- Operating System: Windows (ntended for Windows Defender + Event Viewer)
- Security: Active antivirus/EDR (Windows Defender is optimal)

  
