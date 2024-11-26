import platform
import psutil
import GPUtil
import os
import time


class SystemInfoFetcher:
    def __init__(self):
        self.info = {}

    def fetch_info(self):
        """Fetch all system information and display a progress message."""
        print("Fetching system information... Please wait.")
        self.info["OS"] = platform.system()
        self.info["OS Version"] = platform.version()
        self.info["OS Release"] = platform.release()
        self.info["Machine"] = platform.machine()
        self.info["Processor"] = platform.processor()
        self.info["Hostname"] = platform.node()

        self.info["CPU Usage"] = psutil.cpu_percent(interval=1)
        self.info["Physical Cores"] = psutil.cpu_count(logical=False)
        self.info["Logical Cores"] = psutil.cpu_count(logical=True)

        memory = psutil.virtual_memory()
        self.info["RAM Usage"] = memory.percent

        gpus = GPUtil.getGPUs()
        if gpus:
            self.info["GPU"] = gpus[0].name
            self.info["GPU Usage"] = gpus[0].load * 100
        else:
            self.info["GPU"] = "No GPU detected"
            self.info["GPU Usage"] = 0

    def monitor_thresholds(self):
        """Check if system usage exceeds thresholds."""
        thresholds = {"CPU": 80, "RAM": 85, "GPU": 80}
        messages = []
        if self.info["CPU Usage"] > thresholds["CPU"]:
            messages.append("Warning: High CPU Usage!")
        if self.info["RAM Usage"] > thresholds["RAM"]:
            messages.append("Warning: High RAM Usage!")
        if self.info["GPU Usage"] > thresholds["GPU"]:
            messages.append("Warning: High GPU Usage!")
        return messages if messages else ["All systems running within normal thresholds."]

    def display_graph(self, usage_percentage, label):
        """Display a simple ASCII-based bar graph for resource usage."""
        bar_length = 20
        num_hashes = int(bar_length * (usage_percentage / 100))
        graph = "#" * num_hashes + "-" * (bar_length - num_hashes)
        print(f"{label}: [{graph}] {usage_percentage:.1f}%")


def save_report(fetcher):
    """Save system information to a .txt file."""
    fetcher.fetch_info()
    with open("system_report.txt", "w") as file:
        file.write("System Information Report:\n")
        for key, value in fetcher.info.items():
            file.write(f"{key}: {value}\n")
        file.write("\nThreshold Monitoring:\n")
        for msg in fetcher.monitor_thresholds():
            file.write(f"- {msg}\n")
    print("System report saved to 'system_report.txt'.")


def display_realtime_graphs(fetcher):
    """Display real-time graphs for resource usage."""
    while True:
        fetcher.fetch_info()
        os.system("cls" if os.name == "nt" else "clear")
        print("Real-Time Graphs:")
        fetcher.display_graph(fetcher.info["CPU Usage"], "CPU Usage")
        fetcher.display_graph(fetcher.info["GPU Usage"], "GPU Usage")
        print("\nPress 'Ctrl+C' to exit.")
        time.sleep(5)  # Refresh every 5 seconds


def main():
    fetcher = SystemInfoFetcher()

    while True:
        print("\nSystem Information Tool")
        print("1. View System Information")
        print("2. Save System Report")
        print("3. Display Real-Time Graphs")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            fetcher.fetch_info()
            print("\nSystem Information:")
            for key, value in fetcher.info.items():
                print(f"{key}: {value}")
            print("\nThreshold Monitoring:")
            for msg in fetcher.monitor_thresholds():
                print(f"- {msg}")

        elif choice == "2":
            save_report(fetcher)

        elif choice == "3":
            try:
                display_realtime_graphs(fetcher)
            except KeyboardInterrupt:
                print("\nExiting real-time graphs...")

        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
