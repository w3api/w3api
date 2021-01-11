---
title: XMLReaderFactory.createXMLReader()
permalink: Java/XMLReaderFactory/createXMLReader
date: 2021-01-11
key: JavaJava.X.XMLReaderFactory
category: java
tags: ['java se', 'org.xml.sax.helpers', 'java.xml', 'metodo java', 'Java 1.4', 'SAX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XMLReaderFactory.metodos valor="createXMLReader" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static XMLReader createXMLReader() throws SAXException
public static XMLReader createXMLReader(String className) throws SAXException
~~~

## Parámetros
* **String className**,  {% include w3api/param_description.html metodo=_dato parametro="String className" %}

## Excepciones
[SAXException](/Java/SAXException/)

## Clase Padre
[XMLReaderFactory](/Java/XMLReaderFactory/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
