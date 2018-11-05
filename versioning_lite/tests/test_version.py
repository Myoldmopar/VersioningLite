import unittest

from versioning_lite.version import Version


class TestVersionGreaterThan(unittest.TestCase):

    def test_major_difference(self):
        v1 = Version(major=1)
        v2 = Version(major=2)
        self.assertTrue(v2 > v1)
        self.assertFalse(v1 > v2)
        self.assertFalse(v2 > v2)
        self.assertFalse(v1 > v1)

    def test_minor_difference(self):
        v1 = Version(major=1, minor=1)
        v2 = Version(major=1, minor=2)
        self.assertTrue(v2 > v1)
        self.assertFalse(v1 > v2)
        self.assertFalse(v2 > v2)
        self.assertFalse(v1 > v1)

    def test_patch_difference(self):
        v1 = Version(major=1, minor=1, patch=1)
        v2 = Version(major=1, minor=1, patch=2)
        self.assertTrue(v2 > v1)
        self.assertFalse(v1 > v2)
        self.assertFalse(v2 > v2)
        self.assertFalse(v1 > v1)

    def test_build_difference(self):
        v1 = Version(major=1, minor=1, patch=1, build=1)
        v2 = Version(major=1, minor=1, patch=1, build=2)
        self.assertTrue(v2 > v1)
        self.assertFalse(v1 > v2)
        self.assertFalse(v2 > v2)
        self.assertFalse(v1 > v1)


class TestVersionLessThan(unittest.TestCase):

    def test_major_difference(self):
        v1 = Version(major=1)
        v2 = Version(major=2)
        self.assertTrue(v1 < v2)
        self.assertFalse(v2 < v1)
        self.assertFalse(v2 < v2)
        self.assertFalse(v1 < v1)

    def test_minor_difference(self):
        v1 = Version(major=1, minor=1)
        v2 = Version(major=1, minor=2)
        self.assertTrue(v1 < v2)
        self.assertFalse(v2 < v1)
        self.assertFalse(v2 < v2)
        self.assertFalse(v1 < v1)

    def test_patch_difference(self):
        v1 = Version(major=1, minor=1, patch=1)
        v2 = Version(major=1, minor=1, patch=2)
        self.assertTrue(v1 < v2)
        self.assertFalse(v2 < v1)
        self.assertFalse(v2 < v2)
        self.assertFalse(v1 < v1)

    def test_build_difference(self):
        v1 = Version(major=1, minor=1, patch=1, build=1)
        v2 = Version(major=1, minor=1, patch=1, build=2)
        self.assertTrue(v1 < v2)
        self.assertFalse(v2 < v1)
        self.assertFalse(v2 < v2)
        self.assertFalse(v1 < v1)


class TestVersionLessThanOrEqual(unittest.TestCase):

    def test_major_difference(self):
        v1 = Version(major=1)
        v2 = Version(major=2)
        self.assertTrue(v1 <= v2)
        self.assertFalse(v2 <= v1)
        self.assertTrue(v2 <= v2)
        self.assertTrue(v1 <= v1)

    def test_minor_difference(self):
        v1 = Version(major=1, minor=1)
        v2 = Version(major=1, minor=2)
        self.assertTrue(v1 <= v2)
        self.assertFalse(v2 <= v1)
        self.assertTrue(v2 <= v2)
        self.assertTrue(v1 <= v1)

    def test_patch_difference(self):
        v1 = Version(major=1, minor=1, patch=1)
        v2 = Version(major=1, minor=1, patch=2)
        self.assertTrue(v1 <= v2)
        self.assertFalse(v2 <= v1)
        self.assertTrue(v2 <= v2)
        self.assertTrue(v1 <= v1)

    def test_build_difference(self):
        v1 = Version(major=1, minor=1, patch=1, build=1)
        v2 = Version(major=1, minor=1, patch=1, build=2)
        self.assertTrue(v1 <= v2)
        self.assertFalse(v2 <= v1)
        self.assertTrue(v2 <= v2)
        self.assertTrue(v1 <= v1)

    def test_build_equal(self):
        v1 = Version(major=1, minor=1, patch=1, build=1)
        v2 = Version(major=1, minor=1, patch=1, build=1)
        self.assertTrue(v1 <= v2)
        self.assertTrue(v2 <= v1)
        self.assertTrue(v2 <= v2)
        self.assertTrue(v1 <= v1)


