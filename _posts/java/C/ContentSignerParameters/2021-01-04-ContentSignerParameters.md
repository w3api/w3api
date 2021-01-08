---
title: ContentSignerParameters
permalink: Java/ContentSignerParameters
date: 2021-01-04
key: JavaJava.C.ContentSignerParameters
category: java
tags: ['java se', 'com.sun.jarsigner', 'jdk.jartool', 'interface java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.ContentSignerParameters.description }}

## Sintaxis
~~~java
@Deprecated(since="9") public interface ContentSignerParameters
~~~

## Métodos
* [getCommandLine()](/Java/ContentSignerParameters/getCommandLine)
* [getContent()](/Java/ContentSignerParameters/getContent)
* [getSignature()](/Java/ContentSignerParameters/getSignature)
* [getSignatureAlgorithm()](/Java/ContentSignerParameters/getSignatureAlgorithm)
* [getSignerCertificateChain()](/Java/ContentSignerParameters/getSignerCertificateChain)
* [getSource()](/Java/ContentSignerParameters/getSource)
* [getTimestampingAuthority()](/Java/ContentSignerParameters/getTimestampingAuthority)
* [getTimestampingAuthorityCertificate()](/Java/ContentSignerParameters/getTimestampingAuthorityCertificate)
* [getTSADigestAlg()](/Java/ContentSignerParameters/getTSADigestAlg)
* [getTSAPolicyID()](/Java/ContentSignerParameters/getTSAPolicyID)

## Ejemplo
~~~java
{{ site.data.Java.C.ContentSignerParameters.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ContentSignerParameters.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
