# Virtual Machines and Memory Virtualization Terminology

## Virtual Machines (VMs)

1. **Virtual Machine (VM)** – A software emulation of a physical computer system, allowing multiple operating systems to run on the same hardware.
2. **Virtual Machine Monitor (VMM) / Hypervisor** – A software layer that manages virtual machines by mapping virtual resources to physical resources.
3. **Host OS vs. Guest OS** – The **host OS** is the primary operating system running on the physical machine, while the **guest OS** runs within a virtual machine.
4. **Full Virtualization** – A method where the VMM completely emulates hardware so that an unmodified guest OS can run.
5. **Paravirtualization** – A virtualization method where the guest OS is modified to work efficiently with the hypervisor.
6. **Hardware-Assisted Virtualization** – CPU features that provide direct support for virtualization, reducing the need for software-based emulation (e.g., **Intel VT-x, AMD-V**).
7. **Trap-and-Emulate** – A method where the VMM intercepts privileged instructions executed by the guest OS and safely emulates them.
8. **Type 1 Hypervisor (Bare Metal)** – Runs directly on the hardware without a host OS (e.g., **VMware ESXi, Microsoft Hyper-V, Xen**).
9. **Type 2 Hypervisor (Hosted)** – Runs on a conventional operating system and manages VMs as applications (e.g., **VMware Workstation, VirtualBox**).
10. **VM Isolation** – The principle that each VM is independent and cannot directly interfere with others, improving security and reliability.
11. **Resource Sharing** – Multiple VMs share hardware resources such as CPU, memory, and storage, improving utilization.
12. **VM Snapshots** – A saved state of a virtual machine that can be restored later.
13. **Live Migration** – The process of moving a running VM from one physical host to another without downtime.

## Memory Virtualization

14. **Virtual Memory** – A system where the OS uses disk storage to extend RAM, allowing processes to use more memory than is physically available.
15. **Paging** – A memory management scheme that divides virtual memory into fixed-size units called **pages**.
16. **Page Table** – A data structure used by the OS to map **virtual addresses** to **physical addresses**.
17. **Memory Management Unit (MMU)** – A hardware component that translates virtual addresses into physical addresses.
18. **Page Fault** – Occurs when a requested page is not in physical memory, requiring the OS to fetch it from disk.
19. **Translation Lookaside Buffer (TLB)** – A cache that stores recent virtual-to-physical address mappings to speed up address translation.
20. **TLB Miss** – Occurs when the requested page mapping is not found in the TLB, requiring a lookup in the page table.
21. **Page Table Entry (PTE)** – An entry in the page table that includes:
   - **Physical Page Number** – The actual location in RAM.
   - **Dirty Bit** – Indicates if the page has been modified.
   - **Reference Bit** – Shows if the page was accessed recently.
22. **Page Replacement Algorithms** – Determine which page to remove when memory is full:
   - **Least Recently Used (LRU)** – Removes the least recently accessed page.
   - **First-In-First-Out (FIFO)** – Removes the oldest page.
   - **Random Replacement** – Removes a randomly chosen page.
23. **Swapping** – Moving entire processes between RAM and disk to free memory.
24. **Memory Overcommitment** – The practice of allocating more virtual memory to VMs than physically available, relying on paging and compression.

## Timer Virtualization

25. **Timer Virtualization** – The VMM handles timer interrupts for guest VMs to ensure accurate timekeeping.
26. **Time Drift** – A problem where guest OS clocks become inaccurate due to differences in how virtual time is handled.
27. **Virtual Timer Interrupts** – The VMM suspends a VM when an interrupt occurs and manages how time progresses inside the guest OS.

## Instruction Set Virtualization

28. **Privileged Instructions** – CPU instructions that can only be executed in system mode (e.g., modifying page tables).
29. **System Mode (Kernel Mode)** – A CPU mode that allows unrestricted access to hardware resources.
30. **User Mode** – A restricted CPU mode where applications run without direct hardware access.
31. **Trap Handling** – When a user-mode process executes a privileged instruction, the CPU generates a **trap**, switching execution to system mode.
32. **Renaissance of Virtualization Support** – Modern processors include virtualization-friendly instruction sets to improve performance (e.g., **Intel VT-x, AMD-V**).

## Cache Coherence & Multiprocessor Virtualization

33. **Cache Coherence** – Ensures all CPU caches maintain a consistent view of memory.
34. **Snooping Protocol** – A cache coherence mechanism where caches monitor the bus for changes.
35. **Invalidating Snooping Protocol** – When one processor modifies a cache line, other copies in different caches are invalidated.
36. **Directory-Based Coherence** – A scalable approach where a directory keeps track of which caches store each memory block.
37. **Write-Through Cache** – Writes data to both cache and main memory simultaneously.
38. **Write-Back Cache** – Writes data to memory only when the cache line is replaced.
39. **Cache Migration** – Moves data closer to the processor that uses it most frequently.
40. **Memory Consistency** – Rules that define when updates to shared memory become visible to other processors.

## Conclusion
These concepts form the foundation of **virtualization technology** and **memory management** in modern computing. Virtualization enables efficient resource utilization, while memory virtualization optimizes performance and isolation. Understanding how VMs interact with memory, CPU instructions, and caches is crucial for working with cloud computing, data centers, and modern operating systems.

