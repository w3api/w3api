---
title: ConcurrentSkipListMap.computeIfAbsent()
permalink: Java/ConcurrentSkipListMap/computeIfAbsent
date: 2021-01-04
key: JavaJava.C.ConcurrentSkipListMap
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConcurrentSkipListMap.metodos valor="computeIfAbsent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public V computeIfAbsent(K key, Function<? super K,? extends V> mappingFunction)
~~~

## Parámetros
* **? extends V&gt; mappingFunction**,  {% include w3api/param_description.html metodo=_data parametro="? extends V> mappingFunction" %}
* **Function&lt;? super K**,  {% include w3api/param_description.html metodo=_data parametro="Function<? super K" %}
* **K key**,  {% include w3api/param_description.html metodo=_data parametro="K key" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

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
