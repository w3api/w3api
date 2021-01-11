---
title: Hashtable.compute()
permalink: Java/Hashtable/compute
date: 2021-01-11
key: JavaJava.H.Hashtable
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.Hashtable.metodos valor="compute" %}

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
[ConcurrentModificationException](/Java/ConcurrentModificationException/)

## Clase Padre
[Hashtable](/Java/Hashtable/)

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
