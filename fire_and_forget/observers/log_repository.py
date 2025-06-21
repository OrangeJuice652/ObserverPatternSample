from fire_and_forget.import_result import ImportResult, SkuInput
from fire_and_forget.observers import IObserver
from typing import List


class ImportLogRepository(IObserver):

    def commit(self, import_result: ImportResult):
        if import_result.event_code == ImportResult.SKU_UPSERT:
            self._write_sku_upsert_log(import_result.sku)
        elif import_result.event_code == ImportResult.VALIDATE_ERROR:
            self._write_validate_error_log(import_result.error_messages)

    def _write_sku_upsert_log(self, sku_input: SkuInput):
        # Write a log for upserting the SKU here
        print(f'the SKU saved (sku_code: {sku_input.sku_code})')
        
    def _write_validate_error_log(self, error_messages: List[str]):
        # Write a validate error log here
        print(f'validate error! (error_messages: {"\t".join(error_messages)})')

