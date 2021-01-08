---
title: DocCommentTree
permalink: Java/DocCommentTree
date: 2021-01-04
key: JavaJava.D.DocCommentTree
category: java
tags: ['java se', 'com.sun.source.doctree', 'jdk.compiler', 'interface java', 'Java 1.8']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.D.DocCommentTree.description }}

## Sintaxis
~~~java
public interface DocCommentTree extends DocTree
~~~

## Métodos
* [getBlockTags()](/Java/DocCommentTree/getBlockTags)
* [getBody()](/Java/DocCommentTree/getBody)
* [getFirstSentence()](/Java/DocCommentTree/getFirstSentence)
* [getFullBody()](/Java/DocCommentTree/getFullBody)
* [getPostamble()](/Java/DocCommentTree/getPostamble)
* [getPreamble()](/Java/DocCommentTree/getPreamble)

## Ejemplo
~~~java
{{ site.data.Java.D.DocCommentTree.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DocCommentTree.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
