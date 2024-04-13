---
title: PhantomReference
permalink: /Java/PhantomReference/
date: 2021-01-11
key: Java.P.PhantomReference
category: Java
tags: ['java se', 'java.lang.ref', 'java.base', 'clase java', 'Java 1.2']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.P.PhantomReference.description }}

## Sintaxis
~~~java
public class PhantomReference<T> extends Reference<T>
~~~

## Constructores
* [PhantomReference()](/Java/PhantomReference/PhantomReference/)

## Métodos
* [get()](/Java/PhantomReference/get/)

## Ejemplo
~~~java
{{ site.data.Java.P.PhantomReference.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.P.PhantomReference.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
