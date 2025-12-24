## מבוא ל‑NumPy

NumPy היא ספריית ה־Python הסטנדרטית לחישובים מספריים:
- **ndarray**: מבנה נתונים מרכזי – מערך רב־ממדי מהיר.
- **וקטוריזציה**: פעולות על כל המערך בבת אחת (ללא לולאות Python איטיות).
- **אינטגרציה**: בסיס לרוב ספריות ה־Data Science (Pandas, SciPy, scikit‑learn ועוד).

התקנה:

```bash
pip install numpy
```

ייבוא בסיסי:

```python
import numpy as np
```

---

## יצירת מערכים

### ממערכי Python

```python
import numpy as np

a = np.array([1, 2, 3])           # וקטור
b = np.array([[1, 2], [3, 4]])    # מטריצה 2x2
```

- **`a.shape`** – מחזיר את הצורה (גודל המימדים).
- **`a.dtype`** – טיפוס הנתונים (int64, float64 וכו').

### פונקציות עזר ליצירה

```python
zeros = np.zeros((2, 3))       # מטריצה 2x3 מלאה באפסים
ones = np.ones((3, 3))         # מטריצה מלאה באחדים
eye = np.eye(3)                # מטריצת זהות 3x3
ar = np.arange(0, 10, 2)       # 0,2,4,6,8
lin = np.linspace(0, 1, 5)     # 5 נקודות מ-0 עד 1 כולל
```

---

## אינפורמציה על המערך

```python
x = np.array([[1, 2, 3],
              [4, 5, 6]])

print(x.ndim)   # מספר מימדים (2)
print(x.shape)  # (2, 3)
print(x.size)   # מספר איברים (6)
print(x.dtype)  # סוג (למשל int64)
```

---

## אינדוקס וחתכים (Indexing & Slicing)

### אינדוקס רגיל

```python
x = np.array([[10, 11, 12],
              [20, 21, 22],
              [30, 31, 32]])

print(x[0, 0])   # 10
print(x[1, 2])   # 22
print(x[2])      # השורה השלישית
```

### חתכים

```python
print(x[:, 0])     # העמודה הראשונה
print(x[0:2, 1:3]) # 2 שורות ראשונות, 2 עמודות אחרונות
print(x[::2, :])   # כל שורה שנייה
```

---

## פעולות מתמטיות ווקטוריזציה

פעולות מתבצעות על כל המערך בבת אחת:

```python
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

print(a + b)     # [11 22 33]
print(a * b)     # [10 40 90]
print(a ** 2)    # חזקה: [1 4 9]
print(np.sqrt(b))# שורש ריבועי
```

על מטריצות:

```python
m = np.array([[1, 2],
              [3, 4]])

print(m + 1)          # מוסיף 1 לכל איבר
print(m * 2)          # כפל סקאלרי
print(m @ m)          # כפל מטריצות
print(np.dot(m, m))   # אותו דבר כמו @
```

---

## סטטיסטיקה בסיסית

```python
x = np.array([1, 2, 3, 4, 5])

print(x.mean())    # ממוצע
print(x.sum())     # סכום
print(x.min())     # מינימום
print(x.max())     # מקסימום
print(x.std())     # סטיית תקן
```

על ציר (axis) במטריצה:

```python
m = np.array([[1, 2, 3],
              [4, 5, 6]])

print(m.sum(axis=0))  # סכום לפי עמודות: [5 7 9]
print(m.sum(axis=1))  # סכום לפי שורות: [ 6 15]
```

---

## שינוי צורה (Reshape) ו־Flatten

```python
a = np.arange(12)         # [0..11]

b = a.reshape(3, 4)       # מטריצה 3x4
print(b.shape)            # (3, 4)

flat = b.ravel()          # מחזיר וקטור ממוטח (view ברוב המקרים)
flat2 = b.flatten()       # מחזיר עותק
```

ניתן להשתמש ב־`-1` כדי שהמימד יחושב אוטומטית:

```python
c = a.reshape(2, -1)      # 2 שורות, השאר יחושב לבד -> (2, 6)
```

---

## Broadcasting – שידור אוטומטי של מימדים

Broadcasting מאפשר לבצע פעולות על מערכים בגדלים שונים בצורה חכמה.

```python
m = np.array([[1, 2, 3],
              [4, 5, 6]])

v = np.array([10, 20, 30])

print(m + v)
```

NumPy “משדר” את `v` לשתי שורות, כך שהחיבור מתבצע על כל שורה.

---

## NumPy Random

```python
rng = np.random.default_rng(seed=42)

print(rng.integers(low=0, high=10, size=5))     # חמישה מספרים אקראיים [0,10)
print(rng.random((2, 3)))                       # מטריצה 2x3 בין 0 ל-1
print(rng.normal(loc=0, scale=1, size=(2, 2)))  # התפלגות נורמלית
```

---

## דוגמה מלאה: ממוצע ציונים לכיתה

```python
import numpy as np

# תלמידים x מקצועות
grades = np.array([
    [80, 90, 75],
    [92, 88, 84],
    [70, 100, 95],
])

student_avg = grades.mean(axis=1)  # ממוצע לכל תלמיד
subject_avg = grades.mean(axis=0)  # ממוצע לכל מקצוע

print("ממוצע לתלמיד:", student_avg)
print("ממוצע למקצוע:", subject_avg)
```

---

## המשך לימוד – מה כדאי לחקור הלאה

- **חיתוכים מתקדמים**: boolean indexing (בחירת איברים לפי תנאי).
- **עבודה עם NaN**: שימוש ב־`np.nan`, פונקציות `np.nanmean` וכו'.
- **אינטגרציה עם Pandas**: המרת `ndarray` ל־`DataFrame` ולהפך.
- **ביצועים**: השוואה בין לולאות Python לפעולות וקטוריות.

כדי להעמיק, אתה יכול לשלב את NumPy בתרגילים שלך (למשל במקום רשימות רגילות בחישובים מתמטיים, סטטיסטיקה על נתוני JSONPlaceholder וכדומה).


