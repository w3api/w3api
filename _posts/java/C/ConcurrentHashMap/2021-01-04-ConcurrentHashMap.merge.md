---
title: ConcurrentHashMap.merge()
permalink: Java/ConcurrentHashMap/merge
date: 2021-01-04
key: JavaJava.C.ConcurrentHashMap
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConcurrentHashMap.metodos valor="merge" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public V merge(K key, V value, BiFunction<? super V,? super V,? extends V> remappingFunction)
~~~

## Parámetros
* **V value**,  {% include w3api/param_description.html metodo=_data parametro="V value" %}
* **BiFunction&lt;? super V**,  {% include w3api/param_description.html metodo=_data parametro="BiFunction<? super V" %}
* **? super V**,  {% include w3api/param_description.html metodo=_data parametro="? super V" %}
* **? extends V&gt; remappingFunction**,  {% include w3api/param_description.html metodo=_data parametro="? extends V> remappingFunction" %}
* **K key**,  {% include w3api/param_description.html metodo=_data parametro="K key" %}

## Excepciones
[RuntimeException](/Java/RuntimeException/), [NullPointerException](/Java/NullPointerException/)

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
