# Translauto
Tradutor de arquivos de legenda SRT
![main](https://github.com/Olliv3r/Translauto/blob/main/media/translauto.gif)

> [!IMPORTANT]
> Instalação dos requisitos
```
apt update && apt install git python python-pip -y
git clone https://github.com/Olliv3r/Translauto
cd Translauto && pip install -r requirements.txt
```

Exemplos:
Traduz um arquivo de legenda específico:
```
./translauto.py -s auto -t pt -f subtitle/subtitle.srt
```
Traduz múltiplos arquivos de legenda do diretório padrão `subtitle` ou outro que pode ser expecificado através da variável de ambiente `T_AUTO_DIR`:
```
./translauto.py -s en -t pt -a
```
Substituí o arquivo de origem pelo o novo que será traduzido:
```
./translauto.py -s auto -t pt -a -r
```
Obs!: *Antes de utilizar a opção `-r` ou `--replace-file` faça backup dos arquivos de legenda de origem, pois ao habilitar a substituição do arquivo de origem pelo traduzido através da opção `-r` ou `--replace-file`, poderá perder o arquivo antigo*.

> [!NOTE]
> Se queira traduzir vários arquivos de legenda `.srt` você precisa copiá-los para dentro do diretório `subtitle` o qual o programa usa para traduzir mais de um arquivo de legenda `.srt`. Se for apenas um arquivo não há necessidade de fazer esta etapa.
> Caso queira expecificar um diretório padrão personalizado, basta definir a variável de ambiente `T_AUTO_DIR` com o caminho completo do novo diretório, por exemplo:

```
export T_AUTO_DIR=/sdcard/subtitles
```

> [!WARNING]
> Caso deseja traduzir um idioma que você desconhece, basta expecificar a opção `source` o valor `auto`, sendo assim o programa vai detectar o idioma de origem e traduzí-lo imediatamente:
```
./translauto.py --source=auto --target=pt --file <FILE>
```

Nos exemplos acima a tradução foi realizada somente do idioma `english` para o `portuguese`, é possível traduzir o arquivo para qualquer idioma disponível. Todos os idiomas podem ser acessados usando a opção `--languages`:
```
./translauto.py --languages
```

### Recursos:

- [x] Tradução de arquivos de legendas
- [ ] Outros

© Copyright [Olliver](https://github.com/Olliv3r)
