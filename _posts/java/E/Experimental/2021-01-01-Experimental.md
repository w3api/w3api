---
title: Experimental
permalink: Java/Experimental
date: 2021-01-11
key: JavaJava.E.Experimental
category: java
tags: ['java se', 'jdk.jfr', 'jdk.jfr', 'anotacion java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.E.Experimental.description }}

## Sintaxis
~~~java
@Inherited @Retention(RUNTIME) @Target({FIELD,TYPE}) public @interface Experimental
~~~

## Ejemplo
~~~java
{{ site.data.Java.E.Experimental.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.E.Experimental.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
