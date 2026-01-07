server_url = "https://api.restful-api.dev/objects"
single_object_id = 7
new_object_payload = {
	"name": "Test Laptop",
	"data": {
		"CPU model": "Intel Core i7",
		"Hard disk size": "512 GB",
		"price": 999.99,
		"year": 2021
	}
}

# payload and id for update tests
update_object_id = 7
update_object_payload_put = {
	"name": "Updated Laptop",
	"data": {
		"CPU model": "Intel Core i9",
		"Hard disk size": "1 TB",
		"price": 1299.99,
		"year": 2022
	}
}

update_object_payload_patch = {
	"data": {
		"price": 1199.99
	}
}

# id for delete tests
delete_object_id = 7