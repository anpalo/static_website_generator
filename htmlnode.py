class HTMLNode:

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplemented
    
    def props_to_html(self):
        html_string = ""
        if self.props is not None:
            for key, value in self.props.items():
                html_string += f' {key}="{value}"'
        return html_string.strip()
    
    
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if not self.value:
            raise ValueError
        if self.tag is None:
            return str(self.value)
        if self.props:
            return f'<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>'
        return f'<{self.tag}>{self.value}</{self.tag}>'

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self): 
        if not self.tag:
            raise ValueError('Tag missing')
        if not self.children:
            raise ValueError('children expects argument(s)')
        new_string = f"<{self.tag}>"
        for node in self.children:
            new_node = node.to_html()
            new_string += new_node    
        final_string = f"{new_string}</{self.tag}>"
        return final_string
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
    

        
        
