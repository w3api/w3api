---
title: ConcurrentHashMap.computeIfAbsent()
permalink: /Java/ConcurrentHashMap/computeIfAbsent/
date: 2021-01-11
key: Java.C.ConcurrentHashMap
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConcurrentHashMap.metodos valor="computeIfAbsent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public V computeIfAbsent(K key, Function<? super K,? extends V> mappingFunction)
~~~

## Parámetros
* **? extends V&gt; mappingFunction**,  {% include w3api/param_description.html metodo=_dato parametro="? extends V> mappingFunction" %}
* **K key**,  {% include w3api/param_description.html metodo=_dato parametro="K key" %}
* **Function&lt;? super K**,  {% include w3api/param_description.html metodo=_dato parametro="Function<? super K" %}

## Excepciones
[RuntimeException](/Java/RuntimeException/), [IllegalStateException](/Java/IllegalStateException/), [NullPointerException](/Java/NullPointerException/)

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
