import graphene

from ....product import models
from ...core.mutations import ModelBulkDeleteMutation, ModelBulkPublishMutation


class CategoryBulkDelete(ModelBulkDeleteMutation):
    class Arguments:
        ids = graphene.List(
            graphene.ID,
            required=True,
            description='List of category IDs to delete.')

    class Meta:
        description = 'Deletes categories.'
        model = models.Category

    @classmethod
    def user_is_allowed(cls, user, input):
        return user.has_perm('product.manage_products')


class CollectionBulkDelete(ModelBulkDeleteMutation):
    class Arguments:
        ids = graphene.List(
            graphene.ID,
            required=True,
            description='List of collection IDs to delete.')

    class Meta:
        description = 'Deletes collections.'
        model = models.Collection

    @classmethod
    def user_is_allowed(cls, user, input):
        return user.has_perm('product.manage_products')


class CollectionBulkPublish(ModelBulkPublishMutation):
    class Arguments:
        ids = graphene.List(
            graphene.ID,
            required=True,
            description='List of collections IDs to publish.')

    class Meta:
        description = 'Publish collections.'
        model = models.Collection

    @classmethod
    def user_is_allowed(cls, user, input):
        return user.has_perm('product.manage_products')


class CollectionBulkUnpublish(CollectionBulkPublish):
    class Arguments:
        ids = graphene.List(
            graphene.ID,
            required=True,
            description='List of collections IDs to unpublish.')

    class Meta:
        description = 'Unpublish collections.'
        model = models.Collection

    @classmethod
    def bulk_action(cls, queryset):
        queryset.update(is_published=False)


class ProductBulkDelete(ModelBulkDeleteMutation):
    class Arguments:
        ids = graphene.List(
            graphene.ID,
            required=True,
            description='List of product IDs to delete.')

    class Meta:
        description = 'Deletes products.'
        model = models.Product

    @classmethod
    def user_is_allowed(cls, user, input):
        return user.has_perm('product.manage_products')


class ProductVariantBulkDelete(ModelBulkDeleteMutation):
    class Arguments:
        ids = graphene.List(
            graphene.ID,
            required=True,
            description='List of product variant IDs to delete.')

    class Meta:
        description = 'Deletes product variants.'
        model = models.ProductVariant

    @classmethod
    def user_is_allowed(cls, user, input):
        return user.has_perm('product.manage_products')


class ProductTypeBulkDelete(ModelBulkDeleteMutation):
    class Arguments:
        ids = graphene.List(
            graphene.ID,
            required=True,
            description='List of product type IDs to delete.')

    class Meta:
        description = 'Deletes product types.'
        model = models.ProductType

    @classmethod
    def user_is_allowed(cls, user, input):
        return user.has_perm('product.manage_products')


class ProductImageBulkDelete(ModelBulkDeleteMutation):
    class Arguments:
        ids = graphene.List(
            graphene.ID,
            required=True,
            description='List of product image IDs to delete.')

    class Meta:
        description = 'Deletes product images.'
        model = models.ProductImage

    @classmethod
    def user_is_allowed(cls, user, input):
        return user.has_perm('product.manage_products')