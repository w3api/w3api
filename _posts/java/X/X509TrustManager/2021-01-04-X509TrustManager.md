---
title: X509TrustManager
permalink: Java/X509TrustManager
date: 2021-01-04
key: JavaJava.X.X509TrustManager
category: java
tags: ['java se', 'javax.net.ssl', 'java.base', 'interface java', 'Java 1.4']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.X.X509TrustManager.description }}

## Sintaxis
~~~java
public interface X509TrustManager extends TrustManager
~~~

## Métodos
* [checkClientTrusted()](/Java/X509TrustManager/checkClientTrusted)
* [checkServerTrusted()](/Java/X509TrustManager/checkServerTrusted)
* [getAcceptedIssuers()](/Java/X509TrustManager/getAcceptedIssuers)

## Ejemplo
~~~java
{{ site.data.Java.X.X509TrustManager.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.X.X509TrustManager.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
