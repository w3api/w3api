---
title: DiagnosticCollector
permalink: /Java/DiagnosticCollector/
date: 2021-01-11
key: Java.D.DiagnosticCollector
category: Java
tags: ['java se', 'javax.tools', 'java.compiler', 'clase java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.D.DiagnosticCollector.description }}

## Sintaxis
~~~java
public final class DiagnosticCollector<S> extends Object implements DiagnosticListener<S>
~~~

## Constructores
* [DiagnosticCollector()](/Java/DiagnosticCollector/DiagnosticCollector/)

## Métodos
* [getDiagnostics()](/Java/DiagnosticCollector/getDiagnostics)

## Ejemplo
~~~java
{{ site.data.Java.D.DiagnosticCollector.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DiagnosticCollector.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
