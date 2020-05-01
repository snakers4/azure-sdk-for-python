# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import ApiOperation
    from ._models_py3 import ApiOperationDisplay
    from ._models_py3 import Cache
    from ._models_py3 import CacheEncryptionSettings
    from ._models_py3 import CacheHealth
    from ._models_py3 import CacheIdentity
    from ._models_py3 import CacheNetworkSettings
    from ._models_py3 import CacheSecuritySettings
    from ._models_py3 import CacheSku
    from ._models_py3 import CacheUpgradeStatus
    from ._models_py3 import ClfsTarget
    from ._models_py3 import ClfsTargetProperties
    from ._models_py3 import CloudErrorBody
    from ._models_py3 import KeyVaultKeyReference
    from ._models_py3 import KeyVaultKeyReferenceSourceVault
    from ._models_py3 import NamespaceJunction
    from ._models_py3 import Nfs3Target
    from ._models_py3 import Nfs3TargetProperties
    from ._models_py3 import ResourceSku
    from ._models_py3 import ResourceSkuCapabilities
    from ._models_py3 import ResourceSkuLocationInfo
    from ._models_py3 import Restriction
    from ._models_py3 import StorageTarget
    from ._models_py3 import StorageTargetProperties
    from ._models_py3 import StorageTargetResource
    from ._models_py3 import UnknownTarget
    from ._models_py3 import UnknownTargetProperties
    from ._models_py3 import UsageModel
    from ._models_py3 import UsageModelDisplay
except (SyntaxError, ImportError):
    from ._models import ApiOperation
    from ._models import ApiOperationDisplay
    from ._models import Cache
    from ._models import CacheEncryptionSettings
    from ._models import CacheHealth
    from ._models import CacheIdentity
    from ._models import CacheNetworkSettings
    from ._models import CacheSecuritySettings
    from ._models import CacheSku
    from ._models import CacheUpgradeStatus
    from ._models import ClfsTarget
    from ._models import ClfsTargetProperties
    from ._models import CloudErrorBody
    from ._models import KeyVaultKeyReference
    from ._models import KeyVaultKeyReferenceSourceVault
    from ._models import NamespaceJunction
    from ._models import Nfs3Target
    from ._models import Nfs3TargetProperties
    from ._models import ResourceSku
    from ._models import ResourceSkuCapabilities
    from ._models import ResourceSkuLocationInfo
    from ._models import Restriction
    from ._models import StorageTarget
    from ._models import StorageTargetProperties
    from ._models import StorageTargetResource
    from ._models import UnknownTarget
    from ._models import UnknownTargetProperties
    from ._models import UsageModel
    from ._models import UsageModelDisplay
from ._paged_models import ApiOperationPaged
from ._paged_models import CachePaged
from ._paged_models import ResourceSkuPaged
from ._paged_models import StorageTargetPaged
from ._paged_models import UsageModelPaged
from ._storage_cache_management_client_enums import (
    CacheIdentityType,
    HealthStateType,
    ProvisioningStateType,
    FirmwareStatusType,
    StorageTargetType,
    ReasonCode,
)

__all__ = [
    'ApiOperation',
    'ApiOperationDisplay',
    'Cache',
    'CacheEncryptionSettings',
    'CacheHealth',
    'CacheIdentity',
    'CacheNetworkSettings',
    'CacheSecuritySettings',
    'CacheSku',
    'CacheUpgradeStatus',
    'ClfsTarget',
    'ClfsTargetProperties',
    'CloudErrorBody',
    'KeyVaultKeyReference',
    'KeyVaultKeyReferenceSourceVault',
    'NamespaceJunction',
    'Nfs3Target',
    'Nfs3TargetProperties',
    'ResourceSku',
    'ResourceSkuCapabilities',
    'ResourceSkuLocationInfo',
    'Restriction',
    'StorageTarget',
    'StorageTargetProperties',
    'StorageTargetResource',
    'UnknownTarget',
    'UnknownTargetProperties',
    'UsageModel',
    'UsageModelDisplay',
    'ApiOperationPaged',
    'ResourceSkuPaged',
    'UsageModelPaged',
    'CachePaged',
    'StorageTargetPaged',
    'CacheIdentityType',
    'HealthStateType',
    'ProvisioningStateType',
    'FirmwareStatusType',
    'StorageTargetType',
    'ReasonCode',
]
