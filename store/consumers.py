import json
from django.contrib.auth.models import User
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

from customers.models import Customer
from store.models import Product, Comment


class CommentsConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.product_id = self.scope['url_route']['kwargs']['product_id']
        self.product_group_name = 'product_%s' % self.product_id

        print("Websocket Connected..")

        await self.channel_layer.group_add(
            self.product_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.discard(
            self.product_group_name,
            self.channel_name
        )

    async def receive(self, text_data):

        text_data_json = json.loads(text_data)
        comment = text_data_json['text']
        print(text_data + " Comment Received..")

        new_comment = await self.create_new_comment(comment)
        print(new_comment)
        data = {
            'author': new_comment.author.username,
            'date_posted': new_comment.date_posted.strftime('%Y-%m-%d %H:%m'),
            'text': new_comment.text,
            'image': new_comment.image.url
        }


        await self.channel_layer.group_send(
            self.product_group_name,
            {
                'type': 'new_comment',
                'message': data
            }
        )


    async def new_comment(self,event):
        message = event['message']

        await self.send(
            text_data=json.dumps({
                'message': message
            })
        )

    @database_sync_to_async
    def create_new_comment(self,content):

        new_comment = Comment(
            author=self.scope['user'],
            text=content,
            product_connected_id=int(self.product_id)
        )
        print("New Comment Created of " + new_comment.author.username)
        new_comment.save()
        return new_comment


