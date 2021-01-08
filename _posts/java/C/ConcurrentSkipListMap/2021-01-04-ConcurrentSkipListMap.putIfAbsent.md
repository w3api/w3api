---
title: ConcurrentSkipListMap.putIfAbsent()
permalink: Java/ConcurrentSkipListMap/putIfAbsent
date: 2021-01-04
key: JavaJava.C.ConcurrentSkipListMap
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConcurrentSkipListMap.metodos valor="putIfAbsent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public V putIfAbsent(K key, V value)
~~~

## Parámetros
* **V value**,  {% include w3api/param_description.html metodo=_data parametro="V value" %}
* **K key**,  {% include w3api/param_description.html metodo=_data parametro="K key" %}

## Excepciones
[ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ConcurrentSkipListMap](/Java/ConcurrentSkipListMap/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ConcurrentSkipListMap.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
