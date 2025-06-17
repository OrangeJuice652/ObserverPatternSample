from fire_and_forget.import_result import ImportResult, SkuInput
from fire_and_forget.observers import IObserver


class SkuRepository(IObserver):
    def commit(self, import_result: ImportResult):
        if import_result.event_code == ImportResult.SKU_UPSERT:
            self._upsert_sku(import_result.sku)


    def _upsert_sku(self, sku: SkuInput):
        # Write a something that upsert and commit the SKU here
        print(f'upsert and commit a sku(sku_code: {sku.sku_code})')


