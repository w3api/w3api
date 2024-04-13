---
title: XMLStreamWriter.writeStartElement()
permalink: /Java/XMLStreamWriter/writeStartElement/
date: 2021-01-11
key: Java.X.XMLStreamWriter
category: Java
tags: ['java se', 'javax.xml.stream', 'java.xml', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XMLStreamWriter.metodos valor="writeStartElement" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void writeStartElement(String localName) throws XMLStreamException
void writeStartElement(String namespaceURI, String localName) throws XMLStreamException
void writeStartElement(String prefix, String localName, String namespaceURI) throws XMLStreamException
~~~

## Parámetros
* **String localName**,  {% include w3api/param_description.html metodo=_dato parametro="String localName" %}
* **String prefix**,  {% include w3api/param_description.html metodo=_dato parametro="String prefix" %}
* **String namespaceURI**,  {% include w3api/param_description.html metodo=_dato parametro="String namespaceURI" %}

## Excepciones
[XMLStreamException](/Java/XMLStreamException/)

## Clase Padre
[XMLStreamWriter](/Java/XMLStreamWriter/)

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
