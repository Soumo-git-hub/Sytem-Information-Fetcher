# System Information Tool

## Overview
The **System Information Tool** is a Python-based utility designed to fetch, monitor, and display system information, including CPU, RAM, GPU, and operating system details. This tool also features real-time resource usage graphs and the ability to save a system report to a file. It's an excellent resource for users who want to monitor system performance or diagnose potential issues.

---

## Features
1. **View System Information**:
   - Displays details such as operating system, machine type, processor, hostname, and more.
   - Includes current CPU, RAM, and GPU usage.

2. **Threshold Monitoring**:
   - Monitors resource usage and warns if thresholds are exceeded:
     - CPU Usage > 80%
     - RAM Usage > 85%
     - GPU Usage > 80%

3. **Real-Time Graphs**:
   - Displays ASCII-based bar graphs for CPU and GPU usage.
   - Refreshes every 5 seconds for real-time monitoring.

4. **Save System Report**:
   - Saves all fetched system information and threshold warnings to a `system_report.txt` file.

---

## Prerequisites
- Python 3.0 or higher
- Required Python libraries:
  - `platform` (built-in)
  - `psutil` (`pip install psutil`)
  - `GPUtil` (`pip install gputil`)
  - `os` and `time` (built-in)

---

## Installation
1. Clone or download this repository.
2. Install the required Python libraries:
   ```bash
   pip install psutil gputil
   ```
3. Run the script:
   ```bash
   python system_info_tool.py
   ```

---

## Usage
1. Launch the program by running the script.
2. Choose from the following options in the menu:
   - `1`: View system information and monitor thresholds.
   - `2`: Save a detailed system report to `system_report.txt`.
   - `3`: Display real-time resource usage graphs. Press `Ctrl+C` to exit this mode.
   - `4`: Exit the program.

---

## Example Output
### System Information
```
System Information:
OS: Windows
OS Version: 10.0.19045
OS Release: 10
Machine: AMD64
Processor: Intel(R) Core(TM) i7-9700K CPU @ 3.60GHz
Hostname: User-PC
CPU Usage: 35.6%
Physical Cores: 8
Logical Cores: 8
RAM Usage: 42.3%
GPU: NVIDIA GeForce RTX 3080
GPU Usage: 25.6%

Threshold Monitoring:
- All systems running within normal thresholds.
```

### Real-Time Graph
```
Real-Time Graphs:
CPU Usage: [##########----------] 50.0%
GPU Usage: [######--------------] 30.0%
Press 'Ctrl+C' to exit.
```

---

## Files
- `system_info_tool.py`: Main Python script.
- `system_report.txt`: Generated file containing system information and threshold warnings.

---

## Notes
- Real-time graph mode may require additional system resources.
- Threshold values can be adjusted in the `monitor_thresholds` method within the script.

---

## Future Enhancements
- Add support for monitoring additional hardware components (e.g., disks, network).
- Include GUI-based visualization using libraries like `tkinter` or `PyQt`.

---

## License
This project is open-source and available under the MIT License. Feel free to use and modify it for personal or educational purposes.
