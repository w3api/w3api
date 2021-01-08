---
title: BooleanFlag
permalink: Java/BooleanFlag
date: 2021-01-04
key: JavaJava.B.BooleanFlag
category: java
tags: ['java se', 'jdk.jfr', 'jdk.jfr', 'anotacion java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.B.BooleanFlag.description }}

## Sintaxis
~~~java
@Retention(RUNTIME) @Target({FIELD,TYPE,METHOD}) public @interface BooleanFlag
~~~

## Ejemplo
~~~java
{{ site.data.Java.B.BooleanFlag.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.BooleanFlag.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
