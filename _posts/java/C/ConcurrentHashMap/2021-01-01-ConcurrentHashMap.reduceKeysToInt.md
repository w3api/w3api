---
title: ConcurrentHashMap.reduceKeysToInt()
permalink: /Java/ConcurrentHashMap/reduceKeysToInt/
date: 2021-01-11
key: Java.C.ConcurrentHashMap
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConcurrentHashMap.metodos valor="reduceKeysToInt" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int reduceKeysToInt(long parallelismThreshold, ToIntFunction<? super K> transformer, int basis, IntBinaryOperator reducer)
~~~

## Parámetros
* **ToIntFunction&lt;? super K&gt; transformer**,  {% include w3api/param_description.html metodo=_dato parametro="ToIntFunction<? super K> transformer" %}
* **long parallelismThreshold**,  {% include w3api/param_description.html metodo=_dato parametro="long parallelismThreshold" %}
* **IntBinaryOperator reducer**,  {% include w3api/param_description.html metodo=_dato parametro="IntBinaryOperator reducer" %}
* **int basis**,  {% include w3api/param_description.html metodo=_dato parametro="int basis" %}

## Clase Padre
[ConcurrentHashMap](/Java/ConcurrentHashMap/)

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
