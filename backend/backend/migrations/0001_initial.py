# Generated by Django 5.1.2 on 2024-12-10 15:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('LB_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('LB_tag_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=20)),
                ('user_email', models.CharField(max_length=30)),
                ('user_password', models.CharField(max_length=20)),
                ('user_student_id', models.BigIntegerField()),
                ('user_experience', models.BigIntegerField()),
                ('user_sign_date', models.DateField()),
                ('user_birthday', models.DateField()),
                ('user_uploaded', models.IntegerField()),
                ('user_role', models.IntegerField()),
                ('user_post_cnt', models.IntegerField()),
                ('user_info_cnt', models.IntegerField()),
                ('user_introduction', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('post_title', models.CharField(max_length=100)),
                ('post_content', models.TextField()),
                ('post_label', models.CharField(max_length=30)),
                ('post_heat', models.IntegerField()),
                ('post_time', models.DateTimeField()),
                ('post_isTop', models.BooleanField()),
                ('post_tag_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.label')),
                ('post_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.user')),
            ],
        ),
        migrations.CreateModel(
            name='FirstLayerComment',
            fields=[
                ('FLC_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('FLC_content', models.TextField()),
                ('FLC_time', models.DateTimeField()),
                ('FLC_post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.post')),
                ('FLC_author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.user')),
            ],
        ),
        migrations.CreateModel(
            name='PostAndLabels',
            fields=[
                ('PL_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('PL_post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.post')),
                ('PL_tag_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.label')),
            ],
        ),
        migrations.CreateModel(
            name='PostPicture',
            fields=[
                ('PP_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('PP_path', models.CharField(max_length=300)),
                ('PP_post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.post')),
            ],
        ),
        migrations.CreateModel(
            name='SecondLayerComment',
            fields=[
                ('SLC_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('SLC_content', models.TextField()),
                ('SLC_time', models.DateTimeField()),
                ('SLC_comment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.firstlayercomment')),
                ('SLC_author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.user')),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('RP_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('RP_content', models.TextField()),
                ('RP_comment_date', models.DateField()),
                ('RP_post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.post')),
                ('RP_receiver_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_replies', to='backend.user')),
                ('RP_sender_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_replies', to='backend.user')),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('PC_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('PC_path', models.CharField(max_length=300)),
                ('PC_category', models.IntegerField()),
                ('PC_author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.user')),
            ],
        ),
        migrations.CreateModel(
            name='Inform',
            fields=[
                ('IF_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('IF_content', models.TextField()),
                ('IF_receiver_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_informs', to='backend.user')),
                ('IF_sender_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_informs', to='backend.user')),
            ],
        ),
        migrations.CreateModel(
            name='CollectPost',
            fields=[
                ('CP_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('CP_annotation', models.TextField()),
                ('CP_post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.post')),
                ('CP_author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.user')),
            ],
        ),
    ]
