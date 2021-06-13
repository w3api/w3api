---
title: Diagnostic
permalink: /Java/Diagnostic-javax-tools/
date: 2021-01-11
key: Java.D.Diagnostic-javax-tools
category: Java
tags: ['java se', 'javax.tools', 'java.compiler', 'interface java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.D.Diagnostic-javax-tools.description }}

## Sintaxis
~~~java
public interface Diagnostic<S>
~~~

## Campos
* [NOPOS](/Java/Diagnostic-javax-tools/NOPOS)

## Métodos
* [getCode()](/Java/Diagnostic-javax-tools/getCode)
* [getColumnNumber()](/Java/Diagnostic-javax-tools/getColumnNumber)
* [getEndPosition()](/Java/Diagnostic-javax-tools/getEndPosition)
* [getKind()](/Java/Diagnostic-javax-tools/getKind)
* [getLineNumber()](/Java/Diagnostic-javax-tools/getLineNumber)
* [getMessage()](/Java/Diagnostic-javax-tools/getMessage)
* [getPosition()](/Java/Diagnostic-javax-tools/getPosition)
* [getSource()](/Java/Diagnostic-javax-tools/getSource)
* [getStartPosition()](/Java/Diagnostic-javax-tools/getStartPosition)

## Ejemplo
~~~java
{{ site.data.Java.D.Diagnostic-javax-tools.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.Diagnostic-javax-tools.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
