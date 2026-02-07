# Ticketing System — Documentation

## 1. Flowchart / Diagram (Minimal & Clear)

┌────────────────────┐
│ Start Program │
└─────────┬──────────┘
│
▼
┌────────────────────┐
│ Generate Tickets │
│ (n times, FIFO) │
└─────────┬──────────┘
│
▼
┌────────────────────┐
│ Add to Queue       │
│ (deque append)     │
└─────────┬──────────┘
│
▼
┌────────────────────┐
│ Process Tickets    │
│ (popleft FIFO)     │
└─────────┬──────────┘
│
▼
┌────────────────────┐
│ Queue Empty?       │
└───────┬────────────┘
│Yes
▼
┌────────────────────┐
│ End                │
└────────────────────┘

---

## 2. Clarifying Questions

1. Should ticket numbers reset each day, or continue increasing indefinitely?
2. Do we need to store served tickets for reporting, or can they be discarded?
3. Should the system support concurrent ticket generation and processing, or is a simple sequential simulation acceptable?
4. Is the timestamp required to be in a specific format?
5. Should the queue ever allow priority tickets, or is it strictly FIFO?
6. Should the program run continuously, or only simulate a single batch of customers?

---

## 3. Unit Test Cases (Normal + Edge Cases)

### Normal Test Cases

| Test     | Description                     | Expected Result        |
| -------- | ------------------------------- | ---------------------- |
| Normal 1 | Generate 1 ticket               | Queue length becomes 1 |
| Normal 2 | Generate 3 tickets              | Queue length becomes 3 |
| Normal 3 | Generate 2 tickets then process | Queue becomes empty    |

### Edge Test Cases

| Test   | Description                    | Expected Result             |
| ------ | ------------------------------ | --------------------------- |
| Edge 1 | Generate 0 tickets             | Queue remains empty         |
| Edge 2 | Process with empty queue       | No crash, queue stays empty |
| Edge 3 | Generate 1 ticket then process | Queue becomes empty         |

---

## 4. Time & Space Complexity

### Ticket Generation

- Generates `n` tickets in a loop
- Each append to a deque is `O(1)`

**Time Complexity:**  
`O(n)`

**Space Complexity:**  
`O(n)`  
(because the queue stores `n` Ticket objects)

---

### Ticket Processing

- Processes each ticket once
- Each `popleft()` from a deque is `O(1)`

**Time Complexity:**  
`O(n)`

**Space Complexity:**  
`O(1)`  
(after processing, the queue is empty)

---

### Overall Complexity

**Time:**  
`O(n)`

**Space:**  
`O(n)`

This is the optimal complexity for any FIFO queue simulation.
