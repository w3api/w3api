---
title: ConcurrentMap.putIfAbsent()
permalink: /Java/ConcurrentMap/putIfAbsent/
date: 2021-01-11
key: Java.C.ConcurrentMap
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConcurrentMap.metodos valor="putIfAbsent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
V putIfAbsent(K key, V value)
~~~

## Parámetros
* **V value**,  {% include w3api/param_description.html metodo=_dato parametro="V value" %}
* **K key**,  {% include w3api/param_description.html metodo=_dato parametro="K key" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/), [ClassCastException](/Java/ClassCastException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[ConcurrentMap](/Java/ConcurrentMap/)

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
