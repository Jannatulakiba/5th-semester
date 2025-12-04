import subprocess
import threading
import re
import tkinter as tk
from tkinter import ttk, messagebox, filedialog


class TracerouteGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Traceroute Lab (Windows) - Python GUI")
        self.geometry("820x520")
        self.minsize(760, 480)

        self._build_ui()
        self.process = None
        self.running = False

    def _build_ui(self):
  
        top = ttk.Frame(self, padding=12)
        top.pack(fill="x")

        ttk.Label(top, text="Target Host / IP:").pack(side="left")
        self.target_var = tk.StringVar(value="github.com")
        self.target_entry = ttk.Entry(top, textvariable=self.target_var, width=40)
        self.target_entry.pack(side="left", padx=8)

        self.start_btn = ttk.Button(top, text="Start Traceroute", command=self.start_traceroute)
        self.start_btn.pack(side="left", padx=5)

        self.stop_btn = ttk.Button(top, text="Stop", command=self.stop_traceroute, state="disabled")
        self.stop_btn.pack(side="left", padx=5)

        self.clear_btn = ttk.Button(top, text="Clear", command=self.clear_output)
        self.clear_btn.pack(side="left", padx=5)

        self.save_btn = ttk.Button(top, text="Save Output", command=self.save_output)
        self.save_btn.pack(side="left", padx=5)

  
        opts = ttk.Frame(self, padding=(12, 0))
        opts.pack(fill="x")

        ttk.Label(opts, text="Max Hops:").pack(side="left")
        self.max_hops_var = tk.IntVar(value=30)
        ttk.Spinbox(opts, from_=1, to=64, textvariable=self.max_hops_var, width=5).pack(side="left", padx=6)

        ttk.Label(opts, text="Timeout (ms):").pack(side="left")
        self.timeout_var = tk.IntVar(value=4000)
        ttk.Spinbox(opts, from_=500, to=10000, increment=500,
                    textvariable=self.timeout_var, width=7).pack(side="left", padx=6)

        self.resolve_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(opts, text="Resolve hostnames", variable=self.resolve_var).pack(side="left", padx=10)

    
        out_frame = ttk.Frame(self, padding=12)
        out_frame.pack(fill="both", expand=True)

        self.output = tk.Text(out_frame, wrap="none", font=("Consolas", 10))
        self.output.pack(side="left", fill="both", expand=True)

        yscroll = ttk.Scrollbar(out_frame, orient="vertical", command=self.output.yview)
        yscroll.pack(side="right", fill="y")
        self.output.configure(yscrollcommand=yscroll.set)

   
        self.status_var = tk.StringVar(value="Ready.")
        status = ttk.Label(self, textvariable=self.status_var, relief="sunken", anchor="w", padding=6)
        status.pack(fill="x", side="bottom")

    def log(self, text):
        self.output.insert("end", text + "\n")
        self.output.see("end")

    def clear_output(self):
        self.output.delete("1.0", "end")

    def save_output(self):
        data = self.output.get("1.0", "end").strip()
        if not data:
            messagebox.showinfo("Nothing to save", "Output is empty.")
            return
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt")]
        )
        if file_path:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(data)
            messagebox.showinfo("Saved", f"Output saved to:\n{file_path}")

    def start_traceroute(self):
        target = self.target_var.get().strip()
        if not target:
            messagebox.showerror("Error", "Please enter a target host/IP.")
            return

        max_hops = self.max_hops_var.get()
        timeout = self.timeout_var.get()
        resolve = self.resolve_var.get()

        self.clear_output()
        self.log(f"Starting traceroute to {target}...\n")


        cmd = ["tracert"]
        if not resolve:
            cmd.append("-d")     
        cmd += ["-h", str(max_hops), "-w", str(timeout), target]

        self.running = True
        self.start_btn.config(state="disabled")
        self.stop_btn.config(state="normal")
        self.status_var.set("Running traceroute...")

        thread = threading.Thread(target=self._run_tracert, args=(cmd,), daemon=True)
        thread.start()

    def stop_traceroute(self):
        if self.process and self.running:
            self.running = False
            try:
                self.process.terminate()
            except Exception:
                pass
            self.status_var.set("Stopped.")
            self.start_btn.config(state="normal")
            self.stop_btn.config(state="disabled")
            self.log("\nTraceroute stopped by user.")

    def _run_tracert(self, cmd):
        try:
            self.process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1
            )

            for line in self.process.stdout:
                if not self.running:
                    break
                line = line.rstrip()
                self.after(0, self.log, self._format_line(line))

            self.process.wait()

        except FileNotFoundError:
            self.after(0, messagebox.showerror, "Error", "tracert command not found.")
        except Exception as e:
            self.after(0, messagebox.showerror, "Error", str(e))
        finally:
            self.running = False
            self.after(0, self.start_btn.config, {"state": "normal"})
            self.after(0, self.stop_btn.config, {"state": "disabled"})
            self.after(0, self.status_var.set, "Done.")

    def _format_line(self, line):
  
        hop_match = re.match(r"^\s*(\d+)\s+(.*)$", line)
        if hop_match:
            hop = hop_match.group(1)
            rest = hop_match.group(2)
            return f"Hop {hop:>2}: {rest}"
        return line


if __name__ == "__main__":
    app = TracerouteGUI()
    app.mainloop()
