---
title: InlineTagTree
permalink: /Java/InlineTagTree/
date: 2021-01-11
key: Java.I.InlineTagTree
category: Java
tags: ['java se', 'com.sun.source.doctree', 'jdk.compiler', 'interface java', 'Java 1.8']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.I.InlineTagTree.description }}

## Sintaxis
~~~java
public interface InlineTagTree extends DocTree
~~~

## Métodos
* [getTagName()](/Java/InlineTagTree/getTagName/)

## Ejemplo
~~~java
{{ site.data.Java.I.InlineTagTree.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.I.InlineTagTree.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
