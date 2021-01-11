---
title: XMLStreamWriter.writeNamespace()
permalink: Java/XMLStreamWriter/writeNamespace
date: 2021-01-11
key: JavaJava.X.XMLStreamWriter
category: java
tags: ['java se', 'javax.xml.stream', 'java.xml', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XMLStreamWriter.metodos valor="writeNamespace" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void writeNamespace(String prefix, String namespaceURI) throws XMLStreamException
~~~

## Parámetros
* **String prefix**,  {% include w3api/param_description.html metodo=_dato parametro="String prefix" %}
* **String namespaceURI**,  {% include w3api/param_description.html metodo=_dato parametro="String namespaceURI" %}

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
