@echo off
setlocal enabledelayedexpansion

echo Processing File, Mohon Tunggu



cd scripts
python main.py ../Data/LaporanDownload/LaporanTerkenaCopas -s 5 -o ../Data/OutputPlagiate

echo File Sudah Berhasil di Render,silahkan cek copas anda


pause


