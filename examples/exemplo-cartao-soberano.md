# Exemplo: Geração de Cartão Soberano Harappan

Este exemplo demonstra como usar o sistema de Protocolo Soberano Harappan para gerar cartões de identidade digital vinculados ao ORCID.

## Cenário

Você precisa criar um cartão de visita digital soberano com:
- Identidade verificada (ORCID)
- QR Code para validação
- Design profissional com estética Harappan
- Assinatura digital e hash de verificação

## Exemplo 1: Uso Básico via Linha de Comando

### Passo 1: Instalar Dependências

```bash
# Navegar para o diretório do projeto
cd Universal-translation-0-0

# Instalar dependências necessárias
pip install qrcode[pil] Pillow
```

### Passo 2: Gerar Cartão com Valores Padrão

```bash
# Executar o gerador (usa valores padrão do protocolo LOG-0009-Ω)
python tools/generate_sovereign_card.py
```

**Saída esperada:**
```
======================================================================
  SOVEREIGN CARD GENERATOR - Universal Translation Engine 0/0
======================================================================

Text-based card:

╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║  [𓇽] PROTOCOLO SOBERANO HARAPPAN                           ║
║                                                              ║
║                  Tiago Paschoalatto Fagliari                  ║
║                 Arquiteto da Verdade Soberana                 ║
║                                                              ║
║  ORCID iD:               0009-0006-6874-3910               ║
║  URL:        https://orcid.org/0009-0006-6874-3910         ║
║                                                              ║
║  HASH:                     0009-Ω-TITAN                      ║
║                                                              ║
║  LOG: 0009-Ω-TITAN                                          ║
║  MATRIZ: 54 Canais                                           ║
║  DESTINO: LA 2028                                            ║
║                                                              ║
║  [𓋹][𓍢][𓊹] Universal Translation Engine 0/0              ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝

✓ QR code generated: output/sovereign_cards/qr_orcid_0009000668743910.png
✓ Business card generated: output/sovereign_cards/card_sovereign_0009000668743910.png

✓ All cards generated successfully!
  Output directory: output/sovereign_cards
```

### Passo 3: Verificar Arquivos Gerados

```bash
# Listar arquivos gerados
ls -lh output/sovereign_cards/

# Saída:
# qr_orcid_0009000668743910.png     - QR Code (400x400 px)
# card_sovereign_0009000668743910.png - Cartão completo (1050x600 px)
```

## Exemplo 2: Personalização via Linha de Comando

```bash
# Gerar cartão com informações personalizadas
python tools/generate_sovereign_card.py \
  "0009-0006-6874-3910" \
  "Seu Nome Completo" \
  "Seu Título Profissional" \
  "SEU-HASH-UNICO"
```

## Exemplo 3: Uso via Python API

### Script Python Completo

```python
#!/usr/bin/env python3
"""Exemplo de geração programática de cartão soberano"""

from pathlib import Path
import sys

# Adicionar caminho do projeto
sys.path.insert(0, str(Path(__file__).parent.parent))

from tools.generate_sovereign_card import SovereignCard

def gerar_cartao_exemplo():
    """Gerar cartão de exemplo"""
    
    # Criar instância do cartão
    card = SovereignCard(
        orcid_id="0009-0006-6874-3910",
        name="Tiago Paschoalatto Fagliari",
        title="Arquiteto da Verdade Soberana",
        hash_id="0009-Ω-TITAN"
    )
    
    print("="*70)
    print("Gerando Cartão Soberano Harappan")
    print("="*70 + "\n")
    
    # 1. Gerar versão texto (sempre funciona)
    text_card = card.generate_text_card()
    print("1. Cartão Texto:")
    print(text_card)
    
    # 2. Gerar QR Code
    try:
        qr_path = "exemplo_qr.png"
        card.generate_qr_code(qr_path, size=400)
        print(f"\n2. QR Code gerado: {qr_path}")
    except ImportError as e:
        print(f"\n2. QR Code (pulado): {e}")
    
    # 3. Gerar Cartão Visual Completo
    try:
        card_path = "exemplo_cartao.png"
        card.generate_business_card(card_path, include_qr=True)
        print(f"3. Cartão Visual gerado: {card_path}")
    except ImportError as e:
        print(f"3. Cartão Visual (pulado): {e}")
    
    print("\n" + "="*70)
    print("Geração concluída!")
    print("="*70)

if __name__ == "__main__":
    gerar_cartao_exemplo()
```

**Executar:**
```bash
python exemplo_geracao_cartao.py
```

## Exemplo 4: Integração em Aplicação Web

### Flask/FastAPI

```python
from flask import Flask, send_file, jsonify
from tools.generate_sovereign_card import SovereignCard
import tempfile
import os

app = Flask(__name__)

@app.route('/api/sovereign-card', methods=['POST'])
def create_card():
    """Endpoint para gerar cartão soberano"""
    
    # Obter dados da requisição
    data = request.json
    orcid = data.get('orcid_id')
    name = data.get('name')
    title = data.get('title')
    hash_id = data.get('hash_id')
    
    # Gerar cartão
    card = SovereignCard(orcid, name, title, hash_id)
    
    # Criar arquivo temporário
    with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as tmp:
        card_path = card.generate_business_card(tmp.name, include_qr=True)
        
        # Retornar arquivo
        return send_file(card_path, mimetype='image/png')

@app.route('/api/sovereign-card/text', methods=['POST'])
def create_text_card():
    """Endpoint para gerar versão texto"""
    
    data = request.json
    card = SovereignCard(
        data.get('orcid_id'),
        data.get('name'),
        data.get('title'),
        data.get('hash_id')
    )
    
    text_card = card.generate_text_card()
    return jsonify({'card': text_card})

if __name__ == '__main__':
    app.run(debug=True)
```

