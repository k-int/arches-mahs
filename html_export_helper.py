def html_export_helper (obj, path_root):

    return_list = []

    def find_values(obj, path_root):

        if isinstance(obj, dict):

            for key, value in obj.items():

                if key == "@display_value":
                    content = f'{path_root}|val_from_key:"@display_value"'
                    return_list.append("{{ " + content + " }}")
                
                else:
                    new_path = path_root + f'|val_from_key:"{key}"'
                    find_values(value, new_path)
                
        elif isinstance(obj, list):

            return_list.append(f"{{% for x in {path_root} %}}")

            for x in obj:

                find_values(x, "x")

            return_list.append(f"{{% endfor %}}")
    
        else:
            return

    find_values(obj, path_root)
        
    return return_list