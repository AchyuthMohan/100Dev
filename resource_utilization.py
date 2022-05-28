import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import psutil
import collections
from main import decorator


def cpu_usage(ax0):
    ax0.set_title('CPU usage')
    ax0.plot(cpu, "#f03e3e")
    ax0.scatter(len(cpu)-1, cpu[-1], color="#f03e3e")
    ax0.text(len(cpu)-1, cpu[-1]+2, "{}%".format(cpu[-1]))
    ax0.set_ylim(0, 110)


def memory_usage(ax1):
    ax1.set_title('Memory usage')
    ax1.plot(ram, "#0ca678")
    ax1.scatter(len(ram)-1, ram[-1], color='#0ca678')
    ax1.text(len(ram)-1, ram[-1]+2, "{}% ".format(ram[-1]))
    ax1.set_ylim(0, 100)


def network_usage(ax2):
    ax2.set_title('Bytes send/received')
    ax2.plot(network)
    ax2.scatter(len(network)-1, network[-1])
    ax2.text(len(network)-3, network[-1], "{}".format(network[-1]))
    ax2.set_ylim(0, 0.15)


def disk_usage(ax3):
    ax3.set_title('Disk usage')
    ax3.plot(disk, "#fd7e14")
    ax3.scatter(len(disk)-1, disk[-1], color="#fd7e14")
    ax3.text(len(disk)-3, disk[-1], "{}%".format(disk[-1]))
    ax3.set_ylim(0, 100)


def resource_utils(i):
    cpu.popleft()
    cpu.append(psutil.cpu_percent())

    ram.popleft()
    ram.append(psutil.virtual_memory().percent)

    disk.popleft()
    ds = psutil.disk_usage('/')
    disk.append((ds.used/ds.total)*100)

    network.popleft()
    nw = psutil.net_io_counters()
    bytes_send = nw.bytes_sent
    bytes_received = nw.bytes_recv
    network.append(bytes_send/bytes_received)

    ax0.cla()
    ax1.cla()
    ax2.cla()
    ax3.cla()

    cpu_usage(ax0)
    memory_usage(ax1)
    network_usage(ax2)
    disk_usage(ax3)


@decorator
def resource_util():

    ax0.set_facecolor('#fff5f5')
    ax1.set_facecolor('#f4fce3')
    ax2.set_facecolor('#e7f5ff')
    ax3.set_facecolor('#fff3bf')

    ani = FuncAnimation(fig, resource_utils, interval=1000)
    fig.suptitle('Resource utilization')
    plt.show()


cpu = collections.deque(np.zeros(10))
ram = collections.deque(np.zeros(10))
network = collections.deque(np.zeros(10))
disk = collections.deque(np.zeros(10))
fig, ((ax0, ax1), (ax2, ax3)) = plt.subplots(2, 2)

resource_util()
