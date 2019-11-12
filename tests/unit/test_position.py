from app.models.position import Position

def test_position():
    pos = Position(['a', 'b'])
    assert pos.position == ['a', 'b']
    assert type(pos.position) == list