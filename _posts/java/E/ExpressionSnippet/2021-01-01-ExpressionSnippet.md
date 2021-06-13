---
title: ExpressionSnippet
permalink: /Java/ExpressionSnippet/
date: 2021-01-11
key: Java.E.ExpressionSnippet
category: Java
tags: ['java se', 'jdk.jshell', 'jdk.jshell', 'clase java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.E.ExpressionSnippet.description }}

## Sintaxis
~~~java
public class ExpressionSnippet extends Snippet
~~~

## Métodos
* [name()](/Java/ExpressionSnippet/name)
* [typeName()](/Java/ExpressionSnippet/typeName)

## Ejemplo
~~~java
{{ site.data.Java.E.ExpressionSnippet.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.E.ExpressionSnippet.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
