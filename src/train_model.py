from .config import url_data_enero
from .data.dataset import main as load_data
from .features.build_features import main as build_features
from .modeling.train import main as train_model

def main():
    df_febrero = load_data(url_data_enero, save_parquet=False)
    df_febrero = build_features(df_febrero, bool_header=False)
    train_model(df_febrero)