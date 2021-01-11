---
title: ConcurrentHashMap.reduceKeysToLong()
permalink: Java/ConcurrentHashMap/reduceKeysToLong
date: 2021-01-11
key: JavaJava.C.ConcurrentHashMap
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConcurrentHashMap.metodos valor="reduceKeysToLong" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public long reduceKeysToLong(long parallelismThreshold, ToLongFunction<? super K> transformer, long basis, LongBinaryOperator reducer)
~~~

## Parámetros
* **long basis**,  {% include w3api/param_description.html metodo=_dato parametro="long basis" %}
* **ToLongFunction&lt;? super K&gt; transformer**,  {% include w3api/param_description.html metodo=_dato parametro="ToLongFunction<? super K> transformer" %}
* **long parallelismThreshold**,  {% include w3api/param_description.html metodo=_dato parametro="long parallelismThreshold" %}
* **LongBinaryOperator reducer**,  {% include w3api/param_description.html metodo=_dato parametro="LongBinaryOperator reducer" %}

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
