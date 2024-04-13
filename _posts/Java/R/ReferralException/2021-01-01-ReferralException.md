---
title: ReferralException
permalink: /Java/ReferralException/
date: 2021-01-11
key: Java.R.ReferralException
category: Java
tags: ['java se', 'javax.naming', 'java.naming', 'clase java', 'Java 1.3']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.R.ReferralException.description }}

## Sintaxis
~~~java
public abstract class ReferralException extends NamingException
~~~

## Constructores
* [ReferralException()](/Java/ReferralException/ReferralException/)

## Métodos
* [getReferralContext()](/Java/ReferralException/getReferralContext)
* [getReferralInfo()](/Java/ReferralException/getReferralInfo)
* [retryReferral()](/Java/ReferralException/retryReferral)
* [skipReferral()](/Java/ReferralException/skipReferral)

## Ejemplo
~~~java
{{ site.data.Java.R.ReferralException.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.ReferralException.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
