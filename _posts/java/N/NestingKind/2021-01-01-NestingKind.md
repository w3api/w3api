---
title: NestingKind
permalink: Java/NestingKind
date: 2021-01-11
key: JavaJava.N.NestingKind
category: java
tags: ['java se', 'javax.lang.model.element', 'java.compiler', 'enumerado java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.N.NestingKind.description }}

## Sintaxis
~~~java
public enum NestingKind extends Enum<NestingKind>
~~~

## Enumerados
* [ANONYMOUS](/Java/NestingKind/ANONYMOUS)
* [LOCAL](/Java/NestingKind/LOCAL)
* [MEMBER](/Java/NestingKind/MEMBER)
* [TOP_LEVEL](/Java/NestingKind/TOP_LEVEL)

## Métodos
* [isNested()](/Java/NestingKind/isNested)
* [valueOf()](/Java/NestingKind/valueOf)
* [values()](/Java/NestingKind/values)

## Ejemplo
~~~java
{{ site.data.Java.N.NestingKind.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.N.NestingKind.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
