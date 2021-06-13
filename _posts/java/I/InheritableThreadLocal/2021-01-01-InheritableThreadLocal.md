---
title: InheritableThreadLocal
permalink: /Java/InheritableThreadLocal/
date: 2021-01-11
key: Java.I.InheritableThreadLocal
category: Java
tags: ['java se', 'java.lang', 'java.base', 'clase java', 'Java 1.2']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.I.InheritableThreadLocal.description }}

## Sintaxis
~~~java
public class InheritableThreadLocal<T> extends ThreadLocal<T>
~~~

## Constructores
* [InheritableThreadLocal()](/Java/InheritableThreadLocal/InheritableThreadLocal/)

## Métodos
* [childValue()](/Java/InheritableThreadLocal/childValue)

## Ejemplo
~~~java
{{ site.data.Java.I.InheritableThreadLocal.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.InheritableThreadLocal.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
