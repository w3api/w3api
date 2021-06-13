---
title: Collections.swap()
permalink: /Java/Collections/swap/
date: 2021-01-11
key: Java.C.Collections
category: Java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Collections.metodos valor="swap" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void swap(List<?> list, int i, int j)
~~~

## Parámetros
* **int j**,  {% include w3api/param_description.html metodo=_dato parametro="int j" %}
* **int i**,  {% include w3api/param_description.html metodo=_dato parametro="int i" %}
* **List&lt;?&gt; list**,  {% include w3api/param_description.html metodo=_dato parametro="List<?> list" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/)

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
