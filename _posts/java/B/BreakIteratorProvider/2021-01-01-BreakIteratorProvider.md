---
title: BreakIteratorProvider
permalink: /Java/BreakIteratorProvider/
date: 2021-01-11
key: JavaJava.B.BreakIteratorProvider
category: java
tags: ['java se', 'java.text.spi', 'java.base', 'clase java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.B.BreakIteratorProvider.description }}

## Sintaxis
~~~java
public abstract class BreakIteratorProvider extends LocaleServiceProvider
~~~

## Constructores
* [BreakIteratorProvider()](/Java/BreakIteratorProvider/BreakIteratorProvider/)

## Métodos
* [getCharacterInstance()](/Java/BreakIteratorProvider/getCharacterInstance)
* [getLineInstance()](/Java/BreakIteratorProvider/getLineInstance)
* [getSentenceInstance()](/Java/BreakIteratorProvider/getSentenceInstance)
* [getWordInstance()](/Java/BreakIteratorProvider/getWordInstance)

## Ejemplo
~~~java
{{ site.data.Java.B.BreakIteratorProvider.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.BreakIteratorProvider.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
