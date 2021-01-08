---
title: ConcurrentHashMap.reduceEntriesToLong()
permalink: Java/ConcurrentHashMap/reduceEntriesToLong
date: 2021-01-04
key: JavaJava.C.ConcurrentHashMap
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConcurrentHashMap.metodos valor="reduceEntriesToLong" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public long reduceEntriesToLong(long parallelismThreshold, ToLongFunction<Map.Entry<K,V>> transformer, long basis, LongBinaryOperator reducer)
~~~

## Parámetros
* **long parallelismThreshold**,  {% include w3api/param_description.html metodo=_data parametro="long parallelismThreshold" %}
* **ToLongFunction&lt;Map.Entry&lt;K**,  {% include w3api/param_description.html metodo=_data parametro="ToLongFunction<Map.Entry<K" %}
* **V&gt;&gt; transformer**,  {% include w3api/param_description.html metodo=_data parametro="V>> transformer" %}
* **long basis**,  {% include w3api/param_description.html metodo=_data parametro="long basis" %}
* **LongBinaryOperator reducer**,  {% include w3api/param_description.html metodo=_data parametro="LongBinaryOperator reducer" %}

## Clase Padre
[ConcurrentHashMap](/Java/ConcurrentHashMap/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ConcurrentHashMap.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
