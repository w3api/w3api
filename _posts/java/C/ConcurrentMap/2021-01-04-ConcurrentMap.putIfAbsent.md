---
title: ConcurrentMap.putIfAbsent()
permalink: Java/ConcurrentMap/putIfAbsent
date: 2021-01-04
key: JavaJava.C.ConcurrentMap
category: java
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
* **V value**,  {% include w3api/param_description.html metodo=_data parametro="V value" %}
* **K key**,  {% include w3api/param_description.html metodo=_data parametro="K key" %}

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/), [ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ConcurrentMap](/Java/ConcurrentMap/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ConcurrentMap.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
