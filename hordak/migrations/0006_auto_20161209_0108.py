# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-09 01:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hordak', '0005_account_currencies'),
    ]

    operations = [
        migrations.RunSQL(
            """
                CREATE OR REPLACE FUNCTION check_leg()
                    RETURNS trigger AS
                $$
                DECLARE
                    tx_id INT;
                    non_zero RECORD;
                BEGIN
                    IF (TG_OP = 'DELETE') THEN
                        tx_id := OLD.transaction_id;
                    ELSE
                        tx_id := NEW.transaction_id;
                    END IF;


                    SELECT ABS(SUM(amount)) AS total, amount_currency AS currency
                        INTO non_zero
                        FROM hordak_leg
                        WHERE transaction_id = tx_id
                        GROUP BY amount_currency
                        HAVING ABS(SUM(amount)) > 0
                        LIMIT 1;

                    IF FOUND THEN
                        RAISE EXCEPTION 'Sum of transaction amounts in each currency must be 0. Currency % has non-zero total %',
                            non_zero.currency, non_zero.total;
                    END IF;

                    RETURN NEW;
                END;
                $$
                LANGUAGE plpgsql;
            """
        ),
    ]