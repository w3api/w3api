---
title: ConstructorDoc
permalink: /Java/ConstructorDoc/
date: 2021-01-11
key: Java.C.ConstructorDoc
category: Java
tags: ['java se', 'com.sun.javadoc', 'jdk.javadoc', 'interface java', 'Java 1.2']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.ConstructorDoc.description }}

## Sintaxis
~~~java
@Deprecated public interface ConstructorDoc extends ExecutableMemberDoc
~~~

## Ejemplo
~~~java
{{ site.data.Java.C.ConstructorDoc.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.C.ConstructorDoc.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
