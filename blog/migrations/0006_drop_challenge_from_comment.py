# blog/migrations/0006_drop_challenge_from_comment.py
from django.db import migrations

def forwards(apps, schema_editor):
    """
    Ta bort kolumnen 'challenge' från 'blog_comment' om den finns.
    Gör inget om den saknas.
    """
    vendor = schema_editor.connection.vendor

    if vendor == 'postgresql':
        schema_editor.execute("ALTER TABLE blog_comment DROP COLUMN IF EXISTS challenge;")
    else:
        # SQLite + andra DBs: kolla kolumner först
        try:
            cursor = schema_editor.connection.cursor()
            cursor.execute("PRAGMA table_info('blog_comment');")
            cols = [row[1] for row in cursor.fetchall()]
            if 'challenge' in cols:
                try:
                    schema_editor.execute("ALTER TABLE blog_comment DROP COLUMN challenge;")
                except Exception:
                    # Äldre SQLite saknar DROP COLUMN – skippa tyst
                    pass
        except Exception:
            pass

def backwards(apps, schema_editor):
    """
    Lägg tillbaka kolumnen 'challenge' om den saknas.
    """
    vendor = schema_editor.connection.vendor

    if vendor == 'postgresql':
        schema_editor.execute("ALTER TABLE blog_comment ADD COLUMN IF NOT EXISTS challenge varchar NULL;")
    else:
        try:
            cursor = schema_editor.connection.cursor()
            cursor.execute("PRAGMA table_info('blog_comment');")
            cols = [row[1] for row in cursor.fetchall()]
            if 'challenge' not in cols:
                try:
                    schema_editor.execute("ALTER TABLE blog_comment ADD COLUMN challenge varchar NULL;")
                except Exception:
                    pass
        except Exception:
            pass

class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0005_alter_comment_options_alter_post_options'),
    ]
    operations = [
        migrations.RunPython(forwards, backwards),
    ]
