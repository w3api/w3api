---
title: LoaderDelegate
permalink: Java/LoaderDelegate
date: 2021-01-04
key: JavaJava.L.LoaderDelegate
category: java
tags: ['java se', 'jdk.jshell.execution', 'jdk.jshell', 'interface java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.L.LoaderDelegate.description }}

## Sintaxis
~~~java
public interface LoaderDelegate
~~~

## Métodos
* [addToClasspath()](/Java/LoaderDelegate/addToClasspath)
* [classesRedefined()](/Java/LoaderDelegate/classesRedefined)
* [findClass()](/Java/LoaderDelegate/findClass)
* [load()](/Java/LoaderDelegate/load)

## Ejemplo
~~~java
{{ site.data.Java.L.LoaderDelegate.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.L.LoaderDelegate.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
