---
title: AbstractMap.putAll()
permalink: Java/AbstractMap/putAll
date: 2021-01-10
key: JavaJava.A.AbstractMap
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractMap.metodos valor="putAll" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void putAll(Map<? extends K,? extends V> m)
~~~

## Parámetros
* **? extends V&gt; m**,  {% include w3api/param_description.html metodo=_dato parametro="? extends V> m" %}
* **Map&lt;? extends K**,  {% include w3api/param_description.html metodo=_dato parametro="Map<? extends K" %}

## Excepciones
[ClassCastException](/Java/ClassCastException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[AbstractMap](/Java/AbstractMap/)

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
