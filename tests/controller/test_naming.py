from controller.naming import msg_port_from_name


def test_port_names_full_words():
    assert msg_port_from_name("Angular Velocity") == 7006
    assert msg_port_from_name("Self Diagnostic") == 412


def test_port_names_abbreviations():
    assert msg_port_from_name("AV") == 7006
    assert msg_port_from_name("SD") == 412