class TestVersionGreaterThanOrEqual(unittest.TestCase):

    def test_major_difference(self):
        v1 = Version(major=1)
        v2 = Version(major=2)
        self.assertFalse(v1 >= v2)
        self.assertTrue(v2 >= v1)
        self.assertTrue(v2 >= v2)
        self.assertTrue(v1 >= v1)

    def test_minor_difference(self):
        v1 = Version(major=1, minor=1)
        v2 = Version(major=1, minor=2)
        self.assertFalse(v1 >= v2)
        self.assertTrue(v2 >= v1)
        self.assertTrue(v2 >= v2)
        self.assertTrue(v1 >= v1)

    def test_patch_difference(self):
        v1 = Version(major=1, minor=1, patch=1)
        v2 = Version(major=1, minor=1, patch=2)
        self.assertFalse(v1 >= v2)
        self.assertTrue(v2 >= v1)
        self.assertTrue(v2 >= v2)
        self.assertTrue(v1 >= v1)

    def test_build_difference(self):
        v1 = Version(major=1, minor=1, patch=1, build=1)
        v2 = Version(major=1, minor=1, patch=1, build=2)
        self.assertFalse(v1 >= v2)
        self.assertTrue(v2 >= v1)
        self.assertTrue(v2 >= v2)
        self.assertTrue(v1 >= v1)

    def test_build_equal(self):
        v1 = Version(major=1, minor=1, patch=1, build=1)
        v2 = Version(major=1, minor=1, patch=1, build=1)
        self.assertTrue(v1 >= v2)
        self.assertTrue(v2 >= v1)
        self.assertTrue(v2 >= v2)
        self.assertTrue(v1 >= v1)


class TestVersionEquals(unittest.TestCase):

    def test_major_difference(self):
        v1 = Version(major=1)
        v2 = Version(major=2)
        v3 = Version(major=1)
        self.assertFalse(v1 == v2)
        self.assertFalse(v2 == v3)
        self.assertTrue(v1 == v3)

    def test_minor_difference(self):
        v1 = Version(major=1, minor=1)
        v2 = Version(major=1, minor=2)
        v3 = Version(major=1, minor=1)
        self.assertFalse(v1 == v2)
        self.assertFalse(v2 == v3)
        self.assertTrue(v1 == v3)

    def test_patch_difference(self):
        v1 = Version(major=1, minor=1, patch=1)
        v2 = Version(major=1, minor=1, patch=2)
        v3 = Version(major=1, minor=1, patch=1)
        self.assertFalse(v1 == v2)
        self.assertFalse(v2 == v3)
        self.assertTrue(v1 == v3)

    def test_build_difference(self):
        v1 = Version(major=1, minor=1, patch=1, build=1)
        v2 = Version(major=1, minor=1, patch=1, build=2)
        v3 = Version(major=1, minor=1, patch=1, build=1)
        self.assertFalse(v1 == v2)
        self.assertFalse(v2 == v3)
        self.assertTrue(v1 == v3)


class TestVersionNotEquals(unittest.TestCase):

    def test_major_difference(self):
        v1 = Version(major=1)
        v2 = Version(major=2)
        v3 = Version(major=1)
        self.assertTrue(v1 != v2)
        self.assertTrue(v2 != v3)
        self.assertFalse(v1 != v3)

    def test_minor_difference(self):
        v1 = Version(major=1, minor=1)
        v2 = Version(major=1, minor=2)
        v3 = Version(major=1, minor=1)
        self.assertTrue(v1 != v2)
        self.assertTrue(v2 != v3)
        self.assertFalse(v1 != v3)

    def test_patch_difference(self):
        v1 = Version(major=1, minor=1, patch=1)
        v2 = Version(major=1, minor=1, patch=2)
        v3 = Version(major=1, minor=1, patch=1)
        self.assertTrue(v1 != v2)
        self.assertTrue(v2 != v3)
        self.assertFalse(v1 != v3)

    def test_build_difference(self):
        v1 = Version(major=1, minor=1, patch=1, build=1)
        v2 = Version(major=1, minor=1, patch=1, build=2)
        v3 = Version(major=1, minor=1, patch=1, build=1)
        self.assertTrue(v1 != v2)
        self.assertTrue(v2 != v3)
        self.assertFalse(v1 != v3)


class TestVersionString(unittest.TestCase):

    def test_major_difference(self):
        v1 = Version(major=1)
        self.assertEqual('1', str(v1))

    def test_minor_difference(self):
        v1 = Version(major=1, minor=1)
        self.assertEqual('1.1', str(v1))

    def test_patch_difference(self):
        v1 = Version(major=1, minor=1, patch=1)
        self.assertEqual('1.1.1', str(v1))

    def test_build_difference(self):
        v1 = Version(major=1, minor=1, patch=1, build=1)
        self.assertEqual('1.1.1.1', str(v1))
