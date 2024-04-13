---
title: ConcurrentHashMap.computeIfPresent()
permalink: /Java/ConcurrentHashMap/computeIfPresent/
date: 2021-01-11
key: Java.C.ConcurrentHashMap
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConcurrentHashMap.metodos valor="computeIfPresent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public V computeIfPresent(K key, BiFunction<? super K,? super V,? extends V> remappingFunction)
~~~

## Parámetros
* **BiFunction&lt;? super K**,  {% include w3api/param_description.html metodo=_dato parametro="BiFunction<? super K" %}
* **K key**,  {% include w3api/param_description.html metodo=_dato parametro="K key" %}
* **? extends V&gt; remappingFunction**,  {% include w3api/param_description.html metodo=_dato parametro="? extends V> remappingFunction" %}
* **? super V**,  {% include w3api/param_description.html metodo=_dato parametro="? super V" %}

## Excepciones
[RuntimeException](/Java/RuntimeException/), [IllegalStateException](/Java/IllegalStateException/), [NullPointerException](/Java/NullPointerException/)

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
