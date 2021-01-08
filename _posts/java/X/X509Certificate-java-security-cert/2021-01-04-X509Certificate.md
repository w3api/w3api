---
title: X509Certificate
permalink: Java/X509Certificate-java-security-cert
date: 2021-01-04
key: JavaJava.X.X509Certificate-java-security-cert
category: java
tags: ['java se', 'java.security.cert', 'java.base', 'clase java', 'Java 1.2']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.X.X509Certificate-java-security-cert.description }}

## Sintaxis
~~~java
public abstract class X509Certificate extends Certificate implements X509Extension
~~~

## Constructores
* [X509Certificate()](/Java/X509Certificate-java-security-cert/X509Certificate/)

## Métodos
* [checkValidity()](/Java/X509Certificate-java-security-cert/checkValidity)
* [getBasicConstraints()](/Java/X509Certificate-java-security-cert/getBasicConstraints)
* [getExtendedKeyUsage()](/Java/X509Certificate-java-security-cert/getExtendedKeyUsage)
* [getIssuerAlternativeNames()](/Java/X509Certificate-java-security-cert/getIssuerAlternativeNames)
* [getIssuerDN()](/Java/X509Certificate-java-security-cert/getIssuerDN)
* [getIssuerUniqueID()](/Java/X509Certificate-java-security-cert/getIssuerUniqueID)
* [getIssuerX500Principal()](/Java/X509Certificate-java-security-cert/getIssuerX500Principal)
* [getKeyUsage()](/Java/X509Certificate-java-security-cert/getKeyUsage)
* [getNotAfter()](/Java/X509Certificate-java-security-cert/getNotAfter)
* [getNotBefore()](/Java/X509Certificate-java-security-cert/getNotBefore)
* [getSerialNumber()](/Java/X509Certificate-java-security-cert/getSerialNumber)
* [getSigAlgName()](/Java/X509Certificate-java-security-cert/getSigAlgName)
* [getSigAlgOID()](/Java/X509Certificate-java-security-cert/getSigAlgOID)
* [getSigAlgParams()](/Java/X509Certificate-java-security-cert/getSigAlgParams)
* [getSignature()](/Java/X509Certificate-java-security-cert/getSignature)
* [getSubjectAlternativeNames()](/Java/X509Certificate-java-security-cert/getSubjectAlternativeNames)
* [getSubjectDN()](/Java/X509Certificate-java-security-cert/getSubjectDN)
* [getSubjectUniqueID()](/Java/X509Certificate-java-security-cert/getSubjectUniqueID)
* [getSubjectX500Principal()](/Java/X509Certificate-java-security-cert/getSubjectX500Principal)
* [getTBSCertificate()](/Java/X509Certificate-java-security-cert/getTBSCertificate)
* [getVersion()](/Java/X509Certificate-java-security-cert/getVersion)
* [verify()](/Java/X509Certificate-java-security-cert/verify)

## Ejemplo
~~~java
{{ site.data.Java.X.X509Certificate-java-security-cert.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.X.X509Certificate-java-security-cert.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
