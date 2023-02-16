from dataclasses import dataclass


@dataclass
class Tag:
    t_name: str
    t_type: str
    t_len: int | None
    t_sure: bool


@dataclass
class Header:
    e_name: str
    tags: list[Tag]

