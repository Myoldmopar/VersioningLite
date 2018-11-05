class Version:
    def __init__(self, major, minor=None, patch=None, build=None):
        self.major = major
        if minor is not None:
            self.minor = minor
            self.minor_set = True
        else:
            self.minor = 0
            self.minor_set = False
        if patch is not None:
            self.patch = patch
            self.patch_set = True
        else:
            self.patch = 0
            self.patch_set = False
        if build is not None:
            self.build = build
            self.build_set = True
        else:
            self.build = 0
            self.build_set = False

    def __lt__(self, other_version):
        if other_version.major > self.major:
            return True
        if other_version.minor > self.minor:
            return True
        if other_version.patch > self.patch:
            return True
        if other_version.build > self.build:
            return True
        return False

    def __ge__(self, other_version):
        if other_version.major < self.major:
            return True
        if other_version.minor < self.minor:
            return True
        if other_version.patch < self.patch:
            return True
        if other_version.build < self.build:
            return True
        if other_version.major == self.major and other_version.minor == self.minor and other_version.patch == self.patch and other_version.build == self.build:
            return True
        return False

    def __gt__(self, other_version):
        if other_version.major < self.major:
            return True
        if other_version.minor < self.minor:
            return True
        if other_version.patch < self.patch:
            return True
        if other_version.build < self.build:
            return True
        return False

    def __le__(self, other_version):
        if other_version.major > self.major:
            return True
        if other_version.minor > self.minor:
            return True
        if other_version.patch > self.patch:
            return True
        if other_version.build > self.build:
            return True
        if other_version.major == self.major and other_version.minor == self.minor and other_version.patch == self.patch and other_version.build == self.build:
            return True
        return False

    def __eq__(self, other_version):
        if other_version.major == self.major and other_version.minor == self.minor and other_version.patch == self.patch and other_version.build == self.build:
            return True
        return False

    def __ne__(self, other_version):
        if other_version.major == self.major and other_version.minor == self.minor and other_version.patch == self.patch and other_version.build == self.build:
            return False
        return True

    def __str__(self):
        out_string = str(self.major)
        if self.minor_set:
            out_string += '.' + str(self.minor)
        if self.patch_set:
            out_string += '.' + str(self.patch)
        if self.build_set:
            out_string += '.' + str(self.build)
        return out_string
