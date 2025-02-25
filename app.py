import streamlit as st

# Title of the app
st.title("Memory Hierarchy and Virtualization Quiz")
st.write("Memory Hierarchy Mastery: Test Your Knowledge of Virtual Machines, Memory Systems, and Cache Coherence")

# Initialize session state variables if they don’t exist
if "score" not in st.session_state:
    st.session_state.score = 0https://github.com/MMIX2009/virtual-machines-and-memory/tree/main

if "question_index" not in st.session_state:
    st.session_state.question_index = 0

if "answer_submitted" not in st.session_state:
    st.session_state.answer_submitted = False

# Questions and answers
quiz = [
     # Virtual Machines
    {"question": "What is a virtual machine?",
     "options": ["A physical machine that runs a single OS", "A software emulation of a computer system", "A cache optimization technique", "A high-speed memory unit"],
     "answer": "A software emulation of a computer system"},

    {"question": "Which of the following is NOT an advantage of virtual machines?",
     "options": ["Improved isolation", "Security and reliability", "No performance impact", "Resource sharing"],
     "answer": "No performance impact"},

    {"question": "What does a Virtual Machine Monitor (VMM) do?",
     "options": ["Manages virtual memory paging", "Maps virtual resources to physical resources", "Handles physical hardware failures", "Optimizes CPU scheduling"],
     "answer": "Maps virtual resources to physical resources"},

    {"question": "Which of the following companies developed VM/370 in the 1970s?",
     "options": ["IBM", "Microsoft", "Intel", "VMWare"],
     "answer": "IBM"},

    {"question": "Which of the following is an example of a modern virtual machine software?",
     "options": ["VMWare", "MS Paint", "Adobe Photoshop", "Intel VT"],
     "answer": "VMWare"},
     
    {"question": "What happens when a guest OS executes privileged instructions in a virtual machine?",
     "options": ["The instruction is directly executed by the hardware", "The VMM intercepts the instruction and emulates it", "The host OS crashes", "The instruction is ignored"],
     "answer": "The VMM intercepts the instruction and emulates it"},
     
    {"question": "What is the main benefit of running multiple virtual machines on a single physical host?",
     "options": ["Faster computation", "Increased security through isolation", "Reduced power consumption", "Simplified programming"],
     "answer": "Increased security through isolation"},
     
    {"question": "In modern virtualization, what is 'hardware-assisted virtualization'?",
     "options": ["Running VMs on specialized hardware", "CPU features that support virtualization", "Using hardware accelerators for VM graphics", "Specialized network cards for VMs"],
     "answer": "CPU features that support virtualization"},

    # Timer Virtualization
    {"question": "What happens during timer virtualization?",
     "options": ["A virtual timer replaces the system clock", "VMM handles timer interrupts for guest VMs", "Each process gets direct access to the CPU timer", "Interrupts are disabled for virtualized systems"],
     "answer": "VMM handles timer interrupts for guest VMs"},

    {"question": "Why do virtual machines need timer virtualization?",
     "options": ["To prevent time drift in guest OS", "To improve CPU performance", "To reduce memory usage", "To eliminate page faults"],
     "answer": "To prevent time drift in guest OS"},
     
    {"question": "In timer virtualization, when a timer interrupt occurs, what happens first?",
     "options": ["The guest OS handles it directly", "The VMM suspends the current VM", "The hardware clock is paused", "The interrupt is ignored"],
     "answer": "The VMM suspends the current VM"},

    # Instruction Set Support
    {"question": "Why are privileged instructions restricted to system mode?",
     "options": ["To improve CPU speed", "To prevent unauthorized access to critical resources", "To allow users to manage hardware directly", "To optimize memory access"],
     "answer": "To prevent unauthorized access to critical resources"},

    {"question": "What happens when a user-mode process attempts to execute a privileged instruction?",
     "options": ["The instruction executes normally", "The system reboots", "A trap to system mode occurs", "The CPU ignores the instruction"],
     "answer": "A trap to system mode occurs"},
     
    {"question": "Which processor mode allows access to all hardware resources?",
     "options": ["User mode", "Guest mode", "System mode", "Virtual mode"],
     "answer": "System mode"},
     
    {"question": "What is meant by the 'renaissance of virtualization support' in modern processor architectures?",
     "options": ["Adding more cores for virtualization", "Adapting instruction sets to better support VMs", "Creating specialized VM processors", "Removing legacy instructions"],
     "answer": "Adapting instruction sets to better support VMs"},

    # Virtual Memory
    {"question": "What is virtual memory?",
     "options": ["A type of secondary storage", "A method for extending RAM using disk storage", "A fast form of SRAM", "A process for optimizing CPU scheduling"],
     "answer": "A method for extending RAM using disk storage"},

    {"question": "What is a virtual memory 'page'?",
     "options": ["A unit of virtual memory storage", "A CPU register", "A cache block", "A special RAM segment"],
     "answer": "A unit of virtual memory storage"},

    {"question": "What causes a page fault?",
     "options": ["Corrupt memory data", "A requested page not being in physical memory", "CPU overheating", "Cache miss"],
     "answer": "A requested page not being in physical memory"},

    {"question": "Which component translates virtual addresses to physical addresses?",
     "options": ["Cache controller", "ALU", "Memory Management Unit (MMU)", "I/O bus"],
     "answer": "Memory Management Unit (MMU)"},

    {"question": "What is the purpose of page tables?",
     "options": ["To map virtual addresses to physical addresses", "To store all OS instructions", "To optimize CPU clock cycles", "To track cache misses"],
     "answer": "To map virtual addresses to physical addresses"},
     
    {"question": "What happens when a page fault occurs in a virtual memory system?",
     "options": ["The system crashes", "The OS fetches the page from disk", "The program is terminated", "The CPU switches to another process permanently"],
     "answer": "The OS fetches the page from disk"},
     
    {"question": "What is a typical page size in modern computer systems?",
     "options": ["64 bytes", "512 bytes", "4 KB", "1 MB"],
     "answer": "4 KB"},
     
    {"question": "What information is stored in a Page Table Entry (PTE)?",
     "options": ["Only the physical page number", "Only access permissions", "Physical page number and status bits", "Program instructions"],
     "answer": "Physical page number and status bits"},
     
    {"question": "What is the 'dirty bit' in a page table entry used for?",
     "options": ["Indicating corrupted pages", "Marking pages that have been modified", "Showing pages with errors", "Flagging pages that should be deleted"],
     "answer": "Marking pages that have been modified"},
     
    {"question": "What does the 'reference bit' in a page table entry indicate?",
     "options": ["The page contains references to other pages", "The page has been accessed recently", "The page is a reference manual", "The page contains pointers"],
     "answer": "The page has been accessed recently"},

    # TLB and Translation
    {"question": "What is a Translation Look-aside Buffer (TLB)?",
     "options": ["A special hard drive for virtual memory", "A cache for recently used page table entries", "A buffer for network translations", "A hardware component that replaces page tables"],
     "answer": "A cache for recently used page table entries"},
     
    {"question": "What happens on a TLB miss?",
     "options": ["The CPU crashes", "The operating system is restarted", "The page table in memory is accessed", "The program is terminated"],
     "answer": "The page table in memory is accessed"},
     
    {"question": "Why is a TLB important for virtual memory performance?",
     "options": ["It eliminates the need for virtual memory", "It reduces the time needed for address translation", "It increases the page size", "It allows more programs to run simultaneously"],
     "answer": "It reduces the time needed for address translation"},
     
    {"question": "Who typically handles TLB misses in modern systems?",
     "options": ["The user", "Hardware or software, depending on the architecture", "Only the hardware", "Only the operating system"],
     "answer": "Hardware or software, depending on the architecture"},

    # Cache Coherence
    {"question": "What is the cache coherence problem?",
     "options": ["Different CPU caches holding different values for the same memory location", "Too much data stored in cache", "High memory latency", "Slow disk writes"],
     "answer": "Different CPU caches holding different values for the same memory location"},

    {"question": "Which protocol ensures cache coherence by broadcasting updates?",
     "options": ["Write-back", "Snooping", "Direct-mapped", "Paging"],
     "answer": "Snooping"},

    {"question": "What is an invalidating snooping protocol?",
     "options": ["A protocol that prevents cache corruption by invalidating other copies of a modified block", "A process that deletes all cache entries", "A method for increasing memory speed", "A replacement algorithm for RAM"],
     "answer": "A protocol that prevents cache corruption by invalidating other copies of a modified block"},

    {"question": "Which of the following is a goal of cache coherence?",
     "options": ["Ensure all CPUs have a consistent view of memory", "Increase cache misses", "Reduce virtual memory usage", "Eliminate secondary storage"],
     "answer": "Ensure all CPUs have a consistent view of memory"},

    {"question": "Which replacement policy is often used to minimize page faults?",
     "options": ["Least Recently Used (LRU)", "First-In-First-Out (FIFO)", "Random Replacement", "Round Robin"],
     "answer": "Least Recently Used (LRU)"},
     
    {"question": "What happens when a processor writes to a memory location in an invalidating snooping protocol?",
     "options": ["Other caches are unaffected", "Other caches with that location get updated with the new value", "Other caches with that location invalidate their copy", "The memory location is locked"],
     "answer": "Other caches with that location invalidate their copy"},
     
    {"question": "What is the benefit of a directory-based cache coherence protocol compared to snooping?",
     "options": ["It's simpler to implement", "It scales better with more processors", "It requires less memory", "It's always faster"],
     "answer": "It scales better with more processors"},
     
    {"question": "In a write-through cache, when a processor writes data, what happens?",
     "options": ["Data is written only to the cache", "Data is written to both cache and memory", "Data is written only to memory", "Data is temporarily stored in a buffer"],
     "answer": "Data is written to both cache and memory"},
     
    {"question": "In a write-back cache, when is data written to main memory?",
     "options": ["Immediately after being modified", "Only when the cache line is replaced", "After every 10 modifications", "Data is never written back"],
     "answer": "Only when the cache line is replaced"},
     
    {"question": "What is 'cache migration' in multiprocessor systems?",
     "options": ["Moving the entire cache to another location", "The movement of data to a processor's local cache", "Transitioning from one cache type to another", "Expanding cache size dynamically"],
     "answer": "The movement of data to a processor's local cache"},
     
    {"question": "What is meant by 'memory consistency' in multiprocessor systems?",
     "options": ["All memory modules have the same access speed", "Memory always matches cache contents", "The rules for when memory updates become visible to processors", "Memory that never becomes corrupted"],
     "answer": "The rules for when memory updates become visible to processors"},
     
    {"question": "How does a virtual machine share physical hardware resources like CPUs?",
     "options": ["Each VM gets exclusive access to specific CPU cores", "The VMM schedules VM execution on available physical CPUs", "VMs always get direct access to all CPUs", "VMs create their own virtual CPUs from scratch"],
     "answer": "The VMM schedules VM execution on available physical CPUs"}
]

# Display the current question
current_question = quiz[st.session_state.question_index]
st.write(f"**Question {st.session_state.question_index + 1}: {current_question['question']}**")

# Multiple-choice options
selected_option = st.radio("Select your answer:", current_question["options"], key=f"question_{st.session_state.question_index}")

# Submit button to evaluate the selected answer
if st.button("Submit Answer") and not st.session_state.answer_submitted:
    if selected_option == current_question["answer"]:
        st.success("Correct!")
        st.session_state.score += 1
    else:
        st.error(f"Incorrect. The correct answer is: {current_question['answer']}")
    st.session_state.answer_submitted = True

# Next button (enabled only after an answer is submitted)
if st.session_state.answer_submitted:
    if st.button("Next Question"):
        if st.session_state.question_index < len(quiz) - 1:
            st.session_state.question_index += 1
            st.session_state.answer_submitted = False
            # Force rerun to display the next question immediately
            st.rerun()
        else:
            st.write("### Quiz Completed!")
            st.write(f"Your final score is {st.session_state.score}/{len(quiz)}")
            st.session_state.question_index = 0
            st.session_state.score = 0
            st.session_state.answer_submitted = False

st.write(f"**Current Score:** {st.session_state.score}")
