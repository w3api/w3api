---
title: AuthorizeCallback
permalink: Java/AuthorizeCallback
date: 2021-01-11
key: JavaJava.A.AuthorizeCallback
category: java
tags: ['java se', 'javax.security.sasl', 'java.security.sasl', 'clase java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.A.AuthorizeCallback.description }}

## Sintaxis
~~~java
public class AuthorizeCallback extends Object implements Callback, Serializable
~~~

## Constructores
* [AuthorizeCallback()](/Java/AuthorizeCallback/AuthorizeCallback/)

## Métodos
* [getAuthenticationID()](/Java/AuthorizeCallback/getAuthenticationID)
* [getAuthorizationID()](/Java/AuthorizeCallback/getAuthorizationID)
* [getAuthorizedID()](/Java/AuthorizeCallback/getAuthorizedID)
* [isAuthorized()](/Java/AuthorizeCallback/isAuthorized)
* [setAuthorized()](/Java/AuthorizeCallback/setAuthorized)
* [setAuthorizedID()](/Java/AuthorizeCallback/setAuthorizedID)

## Ejemplo
~~~java
{{ site.data.Java.A.AuthorizeCallback.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AuthorizeCallback.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
