# FIAP — Fase 6 • Capítulo 1 (Grupo 47)
**Autor:** Deivisson Gonçalves Lima · **RM565095**  
**Trabalho:** Individual · **Tema:** Detecção de Objetos (YOLOv5)

---

## 🎯 Objetivo
Treinar e validar um detector de objetos com **YOLOv5**, usando um subconjunto do **Open Images V7** com **2 classes**:

- `copo` (*Coffee cup*)
- `controle` (*Remote control*)

O projeto cobre: coleta e exportação do dataset no **formato YOLOv5**, treino (30 e 60 épocas), validação, inferência e análise dos resultados.

---

## 📁 Estrutura do repositório
```
Fase6_Cap1/
├─ README.md
├─ .gitignore
├─ notebooks/
│  └─ DeivissonLima_RM565095_fase6_cap1_colab_v4.ipynb   # Colab pronto (CPU/GPU)
├─ scripts/                                              # utilitários (opcional)
├─ data/                                                 # data.yaml de exemplo (opcional)
├─ imagens/                                              # evidências para o relatório
└─ assets/                                               # figuras/prints auxiliares
```
> **Windows (local):** `C:\Users\deivi\Downloads\FIAP\Fase6\Fase6_Cap1`  
> **Google Drive (projeto):** https://drive.google.com/drive/folders/1v_7_-mRXQMhjXRD-8zr-zfQlK8O52MX2?usp=drive_link

---

## ▶️ Execução rápida no Google Colab
1. Abra **notebooks/DeivissonLima_RM565095_fase6_cap1_colab_v4.ipynb** no Colab.  
2. Execute as células **na ordem**. O notebook:
   - Instala e corrige compatibilidades do **FiftyOne** (Colab / Py3.12)
   - Faz **download** de amostras do **Open Images V7** (40 por classe → 80 imagens)
   - Gera **splits**: `train/val/test` = **64 / 8 / 8**
   - Exporta no **formato YOLOv5** (com *fix* de subpastas)
   - Gera o arquivo `/content/fase6_data/data.yaml`
   - Executa 2 treinos “rápidos” (30 e 60 épocas) + **validação** + **inferência**
3. Resultados ficam em: `/content/drive/MyDrive/Fase6/Fase6_Cap1/runs/`

---

## 🧪 Dataset (resumo)
- Fonte: **Open Images V7** via **FiftyOne zoo**
- Classes: `Coffee cup`, `Remote control`
- Amostragem: **40** por classe (total **80**)
- Splits: **64** imagens treino · **8** validação · **8** teste
- Exportação: `YOLOv5Dataset` com **cópia** de mídia (sem *symlink*)
- Estrutura final (no runtime):
  ```
  /content/fase6_data/
  ├─ train/{images,labels}
  ├─ val/{images,labels}
  ├─ test/{images,labels}
  └─ data.yaml
  ```

---

## ⚙️ Experimentos
### Exp. 1 — 30 épocas (rápido)
- **weights:** `yolov5n.pt`
- **img:** 512 (GPU) / 448 (CPU) · **batch:** 32 (GPU) / 8 (CPU)
- **cache:** ram · **freeze:** 10 · **patience:** 10  
- Saída: `runs/exp_e30_fast` (ou `exp_e30_fast_cpu`)

### Exp. 2 — 60 épocas (rápido)
- **weights:** `yolov5s.pt`
- **img:** 512 (GPU) / 448 (CPU) · **batch:** 32 (GPU) / 8 (CPU)
- **cache:** ram · **freeze:** 10 · **patience:** 15  
- Saída: `runs/exp_e60_fast` (ou `exp_e60_fast_cpu`)

### Validação & Inferência
- Val: `runs/exp_e30_val`, `runs/exp_e60_val`
- Inferência (val): `runs/infer_val_e60`

---

## 📊 Resultados (execução real em CPU)
- **Val (30 épocas):** mAP@0.5 ≈ **0.413**  
  - `copo` ~ **0.537** · `controle` ~ **0.288**
- **Val (60 épocas):** mAP@0.5 ≈ **0.577**  
  - `copo` ~ **0.564** · `controle` ~ **0.590**
- **Observações**
  - 60 épocas elevou *precision/recall* (especialmente para **controle**)
  - Base pequena (**80** imagens) e pouca diversidade → limita generalização
  - Próximos passos: aumentar dados, *augmentations* (mosaic/scale/hsv), *tuning* de LR e *scheduler*

> Prints e imagens de inferência foram colocados em **/imagens** e no Drive em **evidencias/**.

---

## 🎬 Roteiro do vídeo (até 5 min)
1. Mostrar `/content/fase6_data/` e `data.yaml`  
2. Explicar os gráficos `results.png` (**30 vs 60 épocas**)  
3. Passar pelas detecções em `runs/infer_val_e60`  
4. Conclusões + próximos passos

---

## ✅ Checklist da entrega
- [ ] Repositório **público** no GitHub com este README
- [ ] Notebook nomeado: **DeivissonLima_RM565095_fase6_cap1_colab_v4.ipynb**
- [ ] Link do vídeo no README (YouTube **não listado**)
- [ ] Pasta **/imagens** com prints essenciais (ou Drive `/evidencias`)

---

## 💻 Comandos Git (lembrar de trocar a URL)
```bash
git init
git add .
git commit -m "Fase 6 - Cap 1: YOLOv5 (dataset, treino, validação, inferência)"
git branch -M main
git remote add origin https://github.com/limadeivisson/Fase6_Cap1.git
git push -u origin main
```
