---
title: SignedInfo
permalink: /Java/SignedInfo/
date: 2021-01-11
key: Java.S.SignedInfo
category: Java
tags: ['java se', 'javax.xml.crypto.dsig', 'java.xml.crypto', 'interface java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.SignedInfo.description }}

## Sintaxis
~~~java
public interface SignedInfo extends XMLStructure
~~~

## Métodos
* [getCanonicalizationMethod()](/Java/SignedInfo/getCanonicalizationMethod)
* [getCanonicalizedData()](/Java/SignedInfo/getCanonicalizedData)
* [getId()](/Java/SignedInfo/getId)
* [getReferences()](/Java/SignedInfo/getReferences)
* [getSignatureMethod()](/Java/SignedInfo/getSignatureMethod)

## Ejemplo
~~~java
{{ site.data.Java.S.SignedInfo.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SignedInfo.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
