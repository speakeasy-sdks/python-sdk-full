"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class OfferType(str, Enum):
    DISCOUNT = 'DISCOUNT'
    CASHBACK = 'CASHBACK'
    DISCOUNT_AND_CASHBACK = 'DISCOUNT_AND_CASHBACK'
    NO_COST_EMI = 'NO_COST_EMI'
