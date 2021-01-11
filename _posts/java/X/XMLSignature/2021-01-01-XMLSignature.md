---
title: XMLSignature
permalink: Java/XMLSignature
date: 2021-01-11
key: JavaJava.X.XMLSignature
category: java
tags: ['java se', 'javax.xml.crypto.dsig', 'java.xml.crypto', 'interface java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.X.XMLSignature.description }}

## Sintaxis
~~~java
public interface XMLSignature extends XMLStructure
~~~

## Campos
* [XMLNS](/Java/XMLSignature/XMLNS)

## Métodos
* [getId()](/Java/XMLSignature/getId)
* [getKeyInfo()](/Java/XMLSignature/getKeyInfo)
* [getKeySelectorResult()](/Java/XMLSignature/getKeySelectorResult)
* [getObjects()](/Java/XMLSignature/getObjects)
* [getSignatureValue()](/Java/XMLSignature/getSignatureValue)
* [getSignedInfo()](/Java/XMLSignature/getSignedInfo)
* [sign()](/Java/XMLSignature/sign)
* [validate()](/Java/XMLSignature/validate)

## Ejemplo
~~~java
{{ site.data.Java.X.XMLSignature.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.X.XMLSignature.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
