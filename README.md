Translauto

**Translauto** é um tradutor de arquivos de legenda `.srt` simples e eficiente, que permite traduzir automaticamente suas legendas para diferentes idiomas.

![main](https://github.com/Olliv3r/Translauto/blob/main/media/translauto.gif)

### Instalação

#### 1. Atualize os pacotes e instale as dependências necessárias:

```
apt update && apt install git python python-pip -y
```

#### 2. Clone o repositório e instale os pacotes requeridos:

```
git clone https://github.com/Olliv3r/Translauto
```
```
cd Translauto && pip install -r requirements.txt
```

### Exemplos de Uso

Traduzir um arquivo de legenda específico:
Para traduzir um arquivo .srt de um idioma de origem para o idioma de destino, use:

```
./translauto.py -s auto -t pt -f subtitle/subtitle.srt
```

Onde:

-s auto detecta automaticamente o idioma de origem.

-t pt especifica o idioma de destino (Português).

-f subtitle/subtitle.srt é o caminho para o arquivo de legenda a ser traduzido.

Traduzir múltiplos arquivos de legenda:
Para traduzir todos os arquivos .srt dentro do diretório padrão subtitle (ou de outro diretório especificado pela variável de ambiente `T_AUTO_DIR`), use:

```
./translauto.py -s en -t pt -a
```

Onde:

-s en define o idioma de origem como Inglês.

-t pt define o idioma de destino como Português.

-a significa traduzir todos os arquivos .srt no diretório.

#### Substituir o arquivo de origem pelo traduzido:

Se você deseja substituir o arquivo de legenda original pela versão traduzida, use a opção -r (ou --replace-file). Atenção: Faça backup dos arquivos antes de usar esta opção, pois o arquivo original será substituído.

```
./translauto.py -s auto -t pt -a -r
```

#### Traduzir detectando automaticamente o idioma de origem:

Se você não sabe o idioma de origem, use auto para que o programa detecte automaticamente o idioma e traduza para o idioma de destino:

```
./translauto.py --source=auto --target=pt --file <FILE>
```

#### Personalizando o diretório de legendas:

Por padrão, o programa usa o diretório subtitle para armazenar os arquivos de legenda. Se desejar usar um diretório diferente, defina a variável de ambiente `T_AUTO_DIR` com o caminho completo do novo diretório. Exemplo:

```
export T_AUTO_DIR=/sdcard/subtitles
```

#### Exibir idiomas disponíveis:

Você pode consultar todos os idiomas suportados pela ferramenta com a opção --languages:

```
./translauto.py --languages
```

#### Recursos
 [-] Tradução de arquivos de legenda .srt
 [-] Outros recursos planejados

© Copyright Olliv3r
