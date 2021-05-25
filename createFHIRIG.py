import json
import os
import sys
import getopt
#TODO Add other resource types, as it is very constrained to 4 types so far


def implementationGuide(url):
    print("####Building the ImplementationGuide template####")


def structureDefinition(url):
    data = {}
    print("####Building the structureDefinition template####\n")
    data['resourceType'] = 'StructureDefinition'
    name = input('Specify the name (machine-readable) of the resource\n')
    data['name'] = name
    data['url'] = url+'StructureDefinition/'+name if url.endswith('/') else url+'/StructureDefinition/'+name
    title = input('Specify the title (user-friendly) of the resource\n')
    data['title'] = title
    status = input(
        'what is the status of the system? active | retired | draft | unknown\n')
    data['status'] = status
    description = input('Describe the structure being defined (optional) \n')
    if description:
        data['description'] = description
    fhirVersion = input('FHIR version this definition targets (optional) \n')
    if fhirVersion:
        data['description'] = description
    kind = input(
        'The kind of the structure definition primitive-type | complex-type | resource | logical\n')
    data['kind'] = kind
    abstract = input(
        'Whether the structure is abstract (whether the structure is not intended to be instantiated) True | False\n').lower()
    data['abstract'] = abstract == "true"
    typ = input('The type this structure describes. If the derivation kind is "specialization" then this is the master definition for a type, and there is always one of these (a data type, an extension, a resource, including abstract ones). Otherwise the structure is a constraint on the stated type (cannot be abstract). References are URLs that are relative to http://hl7.org/fhir/StructureDefinition\n')
    data['type'] = typ
    baseDefinition = input(
        '(Base definition) Definition that this type is constrained/specialized from (Base Definition). Absolute URL has to be provided. (Optional)\n')
    data['baseDefinition'] = baseDefinition
    derivation = input(
        'How the type relates to the base definition specialization | constraint (Optional)\n')
    if derivation:
        data['derivation'] = derivation
    snapshot = input("Type anything to include a snapshot view\n")
    if snapshot:
        element = []
        while True:
            try:
                path = input("Path to the element\n")
                sliceName = input(
                    "If using slice, specify slicename if wished (Optional)\n")
                short = input(
                    "Concise definition for space-constrained presentation (Optional)\n")
                definition = input(
                    "Full formal definition for space-constrained presentation (Optional)\n")
                comment = input(
                    "Comments about the use of the element (Optional)\n")
                requirements = input(
                    "Why this resource has been created (Optional)\n")
                min = int(input("Minimum Cardinality as an integer\n"))
                max = input("Maximum Cardinality, can be a number or *\n")
                base = input("Base - Information about the base definition of the element provided to make it unnecessary for tools to trace the deviation of the element through the derived and related profiles, press anything to specify it (Optional)")
                if base:
                    base = {}
                    path = input("Path of the base element")
                    min = int(input("Min of the base element as an integer"))
                    max = input(
                        "Max of the base element as a string (*) allowed")
                    base["path"] = path
                    base["min"] = min
                    base["max"] = max
                el_type = input(
                    "Data type and Profile for this element, press any key to define it (Optional)")
                if el_type:
                    el_type = []
                    el_type_1 = {}
                    code = input(
                        "Data type or Resource (reference to definition), e.g. 'string'")
                    profile = input(
                        "Profiles (StructureDefinition or IG, optional)")
                    targetProfile = input(
                        "(Target) Profile (StructureDefinition or IG) on  the Reference/canonical target, optional")
                    el_type_1["code"] = code
                    if profile:
                        el_type_1["profile"] = profile
                    if targetProfile:
                        el_type_1["targetProfile"] = targetProfile
                    el_type.append(el_type_1)
                mustSupport = input(
                    "Whether the element must be supported or not")
                isModifier = input(
                    "If this modifies the meaning of other elements")
                isModifierReason = input(
                    "Reason that this element is marked as a modifier")
                isSummary = input(
                    "Whether the element should be included if a client requests a search with the parameter _summary = true")
                binding = input(
                    "ValueSet details if this is coded (what Valueset to bind it to), press any key to specify (Optional)")
                if binding:
                    binding = {}
                    strength = input(
                        "The strength of the binding. required | extensible | preferred | example")
                    description = input(
                        "Human explanation of the value set (Optional)")
                    valueset = input("Source of the ValueSet")
                    if strength:
                        binding["strength"] = strength
                    if description:
                        binding["description"] = description
                    if valueset:
                        binding["valueSet"] = valueset
                element["path"] = path
                if sliceName:
                    element["sliceName"] = sliceName
                if short:
                    element["short"] = short
                if definition:
                    element["definition"] = definition
                if comment:
                    element["comment"] = comment
                if requirements:
                    element["requirements"] = requirements
                if min:
                    element["min"] = min
                if max:
                    element["max"] = max
                if base:
                    element["base"] = base
                if el_type:
                    element["type"] = el_type
                if mustSupport:
                    element["mustSupport"] = sorted(mustSupport.lower()) == "true" or "yes"
                if isModifier:
                    element["isModifier"] = sorted(isModifier.lower()) == "true" or "yes"
                if isModifierReason:
                    element["isModifierReason"] = isModifierReason
                if isSummary:
                    element["isSummary"] = sorted(isSummary.lower()) == "true" or "yes"
                if binding:
                    element["binding"] = binding
            except KeyboardInterrupt:
                break
    differential = input("Type anything to include a differential view\n")
    if differential:
        element = []
        while True:
            try:
                element_dict = {}
                path = input("Path to the element\n")
                sliceName = input(
                    "If using slice, specify slicename if wished (Optional)\n")
                short = input(
                    "Concise definition for space-constrained presentation (Optional)\n")
                definition = input(
                    "Full formal definition for space-constrained presentation (Optional)\n")
                comment = input(
                    "Comments about the use of the element (Optional)\n")
                requirements = input(
                    "Why this resource has been created (Optional)\n")
                min = int(input("Minimum Cardinality\n"))
                max = input("Maximum Cardinality, can be a number or *\n")
                base = input("Base - Information about the base definition of the element provided to make it unnecessary for tools to trace the deviation of the element through the derived and related profiles (Optional)")
                if base:
                    base = {}
                    path = input("Path of the base element")
                    min = input("Min of the base element")
                    max = input("Max of the base element")
                    base["path"] = path
                    base["min"] = min
                    base["max"] = max
                el_type = input(
                    "Data type and Profile for this element (Optional). Press any key to define it")
                if el_type:
                    el_type = []
                    el_type_1 = {}
                    code = input(
                        "Data type or Resource (reference to definition), e.g. 'string'")
                    profile = input(
                        "Profiles (StructureDefinition or IG, optional)")
                    targetProfile = input(
                        "Profile (StructureDefinition or IG) on  the Reference/canonical target, optional")
                    el_type_1["code"] = code
                    if profile:
                        el_type_1["profile"] = profile
                    if targetProfile:
                        el_type_1["targetProfile"] = targetProfile
                    el_type.append(el_type_1)
                mustSupport = input(
                    "Whether the element must be supported or not")
                isModifier = input(
                    "If this modifies the meaning of other elements")
                isModifierReason = input(
                    "Reason that this element is marked as a modifier")
                isSummary = input(
                    "Whether the element should be included if a client requests a search with the parameter _summary = true")
                binding = input(
                    "ValueSet details if this is coded (what Valueset to bind it to). Press any key to define it")
                if binding:
                    binding = {}
                    strength = input(
                        "The strength of the binding. required | extensible | preferred | example")
                    description = input(
                        "Human explanation of the value set (Optional)")
                    valueset = input("Source of the ValueSet")
                    if strength:
                        binding["strength"] = strength
                    if description:
                        binding["description"] = description
                    if valueset:
                        binding["valueSet"] = valueset
                element_dict["path"] = path
                if sliceName:
                    element_dict["sliceName"] = sliceName
                if short:
                    element_dict["short"] = short
                if definition:
                    element_dict["definition"] = definition
                if comment:
                    element_dict["comment"] = comment
                if requirements:
                    element_dict["requirements"] = requirements
                if min:
                    element_dict["min"] = min
                if max:
                    element_dict["max"] = max
                if base:
                    element_dict["base"] = base
                if el_type:
                    element_dict["type"] = el_type
                if mustSupport:
                    element_dict["mustSupport"] = mustSupport
                if isModifier:
                    element_dict["isModifier"] = isModifier
                if isModifierReason:
                    element_dict["isModifierReason"] = isModifierReason
                if isSummary:
                    element_dict["isSummary"] = isSummary
                if binding:
                    element_dict["binding"] = binding
                element.append(element_dict)
            except KeyboardInterrupt:
                break
        data["differential"] = element

    path = input(
        'Specify the path with file name, this object should be saved in relative to this file\n')
    path_directory_list = path.split('/')[:-1]
    path_directory = os.path.join(*path_directory_list)
    if not os.path.exists(path_directory):
        os.mkdir(path_directory)
    with open(path, 'w') as outfile:
        json.dump(data, outfile)


