"""Tests for sphinx.util.parallel."""

from __future__ import annotations

import time

import pytest

from sphinx.util.parallel import ParallelTasks, parallel_available


class _MergeError(Exception):
    pass


@pytest.mark.skipif(not parallel_available, reason='requires parallel support')
def test_exception_in_result_func_is_propagated() -> None:
    def result_func(arg: object, result: object) -> None:
        raise _MergeError

    tasks = ParallelTasks(2)
    tasks.add_task(lambda: None, result_func=result_func)
    with pytest.raises(_MergeError):
        tasks.join()


@pytest.mark.skipif(not parallel_available, reason='requires parallel support')
def test_exception_in_result_func_is_propagated_from_add_task() -> None:
    def result_func(arg: object, result: object) -> None:
        raise _MergeError

    tasks = ParallelTasks(1)
    tasks.add_task(lambda: None, result_func=result_func)
    # let the first task finish, so that the next add_task() collects it
    time.sleep(0.5)
    with pytest.raises(_MergeError):
        tasks.add_task(lambda: None)
