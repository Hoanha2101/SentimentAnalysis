import torch
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import emoji as ej
import string 

from gensim.utils import simple_preprocess
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

import torch.nn as nn
from torch.optim import AdamW
from torch.utils.data import Dataset, DataLoader

from transformers import get_linear_schedule_with_warmup, AutoTokenizer, AutoModel, logging


from transformers import get_linear_schedule_with_warmup, AutoTokenizer, AutoModel, logging
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import  Conv1D, Embedding, Dense, Dropout, Bidirectional, LSTM, GRU, Input, GlobalMaxPooling1D, LayerNormalization, MaxPooling1D
from tensorflow.keras.optimizers import Adam, SGD

import random
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from pyvi import ViTokenizer
from pyvi import ViUtils
import py_vncorenlp
from vncorenlp import VnCoreNLP

import pickle


import warnings
warnings.filterwarnings("ignore")

logging.set_verbosity_error()