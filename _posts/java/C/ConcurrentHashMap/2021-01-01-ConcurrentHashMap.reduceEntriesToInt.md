---
title: ConcurrentHashMap.reduceEntriesToInt()
permalink: Java/ConcurrentHashMap/reduceEntriesToInt
date: 2021-01-11
key: JavaJava.C.ConcurrentHashMap
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConcurrentHashMap.metodos valor="reduceEntriesToInt" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int reduceEntriesToInt(long parallelismThreshold, ToIntFunction<Map.Entry<K,V>> transformer, int basis, IntBinaryOperator reducer)
~~~

## Parámetros
* **ToIntFunction&lt;Map.Entry&lt;K**,  {% include w3api/param_description.html metodo=_dato parametro="ToIntFunction<Map.Entry<K" %}
* **IntBinaryOperator reducer**,  {% include w3api/param_description.html metodo=_dato parametro="IntBinaryOperator reducer" %}
* **int basis**,  {% include w3api/param_description.html metodo=_dato parametro="int basis" %}
* **long parallelismThreshold**,  {% include w3api/param_description.html metodo=_dato parametro="long parallelismThreshold" %}
* **V&gt;&gt; transformer**,  {% include w3api/param_description.html metodo=_dato parametro="V>> transformer" %}

## Clase Padre
[ConcurrentHashMap](/Java/ConcurrentHashMap/)

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
