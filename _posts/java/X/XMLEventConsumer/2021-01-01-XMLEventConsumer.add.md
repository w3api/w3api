---
title: XMLEventConsumer.add()
permalink: /Java/XMLEventConsumer/add/
date: 2021-01-11
key: Java.X.XMLEventConsumer
category: Java
tags: ['java se', 'javax.xml.stream.util', 'java.xml', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XMLEventConsumer.metodos valor="add" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void add(XMLEvent event) throws XMLStreamException
~~~

## Parámetros
* **XMLEvent event**,  {% include w3api/param_description.html metodo=_dato parametro="XMLEvent event" %}

## Excepciones
[XMLStreamException](/Java/XMLStreamException/)

## Clase Padre
[XMLEventConsumer](/Java/XMLEventConsumer/)

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
