"""Python環境テストスクリプト"""
import sys
import platform

print("=" * 50)
print("🐍 Python 基本チェック")
print("=" * 50)
print(f"Python バージョン : {sys.version}")
print(f"プラットフォーム   : {platform.system()} {platform.release()}")
print(f"実行パス          : {sys.executable}")
print()

# --- パッケージインポートテスト ---
print("=" * 50)
print("📦 パッケージ インポートチェック")
print("=" * 50)

packages = ["numpy", "pandas", "requests"]
results = {}

for pkg in packages:
    try:
        mod = __import__(pkg)
        ver = getattr(mod, "__version__", "不明")
        results[pkg] = ("✅", ver)
        print(f"  ✅ {pkg:12s} v{ver}")
    except ImportError:
        results[pkg] = ("❌", None)
        print(f"  ❌ {pkg:12s} — 未インストール")

print()

# --- 簡単な動作テスト ---
print("=" * 50)
print("🔧 簡単な動作テスト")
print("=" * 50)

if results["numpy"][0] == "✅":
    import numpy as np
    arr = np.arange(5)
    print(f"  numpy  : np.arange(5) = {arr}")

if results["pandas"][0] == "✅":
    import pandas as pd
    df = pd.DataFrame({"A": [1, 2, 3], "B": ["x", "y", "z"]})
    print(f"  pandas : DataFrame shape = {df.shape}")

if results["requests"][0] == "✅":
    import requests
    print(f"  requests: モジュール読み込み OK")

print()

# --- 結果サマリ ---
ok = sum(1 for v in results.values() if v[0] == "✅")
total = len(results)
print("=" * 50)
if ok == total:
    print(f"🎉 すべてのチェックに合格しました ({ok}/{total})")
else:
    print(f"⚠️  {total - ok} 件のパッケージが見つかりません ({ok}/{total})")
print("=" * 50)
