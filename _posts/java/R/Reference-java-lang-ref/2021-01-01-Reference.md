---
title: Reference
permalink: Java/Reference-java-lang-ref
date: 2021-01-11
key: JavaJava.R.Reference-java-lang-ref
category: java
tags: ['java se', 'java.lang.ref', 'java.base', 'clase java', 'Java 1.2']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.R.Reference-java-lang-ref.description }}

## Sintaxis
~~~java
public abstract class Reference<T> extends Object
~~~

## Métodos
* [clear()](/Java/Reference-java-lang-ref/clear)
* [enqueue()](/Java/Reference-java-lang-ref/enqueue)
* [get()](/Java/Reference-java-lang-ref/get)
* [isEnqueued()](/Java/Reference-java-lang-ref/isEnqueued)
* [reachabilityFence()](/Java/Reference-java-lang-ref/reachabilityFence)

## Ejemplo
~~~java
{{ site.data.Java.R.Reference-java-lang-ref.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.Reference-java-lang-ref.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
