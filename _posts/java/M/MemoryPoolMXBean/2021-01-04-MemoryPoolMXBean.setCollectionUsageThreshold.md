---
title: MemoryPoolMXBean.setCollectionUsageThreshold()
permalink: Java/MemoryPoolMXBean/setCollectionUsageThreshold
date: 2021-01-04
key: JavaJava.M.MemoryPoolMXBean
category: java
tags: ['java se', 'java.lang.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MemoryPoolMXBean.metodos valor="setCollectionUsageThreshold" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setCollectionUsageThreshold(long threshold)
~~~

## Parámetros
* **long threshold**,  {% include w3api/param_description.html metodo=_data parametro="long threshold" %}

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/), [SecurityException](/Java/SecurityException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[MemoryPoolMXBean](/Java/MemoryPoolMXBean/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MemoryPoolMXBean.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
