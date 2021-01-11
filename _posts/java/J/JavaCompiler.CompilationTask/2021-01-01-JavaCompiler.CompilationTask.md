---
title: JavaCompiler.CompilationTask
permalink: Java/JavaCompiler/CompilationTask
date: 2021-01-11
key: JavaJava.J.JavaCompiler.CompilationTask
category: java
tags: ['java se', 'javax.tools', 'java.compiler', 'interface java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.J.JavaCompiler.CompilationTask.description }}

## Sintaxis
~~~java
public static interface JavaCompiler.CompilationTask extends Callable<Boolean>
~~~

## Métodos
* [addModules()](/Java/JavaCompiler/CompilationTask/addModules)
* [call()](/Java/JavaCompiler/CompilationTask/call)
* [setLocale()](/Java/JavaCompiler/CompilationTask/setLocale)
* [setProcessors()](/Java/JavaCompiler/CompilationTask/setProcessors)

## Ejemplo
~~~java
{{ site.data.Java.J.JavaCompiler.CompilationTask.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.J.JavaCompiler.CompilationTask.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
