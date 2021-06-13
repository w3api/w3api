---
title: MemoryAddress
permalink: /Java/MemoryAddress/
date: 2021-01-11
key: Java.M.MemoryAddress
category: Java
tags: ['java se', 'jdk.jfr', 'jdk.jfr', 'anotacion java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.M.MemoryAddress.description }}

## Sintaxis
~~~java
@Retention(RUNTIME) @Target({FIELD,TYPE,METHOD}) public @interface MemoryAddress
~~~

## Ejemplo
~~~java
{{ site.data.Java.M.MemoryAddress.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MemoryAddress.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
