---
title: LanguageVersion
permalink: Java/LanguageVersion
date: 2021-01-11
key: Java.L.LanguageVersion
category: java
tags: ['java se', 'com.sun.javadoc', 'jdk.javadoc', 'enumerado java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.L.LanguageVersion.description }}

## Sintaxis
~~~java
@Deprecated public enum LanguageVersion extends Enum<LanguageVersion>
~~~

## Enumerados
* [JAVA_1_1](/Java/LanguageVersion/JAVA_1_1)
* [JAVA_1_5](/Java/LanguageVersion/JAVA_1_5)

## Métodos
* [valueOf()](/Java/LanguageVersion/valueOf)
* [values()](/Java/LanguageVersion/values)

## Ejemplo
~~~java
{{ site.data.Java.L.LanguageVersion.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.L.LanguageVersion.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
