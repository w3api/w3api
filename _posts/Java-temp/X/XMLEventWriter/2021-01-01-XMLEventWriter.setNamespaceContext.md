---
title: XMLEventWriter.setNamespaceContext()
permalink: /Java/XMLEventWriter/setNamespaceContext/
date: 2021-01-11
key: Java.X.XMLEventWriter
category: Java
tags: ['java se', 'javax.xml.stream', 'java.xml', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XMLEventWriter.metodos valor="setNamespaceContext" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setNamespaceContext(NamespaceContext context) throws XMLStreamException
~~~

## Parámetros
* **NamespaceContext context**,  {% include w3api/param_description.html metodo=_dato parametro="NamespaceContext context" %}

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
