---
title: ReferenceTree
permalink: Java/ReferenceTree
date: 2021-01-11
key: Java.R.ReferenceTree
category: java
tags: ['java se', 'com.sun.source.doctree', 'jdk.compiler', 'interface java', 'Java 1.8']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.R.ReferenceTree.description }}

## Sintaxis
~~~java
public interface ReferenceTree extends DocTree
~~~

## Métodos
* [getSignature()](/Java/ReferenceTree/getSignature)

## Ejemplo
~~~java
{{ site.data.Java.R.ReferenceTree.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.ReferenceTree.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
