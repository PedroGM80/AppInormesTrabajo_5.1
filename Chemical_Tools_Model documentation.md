      

### <a id="documentation-body"></a>

![Hackolade image](/Chemical_Tools_Model%20documentation/image1.png?raw=true)

MongoDB Physical Model
----------------------

#### Schema for:

Model name: Chemical\_Tools\_Model

Author: Pedro Gallego Morrales

Version: 0.1

File name: MongoDB\_model.hck.json

Printed On: Fri Jan 28 2022 14:53:49 GMT+0100 (hora estándar de Europa central)

Created with: [Hackolade](https://hackolade.com/) - Polyglot data modeling for NoSQL databases, storage formats, REST APIs, and JSON in RDBMS

### <a id="contents"></a>

       
### <a id="model"></a>

##### 1\. Model

##### 1.1 Model **Chemical\_Tools\_Model**

##### 1.1.1 **Chemical\_Tools\_Model** Entity Relationship Diagram

![Hackolade image](/Chemical_Tools_Model%20documentation/image2.png?raw=true)

##### 1.1.2 **Chemical\_Tools\_Model** Properties

##### 1.1.2.1 **Details** tab

<table><thead><tr><td>Property</td><td>Value</td></tr></thead><tbody><tr><td><span>Model name</span></td><td>Chemical_Tools_Model</td></tr>
      <tr><td><span>Author</span></td><td>Pedro Gallego Morrales</td></tr>
      <tr><td><span>Version</span></td><td>0.1</td></tr><tr><td><span>DB vendor</span></td><td>MongoDB</td></tr>
      <tr><td><span>DB version</span></td><td>v4.4</td></tr>
      </tbody></table>

##### 1.1.3 **Chemical\_Tools\_Model** DB Definitions

### <a id="containers"></a>

##### 2\. Databases

### <a id="638d55d0-7f9e-11ec-a396-1f25adf88b9f"></a>2.1 Database **b\_db**

![Hackolade image](/Chemical_Tools_Model%20documentation/image3.png?raw=true)

##### 2.1.1 **b\_db** Properties

<table class="collection-properties-table"><thead><tr><td>Property</td><td>Value</td></tr></thead><tbody><tr><td>Database name</td><td>b_db</td></tr>
      <tr><td>Activated</td><td>true</td></tr>
      </tbody></table>

### <a id="638d55d0-7f9e-11ec-a396-1f25adf88b9f-children"></a>2.1.2 **b\_db** Collections

### <a id="6c091e60-7f9e-11ec-a396-1f25adf88b9f"></a>2.1.2.1 Collection **a\_collection**

##### 2.1.2.1.1 **a\_collection** Tree Diagram

![Hackolade image](/Chemical_Tools_Model%20documentation/image4.png?raw=true)

##### 2.1.2.1.2 **a\_collection** Properties

<table class="collection-properties-table"><thead><tr><td>Property</td><td>Value</td></tr></thead><tbody><tr><td>Collection name</td><td>a_collection</td></tr>
      <tr><td>Activated</td><td>true</td></tr>
      <tr><td>Database</td><td><a href=file:///C:/Program%20Files/Hackolade/resources/app/app.html#638d55d0-7f9e-11ec-a396-1f25adf88b9f><span class="name-container">b_db</span></a></td></tr>
      <tr><td>Capped</td><td>false</td></tr>
      <tr><td>Storage engine</td><td>WiredTiger</td></tr>
      <tr><td>Validation level</td><td>Off</td></tr>
      <tr><td>Validation action</td><td>Warn</td></tr>
      <tr><td>Additional properties</td><td>false</td></tr>
      </tbody></table>

##### 2.1.2.1.3 **a\_collection** Fields

<table><thead><tr><td>Field</td><td>Type</td><td>Req</td><td>Key</td></tr></thead>
      <tbody><tr><td><a href=file:///C:/Program%20Files/Hackolade/resources/app/app.html#cdcff100-7f9e-11ec-a396-1f25adf88b9f class="margin-0">_id</a></td><td class="no-break-word">string</td><td>true</td><td>pk</td></tr>
            
            <tr><td><a href=file:///C:/Program%20Files/Hackolade/resources/app/app.html#ec479fc0-7f9e-11ec-a396-1f25adf88b9f class="margin-0">Nombre</a></td><td class="no-break-word">string</td><td>false</td><td></td></tr>
            
            
            <tr><td><a href=file:///C:/Program%20Files/Hackolade/resources/app/app.html#08b5e9f0-7f9f-11ec-a396-1f25adf88b9f class="margin-0">Fórmula&nbsp;química</a></td><td class="no-break-word">string</td><td>false</td><td></td></tr>
            
            <tr><td><a href=file:///C:/Program%20Files/Hackolade/resources/app/app.html#2258b810-7f9f-11ec-a396-1f25adf88b9f class="margin-0">Punto&nbsp;de&nbsp;ebullición</a></td><td class="no-break-word">string</td><td>false</td><td></td></tr>
            
            <tr><td><a href=file:///C:/Program%20Files/Hackolade/resources/app/app.html#34134b10-7f9f-11ec-a396-1f25adf88b9f class="margin-0">Tipo</a></td><td class="no-break-word">string</td><td>false</td><td></td></tr></tbody></table>

### <a id="cdcff100-7f9e-11ec-a396-1f25adf88b9f"></a>2.1.2.1.3.1 Field **\_id**

##### 2.1.2.1.3.1.1 **\_id** Tree Diagram

![Hackolade image](/Chemical_Tools_Model%20documentation/image5.png?raw=true)

##### 2.1.2.1.3.1.2 **\_id** properties

<table><thead><tr><td>Property</td><td>Value</td></tr></thead><tbody>
      <tr><td>Name</td><td>_id</td></tr><tr><td>Technical name</td><td>_id</td></tr><tr><td>Activated</td><td>true</td></tr><tr><td>Id</td><td>_id</td></tr>
      <tr><td>Type</td><td>string</td></tr>
      <tr><td>Required</td><td>true</td></tr><tr><td>Primary key</td><td>true</td></tr>
 </tbody></table>

### <a id="ec479fc0-7f9e-11ec-a396-1f25adf88b9f"></a>2.1.2.1.3.2 Field **Nombre**

##### 2.1.2.1.3.2.1 **Nombre** Tree Diagram

![Hackolade image](/Chemical_Tools_Model%20documentation/image6.png?raw=true)

##### 2.1.2.1.3.2.2 **Nombre** properties

<table><thead><tr><td>Property</td><td>Value</td></tr></thead><tbody><tr><td>Name</td><td>Nombre</td></tr><tr><td>Technical name</td><td>Name</td></tr><tr><td>Activated</td><td>true</td></tr><tr><td>Id</td><td>Nombre</td></tr><tr><td>Type</td><td>string</td></tr>
 </tbody></table>

### <a id="08b5e9f0-7f9f-11ec-a396-1f25adf88b9f"></a>2.1.2.1.3.3 Field **Fórmula química**

##### 2.1.2.1.3.3.1 **Fórmula química** Tree Diagram

![Hackolade image](/Chemical_Tools_Model%20documentation/image7.png?raw=true)

##### 2.1.2.1.3.3.2 **Fórmula química** properties

<table><thead><tr><td>Property</td><td>Value</td></tr>
      </thead>
            <tbody>
                  <tr><td>Name</td><td>Fórmula química</td></tr>
                  <tr><td>Activated</td><td>true</td></tr>
                  <tr><td>Id</td><td>Fórmula química</td></tr>
                  <tr><td>Type</td><td>string</td></tr>
            </tbody>
</table>

### <a id="2258b810-7f9f-11ec-a396-1f25adf88b9f"></a>2.1.2.1.3.4 Field **Punto de ebullición**

##### 2.1.2.1.3.4.1 **Punto de ebullición** Tree Diagram

![Hackolade image](/Chemical_Tools_Model%20documentation/image8.png?raw=true)

##### 2.1.2.1.3.4.2 **Punto de ebullición** properties

<table><thead><tr><td>Property</td><td>Value</td></tr></thead>
      <tbody>
            <tr><td>Name</td><td>Punto de ebullición</td></tr>
            <tr><td>Activated</td><td>true</td></tr>
            <tr><td>Id</td><td>Punto de ebullición</td></tr>
            <tr><td>Type</td><td>string</td></tr></tbody></table>

### <a id="34134b10-7f9f-11ec-a396-1f25adf88b9f"></a>2.1.2.1.3.5 Field **Tipo**

##### 2.1.2.1.3.5.1 **Tipo** Tree Diagram

![Hackolade image](/Chemical_Tools_Model%20documentation/image9.png?raw=true)

##### 2.1.2.1.3.5.2 **Tipo** properties

<table><thead><tr><td>Property</td><td>Value</td></tr></thead><tbody><tr><td>Name</td><td>Tipo</td></tr>
      <tr><td>Activated</td><td>true</td></tr><tr><td>Id</td><td>Tipo</td></tr><tr><td>Type</td><td>string</td></tr></tbody></table>

##### 2.1.2.1.4 **a\_collection** JSON Schema

```
{
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "title": "a_collection",
    "properties": {
        "_id": {
            "id": "_id",
            "type": "string",
            "title": "_id"
        },
        "Name": {
            "id": "Nombre",
            "type": "string",
            "title": "Nombre"
        },
        "Fórmula química": {
            "id": "Fórmula química",
            "type": "string"
        },
        "Punto de ebullición": {
            "id": "Punto de ebullición",
            "type": "string"
        },
        "Tipo": {
            "id": "Tipo",
            "type": "string"
        }
    },
    "additionalProperties": false,
    "required": [
        "_id"
    ]
}
```

##### 2.1.2.1.5 **a\_collection** JSON data

```
{
    "_id": "Lorem",
    "Name": "Lorem",
    "Fórmula química": "Lorem",
    "Punto de ebullición": "Lorem",
    "Tipo": "Lorem"
}
```

##### 2.1.2.1.6 **a\_collection** Target Script

```
use b_db;

db.createCollection("a_collection", {
    "storageEngine": {
        "wiredTiger": {}
    },
    "capped": false,
    "validator": {
        "$jsonSchema": {
            "bsonType": "object",
            "title": "a_collection",
            "properties": {
                "_id": {
                    "bsonType": "string",
                    "title": "_id"
                },
                "Name": {
                    "bsonType": "string",
                    "title": "Nombre"
                },
                "Fórmula química": {
                    "bsonType": "string"
                },
                "Punto de ebullición": {
                    "bsonType": "string"
                },
                "Tipo": {
                    "bsonType": "string"
                }
            },
            "additionalProperties": false,
            "required": [
                "_id"
            ]
        }
    },
    "validationLevel": "off",
    "validationAction": "warn"
});
```

### <a id="edges"></a>
