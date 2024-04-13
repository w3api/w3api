---
title: CertificateRevokedException
permalink: /Java/CertificateRevokedException/
date: 2021-01-11
key: Java.C.CertificateRevokedException
category: Java
tags: ['java se', 'java.security.cert', 'java.base', 'clase java', 'Java 1.7']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.CertificateRevokedException.description }}

## Sintaxis
~~~java
public class CertificateRevokedException extends CertificateException
~~~

## Constructores
* [CertificateRevokedException()](/Java/CertificateRevokedException/CertificateRevokedException/)

## Métodos
* [getAuthorityName()](/Java/CertificateRevokedException/getAuthorityName/)
* [getExtensions()](/Java/CertificateRevokedException/getExtensions/)
* [getInvalidityDate()](/Java/CertificateRevokedException/getInvalidityDate/)
* [getRevocationDate()](/Java/CertificateRevokedException/getRevocationDate/)
* [getRevocationReason()](/Java/CertificateRevokedException/getRevocationReason/)

## Ejemplo
~~~java
{{ site.data.Java.C.CertificateRevokedException.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.C.CertificateRevokedException.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
