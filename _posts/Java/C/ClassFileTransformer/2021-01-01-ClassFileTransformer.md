---
title: ClassFileTransformer
permalink: /Java/ClassFileTransformer/
date: 2021-01-11
key: Java.C.ClassFileTransformer
category: Java
tags: ['java se', 'java.lang.instrument', 'java.instrument', 'interface java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.ClassFileTransformer.description }}

## Sintaxis
~~~java
public interface ClassFileTransformer
~~~

## Métodos
* [transform()](/Java/ClassFileTransformer/transform/)

## Ejemplo
~~~java
{{ site.data.Java.C.ClassFileTransformer.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.C.ClassFileTransformer.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
