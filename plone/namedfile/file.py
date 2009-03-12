from zope.interface import implements

from zope.app.file.file import File
from zope.app.file.image import Image

from z3c.blobfile.file import File as BlobFile
from z3c.blobfile.image import Image as BlobImage

from plone.namedfile.interfaces import INamedFile, INamedImage
from plone.namedfile.interfaces import INamedBlobFile, INamedBlobImage
from plone.namedfile.utils import get_contenttype

class NamedFile(File):
    """A non-BLOB file that stores a filename
    """
    implements(INamedFile)

    def __init__(self, data='', contentType='', filename=None):
        if filename is not None and contentType in ('', 'application/octet-stream'):
            contentType = get_contenttype(filename=filename)
        super(NamedFile, self).__init__(data, contentType)
        self.filename = filename

class NamedImage(Image):
    """An non-BLOB image with a filename
    """
    implements(INamedImage)

    def __init__(self, data='', contentType='', filename=None):
        # Note: we're keeping contentType to have a uniform constructor
        super(NamedImage, self).__init__(data)
        self.filename = filename

class NamedBlobFile(BlobFile):
    """A file stored in a ZODB BLOB, file a filename
    """
    implements(INamedBlobFile)

    def __init__(self, data='', contentType='', filename=None):
        if filename is not None and contentType in ('', 'application/octet-stream'):
            contentType = get_contenttype(filename=filename)
        super(NamedBlobFile, self).__init__(data, contentType)
        self.filename = filename

class NamedBlobImage(BlobImage):
    """An image stored in a ZODB BLOB with a filename
    """
    implements(INamedBlobImage)

    def __init__(self, data='', contentType='', filename=None):
        # Note: we're keeping contentType to have a uniform constructor
        super(NamedBlobImage, self).__init__(data)
        self.filename = filename