---
title: MemberDoc
permalink: Java/MemberDoc
date: 2021-01-04
key: JavaJava.M.MemberDoc
category: java
tags: ['java se', 'com.sun.javadoc', 'jdk.javadoc', 'interface java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.M.MemberDoc.description }}

## Sintaxis
~~~java
@Deprecated public interface MemberDoc extends ProgramElementDoc
~~~

## Métodos
* [isSynthetic()](/Java/MemberDoc/isSynthetic)

## Ejemplo
~~~java
{{ site.data.Java.M.MemberDoc.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MemberDoc.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
