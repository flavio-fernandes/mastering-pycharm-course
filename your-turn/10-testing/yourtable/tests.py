import pytest
import core


def test_pass():
    assert True

def test_there_are_tables_available():
    type_of_food = 1
    choices = core.find_available(type_of_food)
    assert choices, "Found no tables for food type, when there should be some"
    assert isinstance(choices, list), "Choices should be provided as a list"
    # assert False, "Use core to find_available by choice, make sure there is at least one"


def test_table_can_be_booked():
    for table in core.all_tables():
        assert table.is_booked is False, "Expected table to be available"
        core.book_table(table.table_id)
        assert table.is_booked, "Expected table to be available"
        core.unbook_table(table)
        assert table.is_booked is False, "Expected table to be available"
    # assert False, "Get a table (all tables), book it by ID, verify it is booked"


def test_cannot_book_a_nonexistant_table():
    with pytest.raises(core.EntityNotFoundError):
        core.book_table(None)
        # TODO: verify you cannot book a nonexistant table
        pass


def test_cannot_book_a_booked_table():
    tables = core.all_tables()
    assert tables, "All tables returned none"
    table = tables[-1]
    assert table.is_booked is False, "Expected table to be available"
    core.book_table(table.table_id)
    with pytest.raises(core.TableUnavailableError):
        core.book_table(table.table_id)
        # TODO: verify you cannot book a table that is already booked
        pass
    core.unbook_table(table)

