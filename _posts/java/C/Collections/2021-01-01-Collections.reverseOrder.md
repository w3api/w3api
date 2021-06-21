---
title: Collections.reverseOrder()
permalink: /Java/Collections/reverseOrder/
date: 2021-01-11
key: Java.C.Collections
category: Java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Collections.metodos valor="reverseOrder" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <T> Comparator<T> reverseOrder()
static <T> Comparator<T> reverseOrder(Comparator<T> cmp)
~~~

## Parámetros
* **Comparator&lt;T&gt; cmp**,  {% include w3api/param_description.html metodo=_dato parametro="Comparator<T> cmp" %}

## Clase Padre
[Collections](/Java/Collections/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
