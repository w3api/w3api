---
title: AuthorTree
permalink: Java/AuthorTree
date: 2021-01-04
key: JavaJava.A.AuthorTree
category: java
tags: ['java se', 'com.sun.source.doctree', 'jdk.compiler', 'interface java', 'Java 1.8']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.A.AuthorTree.description }}

## Sintaxis
~~~java
public interface AuthorTree extends BlockTagTree
~~~

## Métodos
* [getName()](/Java/AuthorTree/getName)

## Ejemplo
~~~java
{{ site.data.Java.A.AuthorTree.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AuthorTree.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
