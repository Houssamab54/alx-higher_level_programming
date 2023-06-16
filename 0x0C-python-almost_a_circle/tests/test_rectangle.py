import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_init(self):
        r = Rectangle(10, 20)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertIsNotNone(r.id)

    def test_area(self):
        r = Rectangle(10, 20)
        self.assertEqual(r.area(), 200)

    def test_display(self):
        r = Rectangle(4, 3)
        self.assertEqual(r.display(), print("####\n####\n####\n"))

    def test_str(self):
        r = Rectangle(10, 20)
        self.assertEqual(str(r), "[Rectangle] ({}) 0/0 - 10/20".format(r.id))

    def test_update(self):
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(2)
        self.assertEqual(str(r), "[Rectangle] (2) 10/10 - 10/10")
        r.update(3, 20)
        self.assertEqual(str(r), "[Rectangle] (3) 10/10 - 20/10")
        r.update(4, 30, 40)
        self.assertEqual(str(r), "[Rectangle] (4) 10/10 - 30/40")
        r.update(5, 50, 60, 70)
        self.assertEqual(str(r), "[Rectangle] (5) 70/10 - 50/60")
        r.update(6, 70, 80, 90, 100)
        self.assertEqual(str(r), "[Rectangle] (6) 90/100 - 70/80")
        r.update(id=7)
        self.assertEqual(str(r), "[Rectangle] (7) 90/100 - 70/80")
        r.update(id=8, width=80)
        self.assertEqual(str(r), "[Rectangle] (8) 90/100 - 80/80")
        r.update(id=9, width=90, height=100)
        self.assertEqual(str(r), "[Rectangle] (9) 90/100 - 90/100")
        r.update(id=10, width=100, height=110, x=120)
        self.assertEqual(str(r), "[Rectangle] (10) 120/100 - 100/110")
        r.update(id=11, width=110, height=120, x=130, y=140)
        self.assertEqual(str(r), "[Rectangle] (11) 130/140 - 110/120")
        r.update()
        self.assertEqual(str(r), "[Rectangle] (11) 130/140 - 110/120")

if __name__ == '__main__':
    unittest.main()
