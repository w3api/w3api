---
title: XMLInputFactory.createFilteredReader()
permalink: Java/XMLInputFactory/createFilteredReader
date: 2021-01-11
key: JavaJava.X.XMLInputFactory
category: java
tags: ['java se', 'javax.xml.stream', 'java.xml', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XMLInputFactory.metodos valor="createFilteredReader" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract XMLEventReader createFilteredReader(XMLEventReader reader, EventFilter filter) throws XMLStreamException
public abstract XMLStreamReader createFilteredReader(XMLStreamReader reader, StreamFilter filter) throws XMLStreamException
~~~

## Parámetros
* **EventFilter filter**,  {% include w3api/param_description.html metodo=_dato parametro="EventFilter filter" %}
* **XMLEventReader reader**,  {% include w3api/param_description.html metodo=_dato parametro="XMLEventReader reader" %}
* **XMLStreamReader reader**,  {% include w3api/param_description.html metodo=_dato parametro="XMLStreamReader reader" %}
* **StreamFilter filter**,  {% include w3api/param_description.html metodo=_dato parametro="StreamFilter filter" %}

## Excepciones
[XMLStreamException](/Java/XMLStreamException/)

## Clase Padre
[XMLInputFactory](/Java/XMLInputFactory/)

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
