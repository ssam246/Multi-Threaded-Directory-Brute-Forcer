# **Directory Brute Forcer**

A fast and robust multithreaded directory brute-forcing tool designed for security testing. It uses wordlists to discover valid directories on a given URL and displays essential information such as status codes and response lengths.

---

## **Features**

- **Multithreading**: Fast brute-forcing with configurable thread count.
- **Progress Bar**: Real-time feedback on the brute-forcing process using `tqdm`.
- **Customizable Status Codes**: Match specific HTTP status codes to filter results.
- **Error Handling**: Gracefully handles timeouts, connection errors, and invalid inputs.
- **Session Reuse**: Optimized performance with `requests.Session` for reusing TCP connections.
- **Wordlist Support**: Accepts any text file as a wordlist.

---

## **Prerequisites**

- Python 3.10.10 installed on your system.
- Required libraries: Install dependencies using `pip`:
  ```bash
  pip install requests tqdm
  ```

- **Permissions**:
  - Ensure you have the necessary permissions to run the script and access the target URL.

---

## **Installation**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ssam246/Multi-Threaded-Directory-Brute-Forcer
   cd directory-bruteforcer
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## **Usage**

### **Basic Usage**:
Run the tool with a URL and wordlist:
```bash
python directory_bruteforcer.py https://example.com wordlist.txt
```

### **Specify Threads**:
You can specify the number of threads for faster brute-forcing:
```bash
python directory_bruteforcer.py https://example.com wordlist.txt 20
```

### **Command-Line Options**:
| Option          | Description                                                   |
|------------------|---------------------------------------------------------------|
| `URL`           | The base URL to brute force directories.                      |
| `WORDLIST`      | Path to the wordlist file to use.                              |
| `NUMBER_OF_THREADS` | (Optional) Number of threads to use (default: 10).         |

---

## **Output Example**

### Progress Bar:
```
Brute-forcing: 100%|█████████████████████████| 10000/10000 [00:15<00:00, 670.29 request/s]
```

### Found Results:
```
/admin                              [ Status: 403  Length: 123 ]
/login                              [ Status: 200  Length: 4567 ]
/dashboard                          [ Status: 200  Length: 8735 ]
```

If no directories are found:
```
No valid directories found.
```

---

## **Error Handling**

- **File Not Found**:
  - Ensure the provided wordlist file exists.
- **Connection Issues**:
  - Check your network and ensure the target URL is reachable.
- **Invalid Thread Count**:
  - Use a thread count that is greater than 0 and less than or equal to the wordlist size.

---

## **Contributing**

Contributions are welcome! To contribute:
1. Fork the repository.
2. Implement your changes or fix issues.
3. Submit a pull request with a detailed description of your improvements.

---

## **License**

This project is licensed under the **MIT License**.

---

## **Disclaimer**

This tool is intended for **educational and ethical purposes only**.  
The author does not condone the use of this tool for illegal or malicious activities.  
Always ensure you have proper authorization before testing any target.

---

### **Made with 💻 and 🛡️ by Stephen**

