---
title: TypeComponent
permalink: /Java/TypeComponent/
date: 2021-01-11
key: Java.T.TypeComponent
category: Java
tags: ['java se', 'com.sun.jdi', 'jdk.jdi', 'interface java', 'Java 1.3']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.T.TypeComponent.description }}

## Sintaxis
~~~java
public interface TypeComponent extends Mirror, Accessible
~~~

## Métodos
* [declaringType()](/Java/TypeComponent/declaringType)
* [genericSignature()](/Java/TypeComponent/genericSignature)
* [isFinal()](/Java/TypeComponent/isFinal)
* [isStatic()](/Java/TypeComponent/isStatic)
* [isSynthetic()](/Java/TypeComponent/isSynthetic)
* [name()](/Java/TypeComponent/name)
* [signature()](/Java/TypeComponent/signature)

## Ejemplo
~~~java
{{ site.data.Java.T.TypeComponent.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TypeComponent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
