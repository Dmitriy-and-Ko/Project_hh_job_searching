from src.api_hh import HHJobPlatform
import pytest
from src.abstract import JobPlatformAPI

def test_hh_api_init(head_hunter_example):
    assert head_hunter_example.base_url == "https://api.hh.ru/vacancies"