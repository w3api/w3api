---
title: MemoryPoolMXBean.setUsageThreshold()
permalink: /Java/MemoryPoolMXBean/setUsageThreshold/
date: 2021-01-11
key: Java.M.MemoryPoolMXBean
category: Java
tags: ['java se', 'java.lang.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MemoryPoolMXBean.metodos valor="setUsageThreshold" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setUsageThreshold(long threshold)
~~~

## Parámetros
* **long threshold**,  {% include w3api/param_description.html metodo=_dato parametro="long threshold" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[MemoryPoolMXBean](/Java/MemoryPoolMXBean/)

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
