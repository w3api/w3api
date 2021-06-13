---
title: ConcurrentMap.merge()
permalink: /Java/ConcurrentMap/merge/
date: 2021-01-11
key: Java.C.ConcurrentMap
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConcurrentMap.metodos valor="merge" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default V merge(K key, V value, BiFunction<? super V,? super V,? extends V> remappingFunction)
~~~

## Parámetros
* **? super V**,  {% include w3api/param_description.html metodo=_dato parametro="? super V" %}
* **V value**,  {% include w3api/param_description.html metodo=_dato parametro="V value" %}
* **? extends V&gt; remappingFunction**,  {% include w3api/param_description.html metodo=_dato parametro="? extends V> remappingFunction" %}
* **K key**,  {% include w3api/param_description.html metodo=_dato parametro="K key" %}
* **BiFunction&lt;? super V**,  {% include w3api/param_description.html metodo=_dato parametro="BiFunction<? super V" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/), [ClassCastException](/Java/ClassCastException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[ConcurrentMap](/Java/ConcurrentMap/)

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
