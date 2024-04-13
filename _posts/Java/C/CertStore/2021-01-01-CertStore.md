---
title: CertStore
permalink: /Java/CertStore/
date: 2021-01-11
key: Java.C.CertStore
category: Java
tags: ['java se', 'java.security.cert', 'java.base', 'clase java', 'Java 1.4']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.CertStore.description }}

## Sintaxis
~~~java
public class CertStore extends Object
~~~

## Constructores
* [CertStore()](/Java/CertStore/CertStore/)

## Métodos
* [getCertificates()](/Java/CertStore/getCertificates/)
* [getCertStoreParameters()](/Java/CertStore/getCertStoreParameters/)
* [getCRLs()](/Java/CertStore/getCRLs/)
* [getDefaultType()](/Java/CertStore/getDefaultType/)
* [getInstance()](/Java/CertStore/getInstance/)
* [getProvider()](/Java/CertStore/getProvider/)
* [getType()](/Java/CertStore/getType/)

## Ejemplo
~~~java
{{ site.data.Java.C.CertStore.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.C.CertStore.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
