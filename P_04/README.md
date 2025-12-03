# Python Practice Programs - String Manipulation

## 1️⃣ Interleaved Merge with Reversed Half
📄 **File:** `Merge_1.py`  
🧠 **Description:**  
Takes two strings and forms a new string by alternately picking:
* Characters from the start of string 1
* Characters from the end of string 2

Leftover characters are appended.

💻 **Example Run:**
```
Enter string: abcde
Enter string: 123
a3b2c1de
```

---

## 2️⃣ Digit Extractor & Statistics
📄 **File:** `DigitExtractor_2.py`  
🧠 **Description:**  
Extracts digits from a mixed string and calculates:  
✔ Sum  
✔ Average  
✔ Maximum  
✔ Minimum  

If no digits → prints a message.

💻 **Example Run:**
```
Enter string: ab3c09k5
Sum:  17
Average:  4.25
Maximum:  9
Minimum:  0
```

---

## 3️⃣ Balanced-String Test
📄 **File:** `BalanceString_3.py`  
🧠 **Description:**  
Checks whether all characters of string A exist somewhere in string B.

💻 **Example Run:**
```
Enter string a: cat
Enter string b: attack
True
```

---

## 4️⃣ Longest Increasing Digit-Sum Substring
📄 **File:** `IncreasingDigitSum_4.py`  
🧠 **Description:**  
Given numbers separated by spaces:
* Converts each into digit-sum
* Finds the longest contiguous subsequence where each digit-sum is strictly increasing

💻 **Example Run:**
```
Enter space separated numbers: 12 3 45 9 10 2 100
Longest sequence: ['3', '45']
Length: 2
```

---

## 5️⃣ Anagram Group Detection
📄 **File:** `Anagram_5.py`  
🧠 **Description:**  
Groups words that are anagrams of each other.

💻 **Example Run:**
```
Enter words separated by space: eat tea tan ate nat bat
[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
```