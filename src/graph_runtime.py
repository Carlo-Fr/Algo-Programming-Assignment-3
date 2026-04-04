import time
import subprocess
import sys
import os
import matplotlib.pyplot as plt

tests_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tests')
hvlcs = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'hvlcs.py')

lengths = []
times = []

for i in range(1, 11):
    path = os.path.join(tests_dir, f'test_{i:02d}.in')
    lines = open(path).read().splitlines()
    k = int(lines[0])
    avg_len = (len(lines[k + 1]) + len(lines[k + 2])) // 2

    start = time.perf_counter()
    with open(path) as f:
        subprocess.run([sys.executable, hvlcs], stdin=f, stdout=subprocess.DEVNULL)
    elapsed = time.perf_counter() - start

    lengths.append(avg_len)
    times.append(elapsed)
    print(f"test_{i:02d} | len={avg_len} | time={elapsed:.4f}s")

plt.plot(lengths, times, marker='o')
plt.title('HVLCS Runtime')
plt.xlabel('Average String Length')
plt.ylabel('Time (seconds)')
plt.grid(True)
plt.savefig(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'runtime_graph.png'))
plt.show()
