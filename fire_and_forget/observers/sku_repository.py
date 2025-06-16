from fire_and_forget.import_result import ImportResult, SkuInput


class SkuRepository:
    def commit(import_result: ImportResult):
        if import_result.event_code == ImportResult.SKU_UPSERT:
            self._upsert_sku(import_result.sku)


    def _upsert_sku(sku: SkuInput):
        # upsert and commit a sku
        print('upsert and commit a sku')
        pass

