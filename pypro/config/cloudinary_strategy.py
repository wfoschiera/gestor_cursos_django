import requests
from collectfast.strategies.base import CachingHashStrategy
from django.contrib.staticfiles.storage import ManifestFilesMixin


class ManifestHashMixin(ManifestFilesMixin):
    def get_local_file_hash(self, path, local_storage):
        try:
            return self.hashed_files[path]
        except KeyError:
            return super().get_local_file_hash(path, local_storage)


class CloudinaryStrategy(ManifestHashMixin, CachingHashStrategy):
    def get_remote_file_hash(self, prefixed_path):
        response = requests.head(self.remote_storage._get_url(prefixed_path))
        if not response.ok:
            return

        return self._extract_hash_from_etag(response.headers['ETAG'])

    def _extract_hash_from_etag(self, etag):
        return etag.split('"')[1]
