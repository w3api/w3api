---
title: XMLStreamWriter.writeAttribute()
permalink: /Java/XMLStreamWriter/writeAttribute/
date: 2021-01-11
key: Java.X.XMLStreamWriter
category: Java
tags: ['java se', 'javax.xml.stream', 'java.xml', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XMLStreamWriter.metodos valor="writeAttribute" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void writeAttribute(String localName, String value) throws XMLStreamException
void writeAttribute(String namespaceURI, String localName, String value) throws XMLStreamException
void writeAttribute(String prefix, String namespaceURI, String localName, String value) throws XMLStreamException
~~~

## Parámetros
* **String localName**,  {% include w3api/param_description.html metodo=_dato parametro="String localName" %}
* **String namespaceURI**,  {% include w3api/param_description.html metodo=_dato parametro="String namespaceURI" %}
* **String value**,  {% include w3api/param_description.html metodo=_dato parametro="String value" %}
* **String prefix**,  {% include w3api/param_description.html metodo=_dato parametro="String prefix" %}

## Excepciones
[XMLStreamException](/Java/XMLStreamException/), [IllegalStateException](/Java/IllegalStateException/)

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
