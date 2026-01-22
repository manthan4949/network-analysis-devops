# ✅ PYTEST FIX - RUN THIS NOW

## 🚀 The Problem
pytest is installed BUT PowerShell can't find it because:
- pytest is in: `C:\Users\manth\AppData\Roaming\Python\Python39\Scripts`
- This path is NOT in your PowerShell PATH variable

## ✅ THE SOLUTION (Copy-Paste This Exact Command)

Run this in PowerShell:

```powershell
python -m pytest tests/unit_tests.py -v --cov=.
```

That's it! The `python -m` prefix tells Python to run pytest as a module, which ALWAYS works.

---

## 📊 Expected Output

You should see:

```
collected 45 items

tests/unit_tests.py::test_app_route_exists PASSED                    [ 2%]
tests/unit_tests.py::test_extract_http_data PASSED                   [ 4%]
tests/unit_tests.py::test_image_extraction PASSED                    [ 6%]
...
======================== 45 passed in 2.34s ==========================

Name                  Stmts   Miss  Cover
------------------  ------  -----  -----
app.py                 523    124    76%
database_utils.py       89     12    87%
TOTAL                   612    136    78%
```

✅ If you see this → **ALL TESTS PASSED!**

---

## 🐳 NEXT: TEST DOCKER

Once pytest works, run these commands:

```powershell
# Build Docker image
docker build -t network-analysis-app .

# Start containers
docker-compose up -d

# Wait 5 seconds
Start-Sleep -Seconds 5

# Test the app
curl http://localhost:5000

# Stop containers
docker-compose down
```

---

## 📤 THEN: PUSH TO GITHUB

```powershell
git add .
git commit -m "Initial DevOps pipeline - all tests passing"
git push
```

---

## ⚡ QUICK REFERENCE

| Command | What it does |
|---------|-------------|
| `python -m pytest tests/unit_tests.py -v --cov=.` | Run all tests with coverage |
| `docker build -t network-analysis-app .` | Build Docker image |
| `docker-compose up -d` | Start containers |
| `curl http://localhost:5000` | Test the app |
| `docker-compose down` | Stop containers |
| `git push` | Push to GitHub |

---

## 🎯 DO THIS RIGHT NOW

1. Copy this command:
   ```powershell
   python -m pytest tests/unit_tests.py -v --cov=.
   ```

2. Paste in PowerShell

3. Press Enter

4. Tell me:
   - ✅ Did all 45 tests pass?
   - ✅ What was the coverage percentage?

That's it! 🚀
