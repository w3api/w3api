---
title: Collections.asLifoQueue()
permalink: /Java/Collections/asLifoQueue/
date: 2021-01-11
key: Java.C.Collections
category: Java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Collections.metodos valor="asLifoQueue" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <T> Queue<T> asLifoQueue(Deque<T> deque)
~~~

## Parámetros
* **Deque&lt;T&gt; deque**,  {% include w3api/param_description.html metodo=_dato parametro="Deque<T> deque" %}

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