def codeSystem(url):
    print(url)
    data = {}
    print("Building the codeSystem template\n")
    data['resourceType'] = 'CodeSystem'
    id = input("What id should the system have?\n")
    data['id'] = id
    status = input(
        'what is the status of the system? active | retired | draft | unknown\n')
    data['status'] = status
    content = input(
        'What is the state of the content? not-present | example | fragment | complete |supplement\n')
    data['content'] = content
    data['url'] = url + '/CodeSystem/'+id
    name = input('Specify the name (machine-readable) of the resource\n')
    data['name'] = name
    title = input('Specify the title (user-friendly) of the resource\n')
    data['title'] = title
    n_concepts = int(input('How many concepts should be included?\n'))
    data['concept'] = []
    for i in range(0, n_concepts):
        concept = {}
        code = input('Specify the code of the concept\n')
        display = input('Specify the display name of the concept\n')
        concept['code'] = code
        concept['display'] = display
        data['concept'].append(concept)
    path = input(
        'Specify the path with file name, this object should be saved in relative to this file\n')
    path_directory_list = path.split('/')[:-1]
    path_directory = os.path.join(*path_directory_list)
    if not os.path.exists(path_directory):
        os.mkdir(path_directory)
    with open(path, 'w') as outfile:
        json.dump(data, outfile)


