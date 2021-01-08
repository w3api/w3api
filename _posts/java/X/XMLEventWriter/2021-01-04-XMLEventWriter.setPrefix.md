---
title: XMLEventWriter.setPrefix()
permalink: Java/XMLEventWriter/setPrefix
date: 2021-01-04
key: JavaJava.X.XMLEventWriter
category: java
tags: ['java se', 'javax.xml.stream', 'java.xml', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XMLEventWriter.metodos valor="setPrefix" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setPrefix(String prefix, String uri) throws XMLStreamException
~~~

## Parámetros
* **String prefix**,  {% include w3api/param_description.html metodo=_data parametro="String prefix" %}
* **String uri**,  {% include w3api/param_description.html metodo=_data parametro="String uri" %}

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
{%- for _ldc in site.data.Java.X.XMLEventWriter.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
