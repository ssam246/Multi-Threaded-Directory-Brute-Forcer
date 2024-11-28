import requests
import sys
import os
import time
from threading import Thread, Lock
from queue import Queue
from tqdm import tqdm

lock = Lock()  # For thread-safe operations

def usage():
    """Display usage instructions."""
    print("---------- USAGE INSTRUCTION ----------")
    print(f"Usage: python {sys.argv[0]} URL WORDLIST [NUMBER_OF_THREADS (default: 10)]")
    sys.exit(1)

def load_wordlist(wordlist_path):
    """Load the wordlist from the given file."""
    if not os.path.isfile(wordlist_path):
        print(f"The file {wordlist_path} doesn't exist.")
        sys.exit(1)
    with open(wordlist_path, 'r') as file:
        return [line.strip() for line in file]

def prepare_chunks(wordlist, num_chunks):
    """Split the wordlist into chunks for threading."""
    for i in range(0, len(wordlist), num_chunks):
        yield wordlist[i:i + num_chunks]

def worker(queue, url, match_codes, results, progress_bar):
    """Thread worker function to process directories."""
    session = requests.Session()
    while not queue.empty():
        word = queue.get()
        try:
            if word.startswith("/"):
                word = word[1:]
            target_url = f"{url}/{word}"
            response = session.get(target_url, timeout=5)

            if str(response.status_code) in match_codes:
                with lock:
                    results.append(f"/{word:<40}  [ Status: {response.status_code}  Length: {len(response.content)} ]")
            progress_bar.update(1)

        except requests.RequestException as e:
            with lock:
                print(f"Error for {word}: {e}")
        finally:
            queue.task_done()

def brute_force(url, wordlist, num_threads, match_codes):
    """Main brute-forcing logic."""
    queue = Queue()
    results = []
    for word in wordlist:
        queue.put(word)

    progress_bar = tqdm(total=len(wordlist), desc="Brute-forcing", unit="request")

    threads = []
    for _ in range(num_threads):
        thread = Thread(target=worker, args=(queue, url, match_codes, results, progress_bar), daemon=True)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    progress_bar.close()
    return results

def main():
    try:
        # Parse arguments
        if len(sys.argv) < 3:
            usage()

        url = sys.argv[1].rstrip("/")
        wordlist_path = sys.argv[2]
        num_threads = int(sys.argv[3]) if len(sys.argv) > 3 else 10

        # Load wordlist
        wordlist = load_wordlist(wordlist_path)
        total_len = len(wordlist)

        # Validate threads
        if num_threads <= 0 or num_threads > total_len:
            print("\nInvalid number of threads. Ensure it's >0 and <= the wordlist size.\n")
            sys.exit(1)

        # Display configuration
        match_codes = ['200', '301', '302', '401', '403', '429']  # Modify this for desired status codes
        print(f"""
        ======================================
        URL           --> {url}
        Wordlist      --> {wordlist_path}
        Threads       --> {num_threads}
        Status Codes  --> {', '.join(match_codes)}
        ======================================
        \n""")

        # Brute-forcing
        print("------- Starting Directory Brute-forcing -------\n")
        start_time = time.perf_counter()
        results = brute_force(url, wordlist, num_threads, match_codes)
        end_time = time.perf_counter()

        # Display results
        if results:
            print("\nFound Directories:")
            print("\n".join(results))
        else:
            print("\nNo valid directories found.")

        print(f"\nChecked {total_len} directories in {round(end_time - start_time, 2)} seconds.\n")

    except KeyboardInterrupt:
        print("\nProcess interrupted by user. Exiting...")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
