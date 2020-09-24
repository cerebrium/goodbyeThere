from channels.layers import get_channel_layer
from .serializers import MessageSerializer

async def update_message(message):
    serializer = MessageSerializer(message)
    group_name = serializer.get_group_name()
    channel_layer = get_channel_layer()
    content = {
        # This "type" passes through to the front-end to facilitate
        # our Redux events.
        "type": "UPDATE_MESSAGE",
        "payload": serializer.data,
    }
    await channel_layer.group_send(group_name, {
        # This "type" defines which handler on the Consumer gets
        # called.
        "type": "notify",
        "content": content,
    })