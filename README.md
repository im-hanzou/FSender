# Python Emails Sender

Python Email Sender

## Fitur

- Template kustom
- Email kustom
- Subjek kustom

## Konfigurasi

Ubah file `config.ini` sesuai dengan konfigurasi yang Anda miliki.

```ini
[smtp]
host=host
port=port (587)
username=username
password=password
from=mailfrom (Anda dapat menyesuaikannya)

[template]
subject=subject (Anda dapat menyesuaikannya)

[settings]
delay=5
```

## Template Kustom

Aplikasi ini mendukung placeholder template berikut untuk konten dinamis pada subjek email dan isi pesan:

- `$random_string(10)`: Menghasilkan teks acak dengan panjang 10 karakter.
- `$random_number(10)`: Menghasilkan angka acak dengan 10 digit.
- `$time()`: Menghasilkan tahun-bulan-tanggal jam:menit:detik 
- `$time(day)`: Mengembalikan hari saat ini (misalnya, Senin).
- `$time(date)`: Mengembalikan tanggal saat ini (misalnya, 01).
- `$time(month)`: Mengembalikan bulan saat ini (misalnya, 01).
- `$time(year)`: Mengembalikan tahun saat ini (misalnya, 2021).
- `$time(hour)`: Mengembalikan jam saat ini (misalnya, 01).
- `$time(minute)`: Mengembalikan menit saat ini (misalnya, 01).
- `$time(second)`: Mengembalikan detik saat ini (misalnya, 01).
- `$to_email()`: email penerima