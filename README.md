# Skript komprimace.py
Skript, který komprimuje log soubory do gzip souborů za účelem ušetření místa.<br> 
Skript bude spouštěn jako linuxový cron job každých 30 dní. <br>
Původní, nezkomprimované soubory budou smazány, tedy v určeném adresáři zůstanou pouze gzip soubory.

# Příklad použití
Skript bude umístěn v root adresáři. Logy určené ke komprimaci musí být v umístění /var/log.<br>
V root adresáři vytvoříme crontab s příkazem: 0 0 1 * * /usr/bin/python3 /komprimace.py;

# Testy
* Do cílové složky /var/log nahrajeme/vytvoříme soubory např. test_log.log, test_log_a.log.gz a vytvoříme zde složku dir_test.
* Tímto ověříme
    * že skript zkomprimuje .log soubor do požadovaného formátu a nezkomprimovaný soubor smaže
    * bude ignorovat již existující gzip soubory
    * bude ignorovat složky
* Ve skriptu odkomentujeme na řádky 13, 55 a 58
* V root adresáři, kde je umístěný samotný skript komprimace.py spustíme příkaz: python3 komprimace.py
* Výsledkem bude složka /var/log, obsahovat
    * test_log.log.gz
    * test_log_a.log.gz
    * složku dir_test
* Dostaneme hlášku "Total of 1 files were compressed"

* Stejným postupem můžeme nahrát například 20 nezkomprimovaných souborů a 10 zkomprimovaných souborů ve formátu gzip.
* Hláška by v tomto případě měla správně vypadat takto: "Total of 20 files were compressed"

