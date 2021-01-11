---
title: AuthProvider
permalink: Java/AuthProvider
date: 2021-01-11
key: JavaJava.A.AuthProvider
category: java
tags: ['java se', 'java.security', 'java.base', 'clase java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.A.AuthProvider.description }}

## Sintaxis
~~~java
public abstract class AuthProvider extends Provider
~~~

## Constructores
* [AuthProvider()](/Java/AuthProvider/AuthProvider/)

## Métodos
* [login()](/Java/AuthProvider/login)
* [logout()](/Java/AuthProvider/logout)
* [setCallbackHandler()](/Java/AuthProvider/setCallbackHandler)

## Ejemplo
~~~java
{{ site.data.Java.A.AuthProvider.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AuthProvider.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
