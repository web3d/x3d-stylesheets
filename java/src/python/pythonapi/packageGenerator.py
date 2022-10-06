import xml.etree.ElementTree
import re

class alone_field(object):
    def __init__(self, name, type):
        self.attrs = {}
        self.attrs['name'] = name
        self.attrs['type'] = type
        return None
    def get(self, field):
        return self.attrs[field]
    def __getitem__(self, field):
        return self.attrs[field]
    def iter(self, field):
        return []

class ClassPrinter(object):
    def __init__(self, node, name, meta = ""):
        self.__choice_table = \
        {
            "initializeOnly": self.initialize,
            "inputOnly": self.setter,
            "inputOutput": self.settergetter,
            "outputOnly": self.getter,
            "toXML": self.toXML,
            "toXMLNode": self.toXMLNode,
            None: self.getter
        }
        self.node = node
        self.name = name
        self.parents = []
        self.metaInfo = meta

        addinhers = self.node.iter("AdditionalInheritance")
        for addinher in addinhers:
            self.parents.append(addinher.get('baseType'))

        inhers = self.node.iter("Inheritance")
        for inher in inhers:
            self.parents.append(inher.get('baseType'))

        self.printed = False

    def private(self, fld):
        if fld == "Children":
                fld = "children"
        return "self.__"+fld

    def getField(self, name):
        start = self.getStart(name)
        name = self.getName(name)
        if name == 'class':
            fld = name + "_"
        elif name == 'global':
            fld = name + "_"
        else:
            fld = name
        return fld

    def getName(self, name):
        start = self.getStart(name)
        if name == "address":
            pass
        elif re.search(r"_changed$", name):
            name = name
        elif re.search(r"^addSet", name):
            name = name[start+3:start+4].upper() + name[start+4:]
        elif re.search(r"^removeSet", name):
            name = name[start+3:start+4].upper() + name[start+4:]
        elif re.search(r"^getSet", name):
            name = name[start+3:start+4].upper() + name[start+4:]
        elif re.search(r"^add", name):
            name = name[start:start+1].upper() + name[start+1:]
        elif re.search(r"^remove", name):
            name = name[start:start+1].upper() + name[start+1:]
        elif re.search(r"^is", name):
            name = name[start:start+1].upper() + name[start+1:]
        elif re.search(r"^set_", name):
            name = name[start:]
        elif re.search(r"^set", name):
            name = name[start:start+1].upper() + name[start+1:]
        elif re.search(r"^get", name):
            name = name[start:start+1].upper() + name[start+1:]
        return name

    def getFunctionName(self, name):
        start = self.getStart(name)
        functionName = name[:start] + self.getName(name)
        return functionName

    def getStart(self, name):
        start = 0
        if name == "address":
            start = 0
        elif re.search(r"_changed$", name):
            start = 0
        elif re.search(r"^addSet", name):
            start = 3
        elif re.search(r"^removeSet", name):
            start = 6
        elif re.search(r"^getSet", name):
            start = 3
        elif re.search(r"^add", name):
            start = 3
        elif re.search(r"^remove", name):
            start = 6
        elif re.search(r"^is", name):
            start = 2
        elif re.search(r"^set_", name):
            start = 4
        elif re.search(r"^set", name):
            start = 3
        elif re.search(r"^get", name):
            start = 3
        return start


    def getDefault(self, field):
        str = ""
        try:
            if field.get('type').startswith("MF") or field.get('type') == "SFColor" or field.get('type') == "SFVec2f" or field.get('type') == "SFVec3f":
                els = re.split("[, \r\n\t]+", field.get('default'))
                str += '[' + (", ".join(els)) + ']'
            elif field.get('type') == 'SFString':
                str += '"'+field.get('default')+'"'
            elif re.search(r"\s", field.get('default')):
                str += '[' + ", ".join(field.get('default').split()) + ']'
            else:
                if field.get('default') == 'true':
                    field.set('default', 'True')
                if field.get('default') == 'false':
                    field.set('default', 'False')
                if field.get('default') == 'NULL':
                    field.set('default', 'None')
                str += field.get('default')
        except:
                str += "None"
        return str


    def toXMLNode(self, field, name):
        str = ''
        fld = self.getField(name)
        str += "        str += '<"+fld+"'\n"
        str += "        if "+self.private(fld)+" is not None:\n"
        str += "           for s in "+self.private(fld)+":\n"
        str += "               if type(s) not in ['head', 'Scene']:\n"
        str += "                   str += s.toXML()\n"
        str += "        str += '>'\n"
        str += "        if "+self.private(fld)+" is not None:\n"
        str += "           for s in "+self.private(fld)+":\n"
        str += "               if type(s) in ['head', 'Scene']:\n"
        str += "                   str += s.toXMLNode()\n"
        str += "        str += '</"+fld+">'\n"
        return str

    def toXML(self, field, name):
        str = ''
        fld = self.getField(name)

        str += "        if "+self.private(fld)+" is not None:\n"
        str += "            if isinstance("+self.private(fld)+", six.string_types):\n"
        str += "                str += ' "+fld+"=\"'+" + self.private(fld)  + "+'\"'\n"
        str += "            else:\n"
        str += "                str += ' "+fld+"=\"'+" + self.private(fld)  + "[0]+'\"'\n"
        return str

    def initialize(self, field, name):
        str = ""
        fld = self.getField(name)
        str += '        '+fld+'  = ' + 'kwargs.pop("' + fld + '", ' + self.getDefault(field) + ")\n"
        if fld != "accessType":  # hack for now, no check on None accessTypes
            str += self.settervalidate(field, fld)
        str += '        '+self.private(fld)+' = '+fld+'\n'
        return str

    def settervalidate(self, field, name):
        fld = self.getField(name)
        str = ""
        rel = { 'minInclusive':" < ",
                 'maxInclusive':" > ",
                 'minExclusive':" <= ",
                 'maxExclusive':" >= "}
        for k,v in rel.items():
            try:
                if field.get('type').startswith("MF") or field.get('type') == "SFColor" or field.get('type') == "SFVec2f" or field.get('type') == "SFVec3f":
                    str += "        if "+fld+" == None or len("+fld+") <= 0 or "+k[0:3] +"("+fld+") " + v + " " + field.get(k) + ":\n"
                    str += "            return None\n"
                else:
                    str += "        if "+fld+" == None or "+fld+" " + v + " " + field.get(k) + ":\n"
                    str += "            return None\n"
            
            except:
                pass

        try:
            if field.get('additionalEnumerationValuesAllowed') != "true":
                enumerations = field.iter("enumeration")
                efound = 0
                for enum in enumerations:
                    if efound == 0:
                        str += "        if " + "'"+enum.get('value')+"'" + ' == '+fld+':\n'
                        str += "            pass\n"
                        efound = 1
                    else:
                        str += "        elif " + "'"+enum.get('value')+"'" + ' == '+fld+':\n'
                        str += "            pass\n"
                if efound == 1:
                    str +=     "        else:\n"
                    str +=     "            return None\n"
        except KeyError:
            pass
        return str

    def setter(self, field, name):
        str = ""
        fld = self.getField(name)

        # this may be cheating, if there's a setter, there must be a property
        str += '    @property\n'
        str += '    def '+ fld + '(self):\n'
        str += '        return ' + self.private(fld) + "\n"

        str += '    @'+fld+'.setter\n'
        str += '    def ' + fld +'(self, value = ' + self.getDefault(field) +  "):\n"
        str += self.settervalidate(field, "value")
        str += '        '+self.private(fld)+' = [value]\n'

        if not name.startswith("add") and not name.startswith("remove"):
            if name.startswith('set'):
                functionName = self.getFunctionName(name)
            else:
                functionName = self.getFunctionName("set"+name)
            str += '    def ' + functionName +'(self, ' + fld +' = ' + self.getDefault(field) +  "):\n"
            str += self.settervalidate(field, name)
            str += '        '+self.private(fld)+' = ['+fld+"]\n"
            str += "        return self\n"

        if not name.startswith("set") and not name.startswith("remove"):
            if name.startswith('add'):
                functionName = self.getFunctionName(name)
            else:
                functionName = self.getFunctionName("add"+name)
            str += '    def ' + functionName +'(self, ' + fld +' = ' + self.getDefault(field) +  "):\n"
            str += self.settervalidate(field, name)
            str += "        if "+self.private(fld)+" == None:"
            str += '            '+self.private(fld)+' =  []\n'
            str += '        '+self.private(fld)+' +=  ['+fld+']\n'
            str += "        return self\n"

        return str


    def getter(self, field, name):
        str = ""
        fld = self.getField(name)

        if not name.startswith("is"):
            functionName = self.getFunctionName("remove"+name)
            str += '    def ' + functionName +'(self, '+fld+"):\n"
            str += '        '+self.private(fld)+' = [x for x in '+self.private(fld)+' if x not in '+fld+']'+"\n"
            str += '        return ' + self.private(fld) + "\n"

        if field.get('type') == 'SFBool':
            if name.startswith('is'):
                functionName = self.getFunctionName(name)
            else:
                functionName = self.getFunctionName("is"+name)
            str += '    def '+ functionName + '(self, ' + fld +' = ' + self.getDefault(field) +  "):\n"
            str += '        return ' + self.private(fld) + "\n"

        else:
            functionName = self.getFunctionName("get"+name)
            str += '    def '+ functionName + '(self, ' + fld +' = ' + self.getDefault(field) +  "):\n"
            str += '        return ' + self.private(fld) + "\n"

            functionName = self.getFunctionName(name+"_changed")
            str += '    def '+ functionName + '(self, ' + fld +' = ' + self.getDefault(field) +  "):\n"
            str += '        return ' + self.private(fld) + "\n"

        return str

    def settergetter(self, field, name):
        str = ""
        str += self.setter(field, name)
        str += self.getter(field, name)
        return str

    def processField(self, field):
        name = field.get('name')
        name = re.sub(r"-", "_", name)
        name = re.sub(r":", "_", name)
        return name


    def setUpField(self, field, accessType):
        name = self.processField(field)
        return self.__choice_table[accessType](field, name)

    def setUpAloneField(self, fieldname, fieldtype, accessType):
        field = alone_field(fieldname, fieldtype)
        return self.setUpField(field, accessType)



    def printClass(self):
        str = ""
        if self.printed:
            return str
        for parent in self.parents:
            try:
                str += classes[parent].printClass()
            except:
                pass
        str += 'class ' + self.name + self.metaInfo
        strjoin = ", ".join(self.parents)
        if strjoin != "" and not strjoin.startswith("xs:") and strjoin != "SFString":
            str += "("+strjoin+")"
        else:
            str += "(object)"
        str += ":\n"
        str += "    def __init__(self, **kwargs):\n"
            
        if self.name == "X3D" or self.name == "meta" or self.name == "head":
            pass
        else:
            if strjoin == "":
                str += "        super("+ self.name + self.metaInfo + ", self)."+"__init__()\n"
            else:
                str += "        super("+ self.name + self.metaInfo + ", self)."+"__init__(**kwargs)\n"

        # create constructor body
        fields = self.node.iter("field")

        for field in fields:
            str += self.setUpField(field, "initializeOnly")

        if self.name == "Script":
            str += self.setUpAloneField("field", 'MFNode', "initializeOnly")
            str += self.setUpAloneField("IS", 'MFNode', "initializeOnly")
        if self.name == "ComposedShader":
            str += self.setUpAloneField("field", 'MFNode', "initializeOnly")
        if self.name == "field":
            str += self.setUpAloneField("children", 'MFNode', "initializeOnly")
        if self.name == "Scene":
            str += self.setUpAloneField("LayerSet", 'MFNode', "initializeOnly")

        # now create other functions
        fields = self.node.iter("field")

        for field in fields:
            if field.get('accessType') != 'initializeOnly':
                str += self.setUpField(field, field.get('accessType'))

        if not re.search(r"^SF", self.name) and not re.search(r"^MF", self.name):
            str += self.setUpAloneField("comments", '#comment', "inputOnly")

        if self.name == "ComposedShader":
            str += self.setUpAloneField("sourceCode", '#cdata', "inputOnly")
        elif self.name == "Script":
            str += self.setUpAloneField("sourceCode", '#cdata', "inputOnly")
        elif self.name == "Collision":
            str += self.setUpAloneField("proxy", 'MFNode', "inputOnly")
        elif self.name == "LayerSet":
            str += self.setUpAloneField("order", 'MFInt32', "inputOnly")

        if self.name == "ComposedShader":
            str += self.setUpAloneField("field", 'MFNode', "inputOutput")
        elif self.name == "Script":
            str += self.setUpAloneField("field", 'MFNode', "inputOutput")
        elif self.name == "field":
            str += self.setUpAloneField("children", 'MFNode', "inputOutput")
        elif self.name == "head":
            str += self.setUpAloneField("meta", 'MFNode', "inputOutput")
        elif self.name == "Scene":
            str += self.setUpAloneField("LayerSet", 'MFNode', "inputOutput")

        if self.name in [ "TouchSensor", "NavigationInfo", "Viewpoint", "OrientationInterpolator", "PositionInterpolator", "DirectionalLight", "Group", "Transform", "Shape", "Material", "Script", "ProtoInstance", "ShaderPart" ]:
            str += self.setUpAloneField("IS", 'MFNode', "inputOutput")

        # stream to XML
        str += "    def toXML(self):\n"
        str += "        str = ''\n"
        str += "        str += '<"+self.name+"'\n"
        fields = self.node.iter("field")

        for field in fields:
            if field.get("type") not in ['SFNode', 'MFNode']:
                str += self.setUpField(field, "toXML")
        str += "        str += '>'\n"
        fields = self.node.iter("field")

        for field in fields:
            if field.get("type") in ['SFNode', 'MFNode']:
                str += self.setUpField(field, "toXMLNode")
        str += "        str += '</"+self.name+">'\n"
        str += "        return str\n"

        str += '\n\n'
        self.printed = True
        return str

code = "import six\n"
code += "import json\n"
code += "import sys\n"

soup = xml.etree.ElementTree.parse(open("../../../../../../specifications/X3dUnifiedObjectModel-4.0.xml")).getroot()

classes = {}

ants = soup.iter("AbstractNodeType")
for ant in ants:
    classes[ant.get('name')] = ClassPrinter(ant, ant.get('name'))

aots = soup.iter("AbstractObjectType")
for aot in aots:
    classes[aot.get('name')] = ClassPrinter(aot, aot.get('name'))

cns = soup.iter("ConcreteNode")
for cn in cns:
    classes[cn.get('name')] = ClassPrinter(cn, cn.get('name'), "")

sts = soup.iter("Statement")
for st in sts:
    classes[st.get('name')] = ClassPrinter(st, st.get('name'), "")

fts = soup.iter("FieldType")
for ft in fts:
    classes[ft.get('type')] = ClassPrinter(ft, ft.get('type'), "")

for k,v in classes.items():
    code += v.printClass()

f = open("X3Dpackage.py", "w")
f.write(code)
f.close()
