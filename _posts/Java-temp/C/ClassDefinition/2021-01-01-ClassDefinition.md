---
title: ClassDefinition
permalink: /Java/ClassDefinition/
date: 2021-01-11
key: Java.C.ClassDefinition
category: Java
tags: ['java se', 'java.lang.instrument', 'java.instrument', 'clase java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.ClassDefinition.description }}

## Sintaxis
~~~java
public final class ClassDefinition extends Object
~~~

## Constructores
* [ClassDefinition()](/Java/ClassDefinition/ClassDefinition/)

## Métodos
* [getDefinitionClass()](/Java/ClassDefinition/getDefinitionClass)
* [getDefinitionClassFile()](/Java/ClassDefinition/getDefinitionClassFile)

## Ejemplo
~~~java
{{ site.data.Java.C.ClassDefinition.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.C.ClassDefinition.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
