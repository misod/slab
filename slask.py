import psutil

cpu = psutil.cpu_percent(interval=1, percpu=True)

print cpu
