from dataclasses import dataclass


@dataclass
class Tag:
    t_name: str
    t_type: str
    t_sure: bool
    t_len: int | None


@dataclass
class Header:
    e_name: str
    tags: list[Tag]

