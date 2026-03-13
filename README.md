# 🛡️ Iran-Internet-Revivall (Phantom Bridge)

تکنولوژی پیشرفته برای احیای اینترنت بین‌الملل در سرورهای ایزوله شده ایران این پروژه یک راهکار حرفه‌ای و تست‌شده برای بازگرداندن دسترسی به اینترنت جهانی در سرورهای داخل ایران است که به طور کامل از اینترنت بین‌الملل قطع شده‌اند. برخلاف روش‌های سنتی، این ابزار از تکنیک Reverse SSH Bridge استفاده می‌کند؛ به این معنا که سرور خارج، اینترنت را به قلب سرور ایران "تزریق" می‌کند.

---

## ✨ ویژگی‌های برجسته (Technical Highlights)
* نفوذ از لایه ورودی: عبور از محدودیت‌های فایروال ایران با استفاده از ترافیک ورودی (Inbound) به جای خروجی.
* پایداری هوشمند (Keep-Alive): جلوگیری از بسته شدن تونل توسط سیستم‌های شناسایی DPI با ارسال سیگنال‌های زنده ماندن.
* بهینه‌سازی شبکه (TCP BBR): فعال‌سازی الگوریتم گوگل در هسته لینوکس برای افزایش چشمگیر سرعت در شبکه‌های پر از اختلال.
* نصب خودکار (Zero-Config): اجرای کل پروسه پیچیده شبکه تنها با یک دستور.

---

## 🚀 آموزش قدم‌به‌گام راه‌اندازی (Step-by-Step)

### ۱. آماده‌سازی در سرور خارج (Foreign Server)
ابتدا باید به سروری که اینترنت آزاد دارد (مثل آلمان، فنلاند یا ...) وصل شوید تا نقش تامین‌کننده اینترنت را ایفا کند.

* دستور زیر را در ترمینال سرور خارج کپی و اجرا کنید:

```bash
curl -sLO [https://raw.githubusercontent.com/amirdavodi/Iran-Internet-Revivall/refs/heads/main/install.sh](https://raw.githubusercontent.com/amirdavodi/Iran-Internet-Revivall/refs/heads/main/install.sh) && bash install.sh

* گزینه 1 (Foreign Server) را انتخاب کنید.
* آی‌پی سرور ایران و یوزرنیم آن را وارد کنید.
* در صورت درخواست پسورد، آن را وارد نمایید.
* نکته: تا پایان مراحل در سرور ایران، این ترمینال را نبندید.

### ۲. اجرا و احیا در سرور ایران (Iran Server)
حالا به سرور داخل ایران (که اینترنت ندارد) متصل شوید.

* دقیقاً همان دستور بالا را کپی و اجرا کنید:

```bash
curl -sLO [https://raw.githubusercontent.com/amirdavodi/Iran-Internet-Revivall/refs/heads/main/install.sh](https://raw.githubusercontent.com/amirdavodi/Iran-Internet-Revivall/refs/heads/main/install.sh) && bash install.sh
