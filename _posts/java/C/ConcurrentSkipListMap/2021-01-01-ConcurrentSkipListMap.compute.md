---
title: ConcurrentSkipListMap.compute()
permalink: Java/ConcurrentSkipListMap/compute
date: 2021-01-11
key: JavaJava.C.ConcurrentSkipListMap
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConcurrentSkipListMap.metodos valor="compute" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public V compute(K key, BiFunction<? super K,? super V,? extends V> remappingFunction)
~~~

## Parámetros
* **BiFunction&lt;? super K**,  {% include w3api/param_description.html metodo=_dato parametro="BiFunction<? super K" %}
* **K key**,  {% include w3api/param_description.html metodo=_dato parametro="K key" %}
* **? extends V&gt; remappingFunction**,  {% include w3api/param_description.html metodo=_dato parametro="? extends V> remappingFunction" %}
* **? super V**,  {% include w3api/param_description.html metodo=_dato parametro="? super V" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>