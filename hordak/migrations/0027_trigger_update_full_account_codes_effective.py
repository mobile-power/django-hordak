# Generated by Django 2.0.8 on 2018-08-27 09:48

from django.db import migrations

def create_trigger(apps, schema_editor):
    if schema_editor.connection.vendor == 'postgresql':
        schema_editor.execute("""
            CREATE OR REPLACE FUNCTION update_full_account_codes()
                RETURNS TRIGGER AS
            $$
            BEGIN
                -- Set empty string codes to be NULL
                UPDATE hordak_account SET code = NULL where code = '';

                -- Set full code to the combination of the parent account's codes
                UPDATE
                    hordak_account AS a
                SET
                    full_code = (
                        SELECT string_agg(code, '' order by lft)
                        FROM hordak_account AS a2
                        WHERE a2.lft <= a.lft AND a2.rght >= a.rght AND a.tree_id = a2.tree_id AND code IS NOT NULL
                    )
                    WHERE tree_id IN (SELECT DISTINCT tree_id FROM hordak_account WHERE code IS NOT NULL);  -- search only account trees without null codes


                -- Set full codes to NULL where a parent account includes a NULL code
                UPDATE
                    hordak_account AS a
                SET
                    full_code = NULL
                WHERE
                    (
                        SELECT COUNT(*)
                        FROM hordak_account AS a2
                        WHERE a2.lft <= a.lft AND a2.rght >= a.rght AND a.tree_id = a2.tree_id AND a2.code IS NULL
                    ) > 0
                    AND full_code IS NOT NULL;  -- search only account trees without null codes
                RETURN NULL;
            END;
            $$
            LANGUAGE plpgsql;
        """)

    elif schema_editor.connection.vendor == 'mysql':
        schema_editor.execute("""
            CREATE PROCEDURE update_full_account_codes()
            BEGIN
                -- Set empty string codes to be NULL
                UPDATE hordak_account SET code = NULL where code = '';
                
                UPDATE
                    hordak_account AS a
                SET
                    full_code = (
                        SELECT GROUP_CONCAT(code ORDER BY lft SEPARATOR '')
                        FROM hordak_account AS a2
                        WHERE a2.lft <= a.lft AND a2.rght >= a.rght AND a.tree_id = a2.tree_id AND code IS NOT NULL
                    )
                WHERE tree_id IN (SELECT DISTINCT tree_id FROM hordak_account WHERE code IS NOT NULL);  -- search only account trees without null codes


                -- Set full codes to NULL where a parent account includes a NULL code
                UPDATE
                    hordak_account AS a
                SET
                    full_code = NULL
                WHERE
                    (
                        SELECT COUNT(*)
                        FROM hordak_account AS a2
                        WHERE a2.lft <= a.lft AND a2.rght >= a.rght AND a.tree_id = a2.tree_id AND a2.code IS NULL
                    ) > 0
                    AND full_code IS NOT NULL;  -- search only account trees without null codes
            END
        """)

    else:
        raise NotImplementedError("Don't know how to create trigger for %s" % schema_editor.connection.vendor)


def drop_trigger(apps, schema_editor):
    if schema_editor.connection.vendor == 'postgresql':
        schema_editor.execute("DROP FUNCTION update_full_account_codes()")
    elif schema_editor.connection.vendor == 'mysql':
        # the triggers will have to be called within django again...
        schema_editor.execute("DROP PROCEDURE update_full_account_codes")
    else:
        raise NotImplementedError("Don't know how to drop trigger for %s" % schema_editor.connection.vendor)


class Migration(migrations.Migration):
    dependencies = [("hordak", "0026_auto_20190723_0929")]
    atomic = False

    operations = [
        migrations.RunPython(create_trigger, reverse_code=drop_trigger),
    ]
