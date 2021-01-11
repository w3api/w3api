---
title: Collections.rotate()
permalink: Java/Collections/rotate
date: 2021-01-11
key: JavaJava.C.Collections
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Collections.metodos valor="rotate" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void rotate(List<?> list, int distance)
~~~

## Parámetros
* **int distance**,  {% include w3api/param_description.html metodo=_dato parametro="int distance" %}
* **List&lt;?&gt; list**,  {% include w3api/param_description.html metodo=_dato parametro="List<?> list" %}

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[Collections](/Java/Collections/)

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
