---
title: InheritDocTree
permalink: /Java/InheritDocTree/
date: 2021-01-11
key: Java.I.InheritDocTree
category: Java
tags: ['java se', 'com.sun.source.doctree', 'jdk.compiler', 'interface java', 'Java 1.8']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.I.InheritDocTree.description }}

## Sintaxis
~~~java
public interface InheritDocTree extends InlineTagTree
~~~

## Ejemplo
~~~java
{{ site.data.Java.I.InheritDocTree.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.I.InheritDocTree.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
