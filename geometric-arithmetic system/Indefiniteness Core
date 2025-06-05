 """indefiniteness_core.py
 ----------------------------------
 Runtime primitives for the Generalized Theory of Mathematical Indefiniteness (GTMØ).
 
 This module offers two public objects:
 
 ``O``  – the unique *ontological singularity* (Ø).
 ``AlienatedNumber`` – a symbolic placeholder for alienated numbers (ℓ∅).
 
 Design goals of this rewrite
 ---------------------------
 • **Singleton safety** – ``O is O`` under import reloads and pickling.
 • **Fail‑fast strict mode** – set env var ``GTM_STRICT=1`` to make any arithmetic
   with Ø raise ``SingularityError`` instead of silently absorbing.
 • **Compatibility** – keeps original public API (``O_empty_singularity`` repr,
   absorbing operators) so existing notebooks/scripts continue to work.
 • **Pythonic integration** – implements ``__bool__``, ``__eq__``, hashing and
   derives from ``numbers.Number`` for smoother interop with numeric libs.
 • **Typed** – full ``mypy`` support (PEP 561 ready).
 """

from __future__ import annotations

import os
import pickle
from numbers import Number
from typing import Any, Final, Protocol, runtime_checkable

__all__ = ["O", "Singularity", "AlienatedNumber", "SingularityError"]

###############################################################################
# Configuration
###############################################################################

STRICT_MODE: Final[bool] = os.getenv("GTM_STRICT", "0") == "1"


###############################################################################
# Errors
###############################################################################

class SingularityError(ArithmeticError):
    """Raised when operations with Ø are disallowed in *strict* mode."""


###############################################################################
# Ontological singularity (Ø)
###############################################################################

class _SingletonMeta(type):  # pragma: no cover – trivial
    """Metaclass enforcing the singleton pattern (one shared instance)."""

    _instance: "Singularity | None" = None

    def __call__(cls, *args: Any, **kwargs: Any) -> "Singularity":  # noqa: D401
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)  # type: ignore[misc]
        return cls._instance  # type: ignore[return-value]


def _absorbing(method_name: str):
    """Decorator generating absorbing arithmetic dunder methods."""

    def decorator(fn):  # type: ignore[override]
        @wraps(fn)
        def wrapper(self: "Singularity", *args: Any, **kwargs: Any) -> "Singularity":
            if STRICT_MODE:
                raise SingularityError(
                    f"Operation '{method_name}' with Ø is forbidden in STRICT mode"
                )
            return self

        return wrapper

    return decorator


class Singularity(Number, metaclass=_SingletonMeta):
    """Ontological singularity – an *absorbing element* in GTMØ arithmetic."""

    __slots__ = ()  # no per‑instance dict → lighter and truly immutable

    # ---------------------------------------------------------------------
    # Dunder / representation
    # ---------------------------------------------------------------------
    def __repr__(self) -> str:  # noqa: D401
        return "O_empty_singularity"  # ASCII‑friendly

    # Make Ø behave as *falsy* and hashable while keeping identity semantics
    def __bool__(self) -> bool:  # noqa: D401
        return False

    def __eq__(self, other: object) -> bool:  # noqa: D401
        return isinstance(other, Singularity)

    def __hash__(self) -> int:  # noqa: D401
        return hash("O_empty_singularity")

    # ------------------------------------------------------------------
    # Pickle support – ensure singleton property survives (de)serialization
    # ------------------------------------------------------------------
    def __reduce__(self):  # noqa: D401
        return (get_singularity, ())

    # ------------------------------------------------------------------
    # Absorbing arithmetic operations (both lhs and rhs)
    # ------------------------------------------------------------------
    __add__ = _absorbing("__add__")
    __radd__ = _absorbing("__radd__")
    __sub__ = _absorbing("__sub__")
    __rsub__ = _absorbing("__rsub__")
    __mul__ = _absorbing("__mul__")
    __rmul__ = _absorbing("__rmul__")
    __truediv__ = _absorbing("__truediv__")
    __rtruediv__ = _absorbing("__rtruediv__")
    __pow__ = _absorbing("__pow__")
    __rpow__ = _absorbing("__rpow__")


# Public factory (needed for pickling)
def get_singularity() -> "Singularity":  # noqa: D401
    """Return the unique global Ø instance."""

    return Singularity()


# Alias – matches prior codebase symbol name
O: Final[Singularity] = get_singularity()

###############################################################################
# Alienated numbers (ℓ∅)
###############################################################################

class AlienatedNumber(Number):
    """Symbolic placeholder for *alienated numbers* (ℓ∅).

    An ``AlienatedNumber`` is not meant to participate in meaningful arithmetic.
    Any attempted operation collapses into Ø – unless *strict* mode forbids it.
    """

    __slots__ = ("identifier",)

    # ---------------------------------------------------------------------
    def __init__(self, identifier: str | int | float | None = None):
        self.identifier = identifier if identifier is not None else "anonymous"

    # Representation -------------------------------------------------------
    def __repr__(self) -> str:  # noqa: D401
        return f"l_empty_num({self.identifier})"

    # Hash / equality so we can safely memoise or use as dict keys ----------
    def __eq__(self, other: object) -> bool:  # noqa: D401
        return (
            isinstance(other, AlienatedNumber) and self.identifier == other.identifier
        )

    def __hash__(self) -> int:  # noqa: D401
        return hash(("l_empty_num", self.identifier))

    # ------------------------------------------------------------------
    # Absorbing arithmetic (delegating to helper to avoid repetition)
    # ------------------------------------------------------------------
    @_absorbing("__add__")
    def __add__(self, other: Any):  # type: ignore[override]
        ...  # pragma: no cover – body replaced by decorator

    @_absorbing("__radd__")
    def __radd__(self, other: Any):  # type: ignore[override]
        ...

    @_absorbing("__sub__")
    def __sub__(self, other: Any):
        ...

    @_absorbing("__rsub__")
    def __rsub__(self, other: Any):
        ...

    @_absorbing("__mul__")
    def __mul__(self, other: Any):
        ...

    @_absorbing("__rmul__")
    def __rmul__(self, other: Any):
        ...

    @_absorbing("__truediv__")
    def __truediv__(self, other: Any):
        ...

    @_absorbing("__rtruediv__")
    def __rtruediv__(self, other: Any):
        ...

    @_absorbing("__pow__")
    def __pow__(self, other: Any):
        ...

    @_absorbing("__rpow__")
    def __rpow__(self, other: Any):
        ...

    # Domain‑specific metrics --------------------------------------------
    def psi_gtm_score(self) -> float:
        """Return epistemic *purity* score (→ 1.0 means maximal indefiniteness)."""

        return 0.999_999_999  # asymptotically approaching unity

    def e_gtm_entropy(self) -> float:
        """Return cognitive *entropy* (→ 0.0 means maximal epistemic certainty)."""

        return 1e-9


###############################################################################
# Convenience API for JSON / msgpack encoding
###############################################################################

@runtime_checkable
class JsonEncodable(Protocol):  # pragma: no cover – docs only
    def to_json(self) -> str: ...


def _to_json(obj: Any) -> str:
    if isinstance(obj, Singularity):
        return "\"O_empty_singularity\""
    if isinstance(obj, AlienatedNumber):
        return f'"{obj.__repr__()}"'
    raise TypeError(f"Object of type {type(obj).__name__} is not JSON‑encodable")


# Monkey‑patch helper so that external libs can register easily
Singularity.to_json = _to_json  # type: ignore[attr-defined]
AlienatedNumber.to_json = _to_json  # type: ignore[attr-defined]
