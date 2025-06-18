from fire_and_forget.observers import (
    SkuRepository,
    ImportLogRepository,
)
from fire_and_forget.import_result import ImportResult, SkuInput
from fire_and_forget.subject import Subject
import csv


class Client:
    def __init__(self):
        self.subject = Subject(
            [
                SkuRepository(),
                ImportLogRepository(),
            ]
        )

    def _validate(self, row):
        error_messages = []
        is_passed = True
        if row['sku_code'] == '':
            error_messages.append('sku code is required')
            is_passed = False
        try:
            int(row['price'], 10)
        except ValueError:
            error_messages.append('price must be number')
            is_passed = False
            
        return is_passed, error_messages

    def import_csv(self, path: str):
        with open(path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            # Observerを登録
            for row in reader:
                import_result = None
                is_passed, error_messages = self._validate(row)
                if is_passed:
                    import_result = ImportResult(
                        event_code=ImportResult.SKU_UPSERT,
                        error_messages=[],
                        sku=SkuInput(
                            name=row['name'],
                            sku_code=row['sku_code'],
                            jan_code=row['jan_code'],
                            price=int(row['price']),
                        ),
                    )
                else:
                    import_result = ImportResult(
                        event_code=ImportResult.VALIDATE_ERROR,
                        error_messages=error_messages,
                        sku=None,
                    )
                self.subject.notify(import_result)
        self.subject.worker_stop()

