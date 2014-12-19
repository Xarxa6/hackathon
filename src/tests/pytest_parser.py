import parser

#helpers
def all_in(a,b):
    assert(all([ item in a for item in b ]))
    assert(all([ item in b for item in a ]))

class PytestParser:

    def pytest_1(self):
        parsed = parser.parse_request("registrations monthly")
        expected = [{"measure":"registrations"},{"dimension":"monthly"}]
        all_in(parsed,expected)

    def pytest_2(self):
        parsed = parser.parse_request("users last month")
        expected = [{"measure":"users"}, {"dimension":"last"}, {"dimension":"months"}]
        all_in(parsed,expected)

    def pytest_3(self):
        parsed = parser.parse_request("tugo")
        expected = [{"dimension":"tugo"}]
        all_in(parsed,expected)




