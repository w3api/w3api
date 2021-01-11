---
title: StAXResult.StAXResult()
permalink: Java/StAXResult/StAXResult
date: 2021-01-11
key: JavaJava.S.StAXResult
category: java
tags: ['java se', 'javax.xml.transform.stax', 'java.xml', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StAXResult.constructores valor="StAXResult" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public StAXResult(XMLEventWriter xmlEventWriter)
public StAXResult(XMLStreamWriter xmlStreamWriter)
~~~

## Parámetros
* **XMLStreamWriter xmlStreamWriter**,  {% include w3api/param_description.html metodo=_dato parametro="XMLStreamWriter xmlStreamWriter" %}
* **XMLEventWriter xmlEventWriter**,  {% include w3api/param_description.html metodo=_dato parametro="XMLEventWriter xmlEventWriter" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[StAXResult](/Java/StAXResult/)

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
