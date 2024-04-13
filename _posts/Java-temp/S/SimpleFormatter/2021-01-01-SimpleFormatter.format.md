---
title: SimpleFormatter.format()
permalink: /Java/SimpleFormatter/format/
date: 2021-01-11
key: Java.S.SimpleFormatter
category: Java
tags: ['java se', 'java.util.logging', 'java.logging', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SimpleFormatter.metodos valor="format" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public String format(LogRecord record)
~~~

## Parámetros
* **LogRecord record**,  {% include w3api/param_description.html metodo=_dato parametro="LogRecord record" %}

## Clase Padre
[SimpleFormatter](/Java/SimpleFormatter/)

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