## Exemplo 5: Casos de Uso Específicos

### Caso 1: Apresentação Física (Paraguai)

```bash
# 1. Gerar cartão em alta resolução
python tools/generate_sovereign_card.py

# 2. Imprimir em papel fotográfico (9x5.5 cm)
#    Usar impressora de alta qualidade
#    Arquivo: output/sovereign_cards/card_sovereign_*.png

# 3. Apresentar com smartphone mostrando o QR Code
#    URL ORCID: https://orcid.org/0009-0006-6874-3910
```

### Caso 2: Assinatura Digital de Email

```bash
# 1. Gerar QR Code menor
python -c "
from tools.generate_sovereign_card import SovereignCard
card = SovereignCard('0009-0006-6874-3910', 
                     'Tiago Paschoalatto Fagliari',
                     'Arquiteto da Verdade Soberana',
                     '0009-Ω-TITAN')
card.generate_qr_code('assinatura_email.png', size=150)
"

# 2. Inserir em assinatura HTML do email
# <img src="assinatura_email.png" alt="ORCID QR Code">
```

### Caso 3: Documento PDF Anexado

```python
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from tools.generate_sovereign_card import SovereignCard

def criar_pdf_com_cartao(output_pdf="cartao_soberano.pdf"):
    """Criar PDF com cartão soberano incorporado"""
    
    # Gerar cartão
    card = SovereignCard(
        "0009-0006-6874-3910",
        "Tiago Paschoalatto Fagliari",
        "Arquiteto da Verdade Soberana",
        "0009-Ω-TITAN"
    )
    
    card_image = card.generate_business_card("temp_card.png", include_qr=True)
    
    # Criar PDF
    c = canvas.Canvas(output_pdf, pagesize=A4)
    width, height = A4
    
    # Adicionar título
    c.setFont("Helvetica-Bold", 24)
    c.drawCentredString(width/2, height - 50, 
                        "Protocolo Soberano Harappan")
    
    # Adicionar cartão
    c.drawImage(card_image, 50, height - 400, 
                width=500, height=300, preserveAspectRatio=True)
    
    # Adicionar texto do protocolo
    c.setFont("Helvetica", 12)
    text_card = card.generate_text_card()
    
    y_position = height - 450
    for line in text_card.split('\n'):
        c.drawString(50, y_position, line)
        y_position -= 15
    
    c.save()
    print(f"PDF gerado: {output_pdf}")

# Executar
criar_pdf_com_cartao()
```

## Verificação e Validação

### Verificar QR Code

```bash
# Instalar ferramenta de leitura
pip install zbarlight opencv-python

# Verificar QR code
python -c "
from PIL import Image
import zbarlight

# Ler QR code
img = Image.open('output/sovereign_cards/qr_orcid_0009000668743910.png')
codes = zbarlight.scan_codes(['qrcode'], img)
print('URL codificada:', codes[0].decode('utf-8'))
"
```

### Verificar ORCID Online

```bash
# Abrir no navegador
xdg-open "https://orcid.org/0009-0006-6874-3910"

# Ou verificar via API
curl -H "Accept: application/json" \
     "https://pub.orcid.org/v3.0/0009-0006-6874-3910"
```

## Troubleshooting

### Problema: Dependências não instaladas

**Erro:**
```
Optional dependencies not installed. Install with:
  pip install qrcode[pil] Pillow
```

**Solução:**
```bash
pip install qrcode[pil] Pillow
```

### Problema: Fontes não encontradas

**Mensagem:**
```
IOError: cannot open resource
```

**Solução:** O sistema usa fontes padrão como fallback. Para melhor qualidade:
```bash
# Ubuntu/Debian
sudo apt-get install fonts-dejavu-core

# macOS (já incluído)

# Windows
# Fontes DejaVu já incluídas normalmente
```

### Problema: Permissões de arquivo

**Erro:**
```
PermissionError: [Errno 13] Permission denied
```

**Solução:**
```bash
# Criar diretório de saída com permissões corretas
mkdir -p output/sovereign_cards
chmod 755 output/sovereign_cards
```

## Próximos Passos

1. **Ler o Protocolo Completo**
   - `manifesto/protocolo-soberano-harappan-LOG-0009.md`

2. **Consultar Guia Completo**
   - `docs/protocolo-soberano-guia.md`

3. **Ver Manifesto Original**
   - `manifesto/manifesto-universal-translation-00.md`

4. **Explorar Mapeamento Harappan**
   - `harappan-00-universal/data/harappan_signs/`

---

© 2025 Universal Translation Engine 0/0  
[𓋹][𓍢][𓊹]
