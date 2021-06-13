---
title: NavigableMap.subMap()
permalink: /Java/NavigableMap/subMap/
date: 2021-01-11
key: Java.N.NavigableMap
category: Java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.N.NavigableMap.metodos valor="subMap" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
NavigableMap<K,V> subMap(K fromKey, boolean fromInclusive, K toKey, boolean toInclusive)
SortedMap<K,V> subMap(K fromKey, K toKey)
~~~

## Parámetros
* **K fromKey**,  {% include w3api/param_description.html metodo=_dato parametro="K fromKey" %}
* **boolean fromInclusive**,  {% include w3api/param_description.html metodo=_dato parametro="boolean fromInclusive" %}
* **K toKey**,  {% include w3api/param_description.html metodo=_dato parametro="K toKey" %}
* **boolean toInclusive**,  {% include w3api/param_description.html metodo=_dato parametro="boolean toInclusive" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[NavigableMap](/Java/NavigableMap/)

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
