---
title: StAXSource.StAXSource()
permalink: /Java/StAXSource/StAXSource/
date: 2021-01-11
key: Java.S.StAXSource
category: Java
tags: ['java se', 'javax.xml.transform.stax', 'java.xml', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StAXSource.constructores valor="StAXSource" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public StAXSource(XMLEventReader xmlEventReader) throws XMLStreamException
public StAXSource(XMLStreamReader xmlStreamReader)
~~~

## Parámetros
* **XMLStreamReader xmlStreamReader**,  {% include w3api/param_description.html metodo=_dato parametro="XMLStreamReader xmlStreamReader" %}
* **XMLEventReader xmlEventReader**,  {% include w3api/param_description.html metodo=_dato parametro="XMLEventReader xmlEventReader" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [IllegalStateException](/Java/IllegalStateException/), [XMLStreamException](/Java/XMLStreamException/)

## Clase Padre
[StAXSource](/Java/StAXSource/)

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
