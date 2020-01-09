# Generated by Django 2.2.3 on 2020-01-09 23:01

import django.contrib.gis.db.models.fields
import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import opencivicdata.core.models.base
import re
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("core", "0006_merge_20200103_1432"),
        ("legislative", "0014_auto_20200109_2259"),
    ]

    operations = [
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, help_text="The date and time of creation."
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, help_text="The date and time of the last update."
                    ),
                ),
                (
                    "extras",
                    django.contrib.postgres.fields.jsonb.JSONField(
                        blank=True,
                        default=dict,
                        help_text="A key-value store for storing arbitrary information not covered elsewhere.",
                    ),
                ),
                (
                    "locked_fields",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.TextField(),
                        blank=True,
                        default=list,
                        size=None,
                    ),
                ),
                (
                    "id",
                    opencivicdata.core.models.base.OCDIDField(
                        ocd_type="event",
                        serialize=False,
                        validators=[
                            django.core.validators.RegexValidator(
                                flags=re.RegexFlag(32),
                                message="ID must match ^ocd-event/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$",
                                regex="^ocd-event/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$",
                            )
                        ],
                    ),
                ),
                ("name", models.CharField(max_length=1000)),
                ("description", models.TextField()),
                ("classification", models.CharField(max_length=100)),
                ("start_date", models.CharField(max_length=25)),
                ("end_date", models.CharField(blank=True, max_length=25)),
                ("all_day", models.BooleanField(default=False)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("cancelled", "Cancelled"),
                            ("tentative", "Tentative"),
                            ("confirmed", "Confirmed"),
                            ("passed", "Passed"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "jurisdiction",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="events",
                        to="core.Jurisdiction",
                    ),
                ),
            ],
            options={"db_table": "opencivicdata_event",},
        ),
        migrations.CreateModel(
            name="EventAgendaItem",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("description", models.TextField()),
                (
                    "classification",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.TextField(),
                        blank=True,
                        default=list,
                        size=None,
                    ),
                ),
                ("order", models.CharField(blank=True, max_length=100)),
                (
                    "subjects",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.TextField(),
                        blank=True,
                        default=list,
                        size=None,
                    ),
                ),
                (
                    "notes",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.TextField(),
                        blank=True,
                        default=list,
                        size=None,
                    ),
                ),
                (
                    "extras",
                    django.contrib.postgres.fields.jsonb.JSONField(
                        blank=True, default=dict
                    ),
                ),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="agenda",
                        to="events.Event",
                    ),
                ),
            ],
            options={"db_table": "opencivicdata_eventagendaitem",},
        ),
        migrations.CreateModel(
            name="EventAgendaMedia",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("note", models.CharField(max_length=300)),
                ("date", models.CharField(blank=True, max_length=25)),
                ("offset", models.PositiveIntegerField(null=True)),
                (
                    "agenda_item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="media",
                        to="events.EventAgendaItem",
                    ),
                ),
            ],
            options={"db_table": "opencivicdata_eventagendamedia",},
        ),
        migrations.CreateModel(
            name="EventDocument",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("note", models.CharField(max_length=300)),
                ("date", models.CharField(blank=True, max_length=25)),
                (
                    "classification",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("agenda", "Agenda"),
                            ("minutes", "Minutes"),
                            ("transcript", "Transcript"),
                            ("testimony", "Testimony"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="documents",
                        to="events.Event",
                    ),
                ),
            ],
            options={"db_table": "opencivicdata_eventdocument",},
        ),
        migrations.CreateModel(
            name="EventMedia",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("note", models.CharField(max_length=300)),
                ("date", models.CharField(blank=True, max_length=25)),
                ("offset", models.PositiveIntegerField(null=True)),
                (
                    "classification",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("audio recording", "Audio Recording"),
                            ("video recording", "Video Recording"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="media",
                        to="events.Event",
                    ),
                ),
            ],
            options={"db_table": "opencivicdata_eventmedia",},
        ),
        migrations.CreateModel(
            name="EventSource",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "note",
                    models.CharField(
                        blank=True,
                        help_text="A short, optional note related to an object.",
                        max_length=300,
                    ),
                ),
                (
                    "url",
                    models.URLField(
                        help_text="A hyperlink related to an object.", max_length=2000
                    ),
                ),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sources",
                        to="events.Event",
                    ),
                ),
            ],
            options={"db_table": "opencivicdata_eventsource",},
        ),
        migrations.CreateModel(
            name="EventRelatedEntity",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=2000)),
                ("entity_type", models.CharField(blank=True, max_length=20)),
                ("note", models.TextField()),
                (
                    "agenda_item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="related_entities",
                        to="events.EventAgendaItem",
                    ),
                ),
                (
                    "bill",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="legislative.Bill",
                    ),
                ),
                (
                    "organization",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="core.Organization",
                    ),
                ),
                (
                    "person",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="core.Person",
                    ),
                ),
                (
                    "vote_event",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="legislative.VoteEvent",
                    ),
                ),
            ],
            options={"db_table": "opencivicdata_eventrelatedentity",},
        ),
        migrations.CreateModel(
            name="EventParticipant",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=2000)),
                ("entity_type", models.CharField(blank=True, max_length=20)),
                ("note", models.TextField()),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="participants",
                        to="events.Event",
                    ),
                ),
                (
                    "organization",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="core.Organization",
                    ),
                ),
                (
                    "person",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="core.Person",
                    ),
                ),
            ],
            options={"db_table": "opencivicdata_eventparticipant",},
        ),
        migrations.CreateModel(
            name="EventMediaLink",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("media_type", models.CharField(max_length=100)),
                ("url", models.URLField(max_length=2000)),
                ("text", models.TextField(blank=True, default="")),
                (
                    "media",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="links",
                        to="events.EventMedia",
                    ),
                ),
            ],
            options={"db_table": "opencivicdata_eventmedialink",},
        ),
        migrations.CreateModel(
            name="EventLocation",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("url", models.URLField(blank=True, max_length=2000)),
                (
                    "coordinates",
                    django.contrib.gis.db.models.fields.PointField(
                        null=True, srid=4326
                    ),
                ),
                (
                    "jurisdiction",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="event_locations",
                        to="core.Jurisdiction",
                    ),
                ),
            ],
            options={"db_table": "opencivicdata_eventlocation",},
        ),
        migrations.CreateModel(
            name="EventLink",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "note",
                    models.CharField(
                        blank=True,
                        help_text="A short, optional note related to an object.",
                        max_length=300,
                    ),
                ),
                (
                    "url",
                    models.URLField(
                        help_text="A hyperlink related to an object.", max_length=2000
                    ),
                ),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="links",
                        to="events.Event",
                    ),
                ),
            ],
            options={"db_table": "opencivicdata_eventlink",},
        ),
        migrations.CreateModel(
            name="EventDocumentLink",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("media_type", models.CharField(max_length=100)),
                ("url", models.URLField(max_length=2000)),
                ("text", models.TextField(blank=True, default="")),
                (
                    "document",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="links",
                        to="events.EventDocument",
                    ),
                ),
            ],
            options={"db_table": "opencivicdata_eventdocumentlink",},
        ),
        migrations.CreateModel(
            name="EventAgendaMediaLink",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("media_type", models.CharField(max_length=100)),
                ("url", models.URLField(max_length=2000)),
                ("text", models.TextField(blank=True, default="")),
                (
                    "media",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="links",
                        to="events.EventAgendaMedia",
                    ),
                ),
            ],
            options={"db_table": "opencivicdata_eventagendamedialink",},
        ),
        migrations.AddField(
            model_name="event",
            name="location",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="events.EventLocation",
            ),
        ),
        migrations.AlterIndexTogether(
            name="event", index_together={("jurisdiction", "start_date", "name")},
        ),
    ]