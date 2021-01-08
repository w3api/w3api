---
title: StAXSource.StAXSource()
permalink: Java/StAXSource/StAXSource
date: 2021-01-04
key: JavaJava.S.StAXSource
category: java
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
* **XMLStreamReader xmlStreamReader**,  {% include w3api/param_description.html metodo=_data parametro="XMLStreamReader xmlStreamReader" %}
* **XMLEventReader xmlEventReader**,  {% include w3api/param_description.html metodo=_data parametro="XMLEventReader xmlEventReader" %}

## Excepciones
[XMLStreamException](/Java/XMLStreamException/), [IllegalStateException](/Java/IllegalStateException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[StAXSource](/Java/StAXSource/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.StAXSource.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
