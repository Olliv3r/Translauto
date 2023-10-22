# Translator Auto
Traduz arquivos de legenda .srt
![main](https://github.com/Olliv3r/Translator-Auto/blob/main/media/main.gif)

> [!IMPORTANT]
> Instalação dos requisitos
```
apt update && apt install git python python-pip -y
git clone https://github.com/Olliv3r/Translator-Auto
cd Translator-Auto && pip install -r requirements.txt
```

Exemplos:
Traduz a legenda de um arquivo específico:
```
./t-auto.py -s en -t pt -f subtitle/subtitle.srt
```
Traduz a legenda de múltiplos arquivos do diretório padrão `subtitle`:
```
./t-auto -s en -t pt -a
```
Substituí o arquivo de origem pelo novo traduzido:
```
./t-auto -s auto -t pt -a -r
```
Obs!: *Antes de utilizar a opção `-r` ou `--replace-file` faça backup dos arquivos de legenda de origem, pois ao habilitar a substuição do arquivo de origem pelo traduzido através da opção `-r` ou `--replace-file`, poderá perder o arquivo antigo*.

> [!NOTE]
> Se queira traduzir vários arquivos de legenda `.srt` você precisa copiá-los para dentro do diretório `subtitle` o qual o programa usa para traduzir mais de um arquivo de legenda `.srt`. Se for apenas um arquivo não há necessidade de fazer esta etapa.

> [!WARNING]
> Caso deseja traduzir um idioma que você desconhece, basta expecificar a opção `source` o valor `auto`, sendo assim o programa vai detectar o idioma de origem e traduzí-lo imediatamente:
```
./t-auto.py --source=auto --target=pt --file <FILE>
```

Nos exemplos acima a tradução foi realizada somente do idioma `english` para o `portuguese`, é possível traduzir o arquivo para qualquer idioma disponível. Todos os idiomas podem ser acessados usando a opção `--languages`:
```
./t-auto.py --languages
```

### Recursos:

- [x] Tradução de arquivos de legendas
- [ ] Outros

© Copyright [Olliver](https://github.com/Olliv3r/).
