---
title: IdentityHashMap.putAll()
permalink: Java/IdentityHashMap/putAll
date: 2021-01-04
key: JavaJava.I.IdentityHashMap
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IdentityHashMap.metodos valor="putAll" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void putAll(Map<? extends K,? extends V> m)
~~~

## Parámetros
* **? extends V&gt; m**,  {% include w3api/param_description.html metodo=_data parametro="? extends V> m" %}
* **Map&lt;? extends K**,  {% include w3api/param_description.html metodo=_data parametro="Map<? extends K" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[IdentityHashMap](/Java/IdentityHashMap/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.IdentityHashMap.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
