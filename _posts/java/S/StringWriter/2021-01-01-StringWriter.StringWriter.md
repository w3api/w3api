---
title: StringWriter.StringWriter()
permalink: /Java/StringWriter/StringWriter/
date: 2021-01-11
key: Java.S.StringWriter
category: Java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StringWriter.constructores valor="StringWriter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public StringWriter()
public StringWriter(int initialSize)
~~~

## Parámetros
* **int initialSize**,  {% include w3api/param_description.html metodo=_dato parametro="int initialSize" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[StringWriter](/Java/StringWriter/)

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
