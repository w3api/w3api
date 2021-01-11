---
title: StackWalker
permalink: Java/StackWalker
date: 2021-01-11
key: JavaJava.S.StackWalker
category: java
tags: ['java se', 'java.lang', 'java.base', 'clase java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.StackWalker.description }}

## Sintaxis
~~~java
public final class StackWalker extends Object
~~~

## Métodos
* [forEach()](/Java/StackWalker/forEach)
* [getCallerClass()](/Java/StackWalker/getCallerClass)
* [getInstance()](/Java/StackWalker/getInstance)
* [walk()](/Java/StackWalker/walk)

## Ejemplo
~~~java
{{ site.data.Java.S.StackWalker.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.StackWalker.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
