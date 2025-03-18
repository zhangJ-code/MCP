from gradio_client import Client, handle_file

client = Client("http://10.30.1.46:7861/")
result = client.predict(
		image_input=handle_file(r'C:\Users\jian_zhang\Desktop\zuomian.png'),
		box_threshold=0.05,
		iou_threshold=0.1,
		use_paddleocr=False,
		imgsz=1920,
		icon_process_batch_size=64,
		api_name="/process"
)
print(result)
    