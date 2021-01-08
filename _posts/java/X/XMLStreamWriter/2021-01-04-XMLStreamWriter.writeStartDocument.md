---
title: XMLStreamWriter.writeStartDocument()
permalink: Java/XMLStreamWriter/writeStartDocument
date: 2021-01-04
key: JavaJava.X.XMLStreamWriter
category: java
tags: ['java se', 'javax.xml.stream', 'java.xml', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XMLStreamWriter.metodos valor="writeStartDocument" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void writeStartDocument() throws XMLStreamException
void writeStartDocument(String version) throws XMLStreamException
void writeStartDocument(String encoding, String version) throws XMLStreamException
~~~

## Parámetros
* **String version**,  {% include w3api/param_description.html metodo=_data parametro="String version" %}
* **String encoding**,  {% include w3api/param_description.html metodo=_data parametro="String encoding" %}

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
{%- for _ldc in site.data.Java.X.XMLStreamWriter.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
