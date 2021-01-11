---
title: ConcurrentHashMap.reduceValuesToLong()
permalink: Java/ConcurrentHashMap/reduceValuesToLong
date: 2021-01-11
key: JavaJava.C.ConcurrentHashMap
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConcurrentHashMap.metodos valor="reduceValuesToLong" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public long reduceValuesToLong(long parallelismThreshold, ToLongFunction<? super V> transformer, long basis, LongBinaryOperator reducer)
~~~

## Parámetros
* **long basis**,  {% include w3api/param_description.html metodo=_dato parametro="long basis" %}
* **ToLongFunction&lt;? super V&gt; transformer**,  {% include w3api/param_description.html metodo=_dato parametro="ToLongFunction<? super V> transformer" %}
* **LongBinaryOperator reducer**,  {% include w3api/param_description.html metodo=_dato parametro="LongBinaryOperator reducer" %}
* **long parallelismThreshold**,  {% include w3api/param_description.html metodo=_dato parametro="long parallelismThreshold" %}

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
