---
title: SourceVersion
permalink: Java/SourceVersion
date: 2021-01-04
key: JavaJava.S.SourceVersion
category: java
tags: ['java se', 'javax.lang.model', 'java.compiler', 'enumerado java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.SourceVersion.description }}

## Sintaxis
~~~java
public enum SourceVersion extends Enum<SourceVersion>
~~~

## Enumerados
* [RELEASE_0](/Java/SourceVersion/RELEASE_0)
* [RELEASE_1](/Java/SourceVersion/RELEASE_1)
* [RELEASE_10](/Java/SourceVersion/RELEASE_10)
* [RELEASE_2](/Java/SourceVersion/RELEASE_2)
* [RELEASE_3](/Java/SourceVersion/RELEASE_3)
* [RELEASE_4](/Java/SourceVersion/RELEASE_4)
* [RELEASE_5](/Java/SourceVersion/RELEASE_5)
* [RELEASE_6](/Java/SourceVersion/RELEASE_6)
* [RELEASE_7](/Java/SourceVersion/RELEASE_7)
* [RELEASE_8](/Java/SourceVersion/RELEASE_8)
* [RELEASE_9](/Java/SourceVersion/RELEASE_9)

## Métodos
* [isIdentifier()](/Java/SourceVersion/isIdentifier)
* [isKeyword()](/Java/SourceVersion/isKeyword)
* [isName()](/Java/SourceVersion/isName)
* [latest()](/Java/SourceVersion/latest)
* [latestSupported()](/Java/SourceVersion/latestSupported)
* [valueOf()](/Java/SourceVersion/valueOf)
* [values()](/Java/SourceVersion/values)

## Ejemplo
~~~java
{{ site.data.Java.S.SourceVersion.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SourceVersion.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
