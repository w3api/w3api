---
title: ConcurrentNavigableMap.subMap()
permalink: Java/ConcurrentNavigableMap/subMap
date: 2021-01-04
key: JavaJava.C.ConcurrentNavigableMap
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConcurrentNavigableMap.metodos valor="subMap" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
ConcurrentNavigableMap<K,V> subMap(K fromKey, boolean fromInclusive, K toKey, boolean toInclusive)
ConcurrentNavigableMap<K,V> subMap(K fromKey, K toKey)
~~~

## Parámetros
* **boolean fromInclusive**,  {% include w3api/param_description.html metodo=_data parametro="boolean fromInclusive" %}
* **K fromKey**,  {% include w3api/param_description.html metodo=_data parametro="K fromKey" %}
* **boolean toInclusive**,  {% include w3api/param_description.html metodo=_data parametro="boolean toInclusive" %}
* **K toKey**,  {% include w3api/param_description.html metodo=_data parametro="K toKey" %}

## Excepciones
[ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ConcurrentNavigableMap](/Java/ConcurrentNavigableMap/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ConcurrentNavigableMap.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
