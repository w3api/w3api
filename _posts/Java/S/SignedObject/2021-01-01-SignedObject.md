---
title: SignedObject
permalink: /Java/SignedObject/
date: 2021-01-11
key: Java.S.SignedObject
category: Java
tags: ['java se', 'java.security', 'java.base', 'clase java', 'Java 1.2']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.SignedObject.description }}

## Sintaxis
~~~java
public final class SignedObject extends Object implements Serializable
~~~

## Constructores
* [SignedObject()](/Java/SignedObject/SignedObject/)

## Métodos
* [getAlgorithm()](/Java/SignedObject/getAlgorithm)
* [getObject()](/Java/SignedObject/getObject)
* [getSignature()](/Java/SignedObject/getSignature)
* [verify()](/Java/SignedObject/verify)

## Ejemplo
~~~java
{{ site.data.Java.S.SignedObject.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SignedObject.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
