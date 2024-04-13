---
title: LogRecord.setInstant()
permalink: /Java/LogRecord/setInstant/
date: 2021-01-11
key: Java.L.LogRecord
category: Java
tags: ['java se', 'java.util.logging', 'java.logging', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LogRecord.metodos valor="setInstant" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setInstant(Instant instant)
~~~

## Parámetros
* **Instant instant**,  {% include w3api/param_description.html metodo=_dato parametro="Instant instant" %}

## Excepciones
[ArithmeticException](/Java/ArithmeticException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[LogRecord](/Java/LogRecord/)

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
