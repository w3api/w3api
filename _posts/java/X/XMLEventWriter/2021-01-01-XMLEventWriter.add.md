---
title: XMLEventWriter.add()
permalink: Java/XMLEventWriter/add
date: 2021-01-11
key: JavaJava.X.XMLEventWriter
category: java
tags: ['java se', 'javax.xml.stream', 'java.xml', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XMLEventWriter.metodos valor="add" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void add(XMLEvent event) throws XMLStreamException
void add(XMLEventReader reader) throws XMLStreamException
~~~

## Parámetros
* **XMLEvent event**,  {% include w3api/param_description.html metodo=_dato parametro="XMLEvent event" %}
* **XMLEventReader reader**,  {% include w3api/param_description.html metodo=_dato parametro="XMLEventReader reader" %}

## Excepciones
[XMLStreamException](/Java/XMLStreamException/)

## Clase Padre
[XMLEventWriter](/Java/XMLEventWriter/)

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
