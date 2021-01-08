---
title: XMLInputFactory.createFilteredReader()
permalink: Java/XMLInputFactory/createFilteredReader
date: 2021-01-04
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
* **StreamFilter filter**,  {% include w3api/param_description.html metodo=_data parametro="StreamFilter filter" %}
* **EventFilter filter**,  {% include w3api/param_description.html metodo=_data parametro="EventFilter filter" %}
* **XMLStreamReader reader**,  {% include w3api/param_description.html metodo=_data parametro="XMLStreamReader reader" %}
* **XMLEventReader reader**,  {% include w3api/param_description.html metodo=_data parametro="XMLEventReader reader" %}

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
{%- for _ldc in site.data.Java.X.XMLInputFactory.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
