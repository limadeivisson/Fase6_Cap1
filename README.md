# FIAP – Fase 6 • Capítulo 1 — FarmTech Solutions (YOLOv5)

**Autor:** Deivisson Gonçalves Lima — **RM565095**  
**Grupo:** 47 (trabalho individual)  
**Período:** 10/09/2025 a 14/10/2025  
**Notebook (Colab):** `notebooks/DeivissonLima_RM565095_fase6_cap1_colab_v4_1.ipynb` (GPU) · `notebooks/DeivissonLima_RM565095_fase6_cap1_colab_v4_2_cpu.ipynb` (CPU)

---

## 🎯 Objetivo
Construir um sistema de **detecção de objetos** com **YOLOv5**, demonstrando preparação de dataset, treinamento, validação, inferência e análise.  
Classes escolhidas (Open Images V7):
- `copo` (*Coffee cup*)
- `controle` (*Remote control*)

---

## 📁 Estrutura sugerida do repositório
```
Fase6_Cap1/
├─ README.md
├─ notebooks/
│  ├─ DeivissonLima_RM565095_fase6_cap1_colab_v4_1.ipynb   # Colab (GPU)
│  └─ DeivissonLima_RM565095_fase6_cap1_colab_v4_2_cpu.ipynb # Colab (CPU)
├─ data/
│  └─ data.yaml  # referência (no Colab é gerado em /content/fase6_data/data.yaml)
├─ scripts/
│  └─ check_counts.py  # utilitário para contar imagens/labels por split
└─ runs/               # resultados do YOLOv5 (gerados em execução)
```
> **Local (Windows):** `C:\\Users\\deivi\\Downloads\\FIAP\\Fase6\\Fase6_Cap1`  
> **Drive (Google):** `MyDrive/Fase6/Fase6_Cap1` — pasta do projeto.

---

## 🚀 Como executar (resumo)
1. Abra o **Google Colab** e carregue o notebook **GPU** (v4.1) ou **CPU** (v4.2).  
2. Execute as células **na ordem**. Se o Colab solicitar, **reinicie** após instalar o FiftyOne.  
3. O notebook irá:
   - Baixar o **Open Images V7** apenas nas classes `Coffee cup` e `Remote control`  
   - Selecionar **40** imagens por classe e montar splits **32/4/4** (train/val/test)  
   - **Exportar por split** no formato YOLOv5 (com correção de subpastas)  
   - Gerar `data.yaml` local (`/content/fase6_data/data.yaml`)  
   - Treinar **30** e **60** épocas (versão rápida)  
   - Rodar **validação** e **inferência**

---

## 🧪 Dataset & Splits
- Fonte: **Open Images V7** via **FiftyOne**  
- Amostragem: **40** por classe (total **80**)  
- Splits por classe: **32** treino, **4** validação, **4** teste → total **64/8/8**  
- Export: YOLOv5 com **cópia de mídia** (sem symlinks)

Árvore no runtime do Colab:
```
/content/fase6_data/
├─ train/
│  ├─ images/*.jpg|png
│  └─ labels/*.txt
├─ val/
│  ├─ images/*.jpg|png
│  └─ labels/*.txt
├─ test/
│  ├─ images/*.jpg|png
│  └─ labels/*.txt
└─ data.yaml
```

---

## ⚙️ Experimentos (rápidos)
### Exp 1 — 30 épocas (rápido)
- `weights`: `yolov5n.pt`  
- `--img 512 (GPU) / 448 (CPU)` • `--batch 32 (GPU) / 8 (CPU)`  
- `--cache ram` • `--freeze 10` • `--patience 10`  
- Pasta: `runs/exp_e30_fast` (GPU) ou `runs/exp_e30_fast_cpu` (CPU)

### Exp 2 — 60 épocas (rápido)
- `weights`: `yolov5s.pt`  
- `--img 512 (GPU) / 448 (CPU)` • `--batch 32 (GPU) / 8 (CPU)`  
- `--cache ram` • `--freeze 10` • `--patience 15`  
- Pasta: `runs/exp_e60_fast` (GPU) ou `runs/exp_e60_fast_cpu` (CPU)

### Validação & Inferência
- Val: `runs/exp_e30_val`, `runs/exp_e60_val`  
- Inferência (prints): `runs/infer_val_e60` (ou `infer_test_e60`)

---

## 📊 Resultados (execução real)
- **Val (30 épocas / CPU)** → mAP@0.5 ≈ **0.413** (copo ~0.537; controle ~0.288)  
- **Val (60 épocas / CPU)** → mAP@0.5 ≈ **0.577** (copo ~0.564; controle ~0.590)  
- **Inferência** salva em: `runs/infer_val_e60` (com detecções nas 8 imagens de `val`)

> Interprete: aumentar épocas melhorou recall/precision, especialmente para **controle**.  
> Limitações: base pequena (80 imgs), diversidade limitada, variação de contexto.  
> Próximos passos: mais dados, augmentations (mosaic/scale/hsv), *tuning* de LR e arquiteturas.

---

## 🎥 Vídeo (até 5 min)
1. Mostrar a estrutura `/content/fase6_data/` e `data.yaml`  
2. Comparar `results.png` de 30 vs 60 épocas  
3. Exibir as imagens de `runs/infer_val_e60`  
4. Conclusões e limitações

> Publique **não listado** no YouTube e adicione o link no topo deste README e no **README do GitHub** do projeto.

---

## ✅ Checklist da entrega
- [ ] Repositório **público** no GitHub, com este README
- [ ] Notebook nomeado conforme: `DeivissonLima_RM565095_fase6_cap1.ipynb` (ou v4.1/v4.2)
- [ ] Link do vídeo (não listado) no README
- [ ] `runs/` com resultados (ou prints principais salvos em `/evidencias`)

---

## 💡 Comandos úteis (Git)
```bash
git init
git add .
git commit -m "Fase 6 - Cap 1 (YOLOv5): dataset, treino, validação e inferência"
git branch -M main
git remote add origin https://github.com/<seu-usuario>/<seu-repo>.git
git push -u origin main
```

---

## 📎 Identificação do notebook
Nome recomendado para submissão:  
`DeivissonLima_RM565095_fase6_cap1.ipynb`
