---
title: UnsolicitedNotification
permalink: Java/UnsolicitedNotification
date: 2021-01-11
key: JavaJava.U.UnsolicitedNotification
category: java
tags: ['java se', 'javax.naming.ldap', 'java.naming', 'interface java', 'Java 1.3']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.U.UnsolicitedNotification.description }}

## Sintaxis
~~~java
public interface UnsolicitedNotification extends ExtendedResponse, HasControls
~~~

## Métodos
* [getException()](/Java/UnsolicitedNotification/getException)
* [getReferrals()](/Java/UnsolicitedNotification/getReferrals)

## Ejemplo
~~~java
{{ site.data.Java.U.UnsolicitedNotification.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.U.UnsolicitedNotification.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
