---
title: CanonicalizationMethod
permalink: /Java/CanonicalizationMethod/
date: 2021-01-11
key: Java.C.CanonicalizationMethod
category: Java
tags: ['java se', 'javax.xml.crypto.dsig', 'java.xml.crypto', 'interface java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.CanonicalizationMethod.description }}

## Sintaxis
~~~java
public interface CanonicalizationMethod extends Transform
~~~

## Campos
* [EXCLUSIVE](/Java/CanonicalizationMethod/EXCLUSIVE)
* [EXCLUSIVE_WITH_COMMENTS](/Java/CanonicalizationMethod/EXCLUSIVE_WITH_COMMENTS)
* [INCLUSIVE](/Java/CanonicalizationMethod/INCLUSIVE)
* [INCLUSIVE_WITH_COMMENTS](/Java/CanonicalizationMethod/INCLUSIVE_WITH_COMMENTS)

## Métodos
* [getParameterSpec()](/Java/CanonicalizationMethod/getParameterSpec)

## Ejemplo
~~~java
{{ site.data.Java.C.CanonicalizationMethod.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.C.CanonicalizationMethod.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
