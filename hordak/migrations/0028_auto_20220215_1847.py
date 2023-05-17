# Generated by Django 2.2.27 on 2022-02-15 18:47

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
import django.db.models.deletion
import django.utils.timezone
import django_smalluuid.models
import djmoney.models.fields
import mptt.fields
from django.db import migrations, models

import hordak.models.core


class Migration(migrations.Migration):
    dependencies = [
        ("hordak", "0027_trigger_update_full_account_codes_effective"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="account",
            options={"verbose_name": "account"},
        ),
        migrations.AlterModelOptions(
            name="leg",
            options={"verbose_name": "Leg"},
        ),
        migrations.AlterModelOptions(
            name="statementimport",
            options={"verbose_name": "statementImport"},
        ),
        migrations.AlterModelOptions(
            name="statementline",
            options={"verbose_name": "statementLine"},
        ),
        migrations.AlterModelOptions(
            name="transaction",
            options={"get_latest_by": "date", "verbose_name": "transaction"},
        ),
        migrations.AlterModelOptions(
            name="transactioncsvimportcolumn",
            options={
                "ordering": ["transaction_import", "column_number"],
                "verbose_name": "transactionCsvImportColumn",
            },
        ),
        migrations.AlterField(
            model_name="account",
            name="code",
            field=models.CharField(
                blank=True, max_length=3, null=True, verbose_name="code"
            ),
        ),
        migrations.AlterField(
            model_name="account",
            name="currencies",
            field=models.JSONField(
                verbose_name="currencies",
            ),
        ),
        migrations.AlterField(
            model_name="account",
            name="full_code",
            field=models.CharField(
                blank=True,
                db_index=True,
                max_length=100,
                null=True,
                unique=True,
                verbose_name="full_code",
            ),
        ),
        migrations.AlterField(
            model_name="account",
            name="is_bank_account",
            field=models.BooleanField(
                blank=True,
                default=False,
                help_text="Is this a bank account. This implies we can import bank statements into it and that it only supports a single currency",
                verbose_name="is bank account",
            ),
        ),
        migrations.AlterField(
            model_name="account",
            name="name",
            field=models.CharField(max_length=50, verbose_name="name"),
        ),
        migrations.AlterField(
            model_name="account",
            name="parent",
            field=mptt.fields.TreeForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="children",
                to="hordak.Account",
                verbose_name="parent",
            ),
        ),
        migrations.AlterField(
            model_name="account",
            name="type",
            field=models.CharField(
                blank=True,
                choices=[
                    ("AS", "Asset"),
                    ("LI", "Liability"),
                    ("IN", "Income"),
                    ("EX", "Expense"),
                    ("EQ", "Equity"),
                    ("TR", "Currency Trading"),
                ],
                max_length=2,
                verbose_name="type",
            ),
        ),
        migrations.AlterField(
            model_name="account",
            name="uuid",
            field=django_smalluuid.models.SmallUUIDField(
                default=django_smalluuid.models.UUIDDefault(),
                editable=False,
                unique=True,
                verbose_name="uuid",
            ),
        ),
        migrations.AlterField(
            model_name="leg",
            name="account",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="legs",
                to="hordak.Account",
                verbose_name="account",
            ),
        ),
        migrations.AlterField(
            model_name="leg",
            name="amount",
            field=djmoney.models.fields.MoneyField(
                decimal_places=2,
                default_currency="EUR",
                help_text="Record debits as positive, credits as negative",
                max_digits=13,
                verbose_name="amount",
            ),
        ),
        migrations.AlterField(
            model_name="leg",
            name="description",
            field=models.TextField(blank=True, default="", verbose_name="description"),
        ),
        migrations.AlterField(
            model_name="leg",
            name="transaction",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="legs",
                to="hordak.Transaction",
                verbose_name="transaction",
            ),
        ),
        migrations.AlterField(
            model_name="leg",
            name="uuid",
            field=django_smalluuid.models.SmallUUIDField(
                default=django_smalluuid.models.UUIDDefault(),
                editable=False,
                unique=True,
                verbose_name="uuid",
            ),
        ),
        migrations.AlterField(
            model_name="statementimport",
            name="bank_account",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="imports",
                to="hordak.Account",
                verbose_name="bank account",
            ),
        ),
        migrations.AlterField(
            model_name="statementimport",
            name="extra",
            field=django.contrib.postgres.fields.jsonb.JSONField(
                default=hordak.models.core.json_default,
                help_text="Any extra data relating to the import, probably specific to the data source.",
                verbose_name="extra",
            ),
        ),
        migrations.AlterField(
            model_name="statementimport",
            name="source",
            field=models.CharField(
                help_text='A value uniquely identifying where this data came from. Examples: "csv", "teller.io".',
                max_length=20,
                verbose_name="source",
            ),
        ),
        migrations.AlterField(
            model_name="statementimport",
            name="timestamp",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="timestamp"
            ),
        ),
        migrations.AlterField(
            model_name="statementimport",
            name="uuid",
            field=django_smalluuid.models.SmallUUIDField(
                default=django_smalluuid.models.UUIDDefault(),
                editable=False,
                unique=True,
                verbose_name="uuid",
            ),
        ),
        migrations.AlterField(
            model_name="statementline",
            name="amount",
            field=models.DecimalField(
                decimal_places=2, max_digits=13, verbose_name="amount"
            ),
        ),
        migrations.AlterField(
            model_name="statementline",
            name="date",
            field=models.DateField(verbose_name="date"),
        ),
        migrations.AlterField(
            model_name="statementline",
            name="description",
            field=models.TextField(blank=True, default="", verbose_name="description"),
        ),
        migrations.AlterField(
            model_name="statementline",
            name="source_data",
            field=django.contrib.postgres.fields.jsonb.JSONField(
                default=hordak.models.core.json_default,
                help_text="Original data received from the data source.",
                verbose_name="source data",
            ),
        ),
        migrations.AlterField(
            model_name="statementline",
            name="statement_import",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="lines",
                to="hordak.StatementImport",
                verbose_name="statement import",
            ),
        ),
        migrations.AlterField(
            model_name="statementline",
            name="timestamp",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="timestamp"
            ),
        ),
        migrations.AlterField(
            model_name="statementline",
            name="transaction",
            field=models.ForeignKey(
                blank=True,
                default=None,
                help_text="Reconcile this statement line to this transaction",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="hordak.Transaction",
                verbose_name="transaction",
            ),
        ),
        migrations.AlterField(
            model_name="statementline",
            name="type",
            field=models.CharField(default="", max_length=50, verbose_name="type"),
        ),
        migrations.AlterField(
            model_name="statementline",
            name="uuid",
            field=django_smalluuid.models.SmallUUIDField(
                default=django_smalluuid.models.UUIDDefault(),
                editable=False,
                unique=True,
                verbose_name="uuid",
            ),
        ),
        migrations.AlterField(
            model_name="transaction",
            name="date",
            field=models.DateField(
                default=django.utils.timezone.now,
                help_text="The date on which this transaction occurred",
                verbose_name="date",
            ),
        ),
        migrations.AlterField(
            model_name="transaction",
            name="description",
            field=models.TextField(blank=True, default="", verbose_name="description"),
        ),
        migrations.AlterField(
            model_name="transaction",
            name="timestamp",
            field=models.DateTimeField(
                default=django.utils.timezone.now,
                help_text="The creation date of this transaction object",
                verbose_name="timestamp",
            ),
        ),
        migrations.AlterField(
            model_name="transaction",
            name="uuid",
            field=django_smalluuid.models.SmallUUIDField(
                default=django_smalluuid.models.UUIDDefault(),
                editable=False,
                unique=True,
                verbose_name="uuid",
            ),
        ),
        migrations.AlterField(
            model_name="transactioncsvimport",
            name="date_format",
            field=models.CharField(
                choices=[
                    ("%d-%m-%Y", "dd-mm-yyyy"),
                    ("%d/%m/%Y", "dd/mm/yyyy"),
                    ("%d.%m.%Y", "dd.mm.yyyy"),
                    ("%d-%Y-%m", "dd-yyyy-mm"),
                    ("%d/%Y/%m", "dd/yyyy/mm"),
                    ("%d.%Y.%m", "dd.yyyy.mm"),
                    ("%m-%d-%Y", "mm-dd-yyyy"),
                    ("%m/%d/%Y", "mm/dd/yyyy"),
                    ("%m.%d.%Y", "mm.dd.yyyy"),
                    ("%m-%Y-%d", "mm-yyyy-dd"),
                    ("%m/%Y/%d", "mm/yyyy/dd"),
                    ("%m.%Y.%d", "mm.yyyy.dd"),
                    ("%Y-%d-%m", "yyyy-dd-mm"),
                    ("%Y/%d/%m", "yyyy/dd/mm"),
                    ("%Y.%d.%m", "yyyy.dd.mm"),
                    ("%Y-%m-%d", "yyyy-mm-dd"),
                    ("%Y/%m/%d", "yyyy/mm/dd"),
                    ("%Y.%m.%d", "yyyy.mm.dd"),
                    ("%d-%m-%y", "dd-mm-yy"),
                    ("%d/%m/%y", "dd/mm/yy"),
                    ("%d.%m.%y", "dd.mm.yy"),
                    ("%d-%y-%m", "dd-yy-mm"),
                    ("%d/%y/%m", "dd/yy/mm"),
                    ("%d.%y.%m", "dd.yy.mm"),
                    ("%m-%d-%y", "mm-dd-yy"),
                    ("%m/%d/%y", "mm/dd/yy"),
                    ("%m.%d.%y", "mm.dd.yy"),
                    ("%m-%y-%d", "mm-yy-dd"),
                    ("%m/%y/%d", "mm/yy/dd"),
                    ("%m.%y.%d", "mm.yy.dd"),
                    ("%y-%d-%m", "yy-dd-mm"),
                    ("%y/%d/%m", "yy/dd/mm"),
                    ("%y.%d.%m", "yy.dd.mm"),
                    ("%y-%m-%d", "yy-mm-dd"),
                    ("%y/%m/%d", "yy/mm/dd"),
                    ("%y.%m.%d", "yy.mm.dd"),
                ],
                default="%d-%m-%Y",
                max_length=50,
                verbose_name="date format",
            ),
        ),
        migrations.AlterField(
            model_name="transactioncsvimport",
            name="hordak_import",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="hordak.StatementImport",
                verbose_name="hordak import",
            ),
        ),
        migrations.AlterField(
            model_name="transactioncsvimport",
            name="state",
            field=models.CharField(
                choices=[
                    ("pending", "Pending"),
                    ("uploaded", "Uploaded, ready to import"),
                    ("done", "Import complete"),
                ],
                default="pending",
                max_length=20,
                verbose_name="state",
            ),
        ),
        migrations.AlterField(
            model_name="transactioncsvimport",
            name="timestamp",
            field=models.DateTimeField(
                default=django.utils.timezone.now,
                editable=False,
                verbose_name="timestamp",
            ),
        ),
        migrations.AlterField(
            model_name="transactioncsvimport",
            name="uuid",
            field=django_smalluuid.models.SmallUUIDField(
                default=django_smalluuid.models.UUIDDefault(),
                editable=False,
                unique=True,
                verbose_name="uuid",
            ),
        ),
        migrations.AlterField(
            model_name="transactioncsvimportcolumn",
            name="column_number",
            field=models.PositiveSmallIntegerField(verbose_name="column number"),
        ),
        migrations.AlterField(
            model_name="transactioncsvimportcolumn",
            name="example",
            field=models.CharField(
                blank=True, default="", max_length=200, verbose_name="example"
            ),
        ),
        migrations.AlterField(
            model_name="transactioncsvimportcolumn",
            name="transaction_import",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="columns",
                to="hordak.TransactionCsvImport",
                verbose_name="transaction import",
            ),
        ),
    ]