def valueSet(url):
    data = {}
    print("####Building the ValueSet template####")
    data['resourceType'] = 'ValueSet'
    id = input("What id should the system have?\n")
    data['id'] = id
    status = input(
        'what is the status of the system? active | retired | draft | unknown\n')
    data['status'] = status
    data['url'] = (url+'ValueSet/'+id) if url.endswith('/') else (url+'/ValueSet'+id)
    name = input('Specify the name (machine-readable) of the resource\n')
    data['name'] = name
    title = input('Specify the title (user-friendly) of the resource\n')
    data['title'] = title
    compose = input('Type anything to start a defining a compose\n')
    if compose:
        compose = {}
        include = input('Type anything to include a system\n')
        if include:
            include = []
            includeSet = {}
            includeSet['system'] = input(
                'Specify the URL of the system to include\n')
            concept = input(
                'Type anything to specify the concepts to be included\n')
            concepts = []
            if concept:
                while True:
                    try:
                        exc_code = {}
                        code = input('Code to be included\n')
                        display = input(
                            'Text to display for this code for this value set in this valueset (Optional)\n')
                        exc_code['code'] = code
                        if display:
                            exc_code['display'] = display
                        concepts.append(exc_code)
                    except KeyboardInterrupt:
                        break
                includeSet['concept'] = concepts
        include.append(includeSet)
        if include: compose['include'] = include
        exclude = input('Type anything to exclude from a system (Optional)\n')
        if exclude:
            exclude = []
            excludeSet = {}
            excludeSet['system'] = input(
                'Specify the URL of the system to exclude')
            concept = input(
                'Type anything to specify the concepts to be excluded')
            concepts = []
            while True:
                try:
                    exc_code = {}
                    code = input('Code to be excluded')
                    display = input(
                        'Text to display for this code for this value set in this valueset (Optional)')
                    exc_code['code'] = code
                    if display:
                        exc_code['display'] = display
                    concepts.append(exc_code)
                except KeyboardInterrupt:
                    break
                excludeSet['concept'] = concepts
                exclude.append(excludeSet)
        if concept: compose['exclude'] = exclude
        data['compose'] = compose
    path = input(
        'Specify the path with file name, this object should be saved in relative to this file\n')
    path_directory_list = path.split('/')[:-1]
    path_directory = os.path.join(*path_directory_list)
    if not os.path.exists(path_directory):
        os.mkdir(path_directory)
    with open(path, 'w') as outfile:
        json.dump(data, outfile)


options = {
    "implementationguide": implementationGuide,
    "structuredefinition": structureDefinition,
    "codesystem": codeSystem,
    "valueset": valueSet
}


def main(argv):
    url = ''
    try:
        opts, args = getopt.getopt(argv, "u:")
    except getopt.GetoptError:
        print('createFHIRIG.py -u <url>')
        sys.exit(2)
    for opt, arg in opts:
                if opt != '-u':
                    print('createFHIRIG.py -u <base URL of the FHIR IG>')
                    sys.exit()
                elif opt in ('-u', '--url'):
                    url = arg
    while True:
        try:
            print('-----------------IG-Creation Helper-----------------')
            resourceType = input(
                'Which resource would you like to create a template for?\n').lower()
            options[resourceType](url)
        except KeyboardInterrupt:
            break


if __name__ == "__main__":
    main(sys.argv[1:])
