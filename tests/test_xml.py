from bs4 import BeautifulSoup

from edgar.xml import child_value, child_text, value_or_footnote


def test_child_value():
    soup = BeautifulSoup(
        """
        <root>
            <child>
            <value>Music</value>
            </child>
        </root>   
        """, features="xml"
    )
    root = soup.find("root")
    assert child_value(root, "child") == "Music"
    assert child_text(root, "child").strip() == "Music"


def test_value_or_footnote():
    soup = BeautifulSoup(
        """
        <root>
            <child>
            <footnote id="F1"/>
            </child>
        </root>   
        """, features="xml"
    )
    root = soup.find("root")
    child = root.find("child")
    assert value_or_footnote(child) == "F1"



