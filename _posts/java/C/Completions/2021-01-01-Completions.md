---
title: Completions
permalink: /Java/Completions/
date: 2021-01-11
key: Java.C.Completions
category: Java
tags: ['java se', 'javax.annotation.processing', 'java.compiler', 'clase java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.Completions.description }}

## Sintaxis
~~~java
public class Completions extends Object
~~~

## Métodos
* [of()](/Java/Completions/of)

## Ejemplo
~~~java
{{ site.data.Java.C.Completions.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.C.Completions.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
