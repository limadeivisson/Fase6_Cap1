#!/usr/bin/env python3
import os, glob, sys
BASE = sys.argv[1] if len(sys.argv) > 1 else "/content/fase6_data"
for s in ["train","val","test"]:
    imgs = glob.glob(f"{BASE}/{s}/images/*")
    lbls = glob.glob(f"{BASE}/{s}/labels/*")
    print(f"{s}: imgs={len(imgs)} | labels={len(lbls)}")
