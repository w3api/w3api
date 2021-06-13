---
title: DocErrorReporter
permalink: /Java/DocErrorReporter/
date: 2021-01-11
key: Java.D.DocErrorReporter
category: Java
tags: ['java se', 'com.sun.javadoc', 'jdk.javadoc', 'interface java', 'Java 1.2']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.D.DocErrorReporter.description }}

## Sintaxis
~~~java
@Deprecated public interface DocErrorReporter
~~~

## Métodos
* [printError()](/Java/DocErrorReporter/printError)
* [printNotice()](/Java/DocErrorReporter/printNotice)
* [printWarning()](/Java/DocErrorReporter/printWarning)

## Ejemplo
~~~java
{{ site.data.Java.D.DocErrorReporter.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DocErrorReporter.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
