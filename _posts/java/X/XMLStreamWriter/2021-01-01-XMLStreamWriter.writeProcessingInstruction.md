---
title: XMLStreamWriter.writeProcessingInstruction()
permalink: /Java/XMLStreamWriter/writeProcessingInstruction/
date: 2021-01-11
key: Java.X.XMLStreamWriter
category: Java
tags: ['java se', 'javax.xml.stream', 'java.xml', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XMLStreamWriter.metodos valor="writeProcessingInstruction" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void writeProcessingInstruction(String target) throws XMLStreamException
void writeProcessingInstruction(String target, String data) throws XMLStreamException
~~~

## Parámetros
* **String data**,  {% include w3api/param_description.html metodo=_dato parametro="String data" %}
* **String target**,  {% include w3api/param_description.html metodo=_dato parametro="String target" %}

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
