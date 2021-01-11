---
title: RecursiveAction
permalink: Java/RecursiveAction
date: 2021-01-11
key: JavaJava.R.RecursiveAction
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'clase java', 'Java 1.7']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.R.RecursiveAction.description }}

## Sintaxis
~~~java
public abstract class RecursiveAction extends ForkJoinTask<Void>
~~~

## Constructores
* [RecursiveAction()](/Java/RecursiveAction/RecursiveAction/)

## Métodos
* [compute()](/Java/RecursiveAction/compute)
* [exec()](/Java/RecursiveAction/exec)
* [getRawResult()](/Java/RecursiveAction/getRawResult)
* [setRawResult()](/Java/RecursiveAction/setRawResult)

## Ejemplo
~~~java
{{ site.data.Java.R.RecursiveAction.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.RecursiveAction.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
