@echo off
setlocal

REM Define o diretório onde o arquivo Python está localizado
set "diretorio=Z:\Documentos Compartilhados\GERAL MATRIZ\INTELIGENCIA\BI\PowerBI - Geral Cotrasa\Bot\Front"

REM Navegar até o diretório
cd "%diretorio%"

REM Executar o script Python
python index.py


endlocal

