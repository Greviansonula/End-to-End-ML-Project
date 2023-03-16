import os
import sys
from dataclasses import dataclass

from catboost import CatBoostingRegressor
from sklearn.ensemble import (
    AdaBoostingRegressor,
    GradientBoostingRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor,
)

from sklearn.linear_model import LinearRegression
from skearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src.exception import CustomException
from src.logger import logging

from src.utils import save_obj

