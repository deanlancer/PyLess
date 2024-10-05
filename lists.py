plugins = ["lsp", "black", "cmp", "lualine", ]
print( plugins )
print (plugins[0])
plugins.append("plenary")
print(plugins)
plugins.extend(["playground", "suda"])
print(plugins)
plugins.remove("suda")
print("suda" in plugins)
