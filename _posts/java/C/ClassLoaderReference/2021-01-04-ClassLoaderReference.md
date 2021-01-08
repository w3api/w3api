---
title: ClassLoaderReference
permalink: Java/ClassLoaderReference
date: 2021-01-04
key: JavaJava.C.ClassLoaderReference
category: java
tags: ['java se', 'com.sun.jdi', 'jdk.jdi', 'interface java', 'Java 1.3']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.ClassLoaderReference.description }}

## Sintaxis
~~~java
public interface ClassLoaderReference extends ObjectReference
~~~

## Métodos
* [definedClasses()](/Java/ClassLoaderReference/definedClasses)
* [visibleClasses()](/Java/ClassLoaderReference/visibleClasses)

## Ejemplo
~~~java
{{ site.data.Java.C.ClassLoaderReference.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ClassLoaderReference.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
