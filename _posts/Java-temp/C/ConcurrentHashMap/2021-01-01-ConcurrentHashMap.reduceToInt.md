---
title: ConcurrentHashMap.reduceToInt()
permalink: /Java/ConcurrentHashMap/reduceToInt/
date: 2021-01-11
key: Java.C.ConcurrentHashMap
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConcurrentHashMap.metodos valor="reduceToInt" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int reduceToInt(long parallelismThreshold, ToIntBiFunction<? super K,? super V> transformer, int basis, IntBinaryOperator reducer)
~~~

## Parámetros
* **IntBinaryOperator reducer**,  {% include w3api/param_description.html metodo=_dato parametro="IntBinaryOperator reducer" %}
* **int basis**,  {% include w3api/param_description.html metodo=_dato parametro="int basis" %}
* **long parallelismThreshold**,  {% include w3api/param_description.html metodo=_dato parametro="long parallelismThreshold" %}
* **? super V&gt; transformer**,  {% include w3api/param_description.html metodo=_dato parametro="? super V> transformer" %}
* **ToIntBiFunction&lt;? super K**,  {% include w3api/param_description.html metodo=_dato parametro="ToIntBiFunction<? super K" %}

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
