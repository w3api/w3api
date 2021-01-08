---
title: XMLEventAllocator.allocate()
permalink: Java/XMLEventAllocator/allocate
date: 2021-01-04
key: JavaJava.X.XMLEventAllocator
category: java
tags: ['java se', 'javax.xml.stream.util', 'java.xml', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XMLEventAllocator.metodos valor="allocate" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
XMLEvent allocate(XMLStreamReader reader) throws XMLStreamException
void allocate(XMLStreamReader reader, XMLEventConsumer consumer) throws XMLStreamException
~~~

## Parámetros
* **XMLEventConsumer consumer**,  {% include w3api/param_description.html metodo=_data parametro="XMLEventConsumer consumer" %}
* **XMLStreamReader reader**,  {% include w3api/param_description.html metodo=_data parametro="XMLStreamReader reader" %}

## Excepciones
[XMLStreamException](/Java/XMLStreamException/)

## Clase Padre
[XMLEventAllocator](/Java/XMLEventAllocator/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.X.XMLEventAllocator.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
