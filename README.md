# AI Data Cleaner

أداة سطر أوامر بلغة Python لفحص وتنظيف ملفات CSV قبل استخدامها في مشاريع الذكاء الاصطناعي.

## المزايا

- قراءة أي ملف CSV من سطر الأوامر.
- عرض عدد الصفوف والأعمدة.
- كشف القيم الناقصة والصفوف المكررة.
- إزالة الصفوف المكررة.
- ملء القيم الرقمية الناقصة بالوسيط.
- ملء القيم النصية الناقصة بكلمة `Unknown`.
- حفظ ملف بيانات نظيف.
- إنشاء تقرير بعمليات التنظيف.
- اختبارات تلقائية باستخدام `pytest`.

## بنية المشروع

```text
ai-data-cleaner/
├── data/
│   ├── raw/        # البيانات الأصلية
│   └── processed/  # البيانات بعد التنظيف
├── reports/        # تقارير التنظيف
├── src/            # كود البرنامج
├── tests/          # الاختبارات التلقائية
├── requirements.txt
└── README.md
```

## التثبيت

```bash
python -m venv .venv
source .venv/Scripts/activate
python -m pip install -r requirements.txt
```

## الاستخدام

```bash
python -m src.main data/raw/customers.csv
```

لتحديد أسماء مخصصة للملف النظيف والتقرير:

```bash
python -m src.main data/raw/customers.csv \
  --output data/processed/customers_clean.csv \
  --report reports/customers_report.txt
```

لعرض كل الخيارات:

```bash
python -m src.main --help
```

## تشغيل الاختبارات

```bash
python -m pytest -v
```
