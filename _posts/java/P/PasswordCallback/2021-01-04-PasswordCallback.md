---
title: PasswordCallback
permalink: Java/PasswordCallback
date: 2021-01-04
key: JavaJava.P.PasswordCallback
category: java
tags: ['java se', 'javax.security.auth.callback', 'java.base', 'clase java', 'Java 1.4']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.P.PasswordCallback.description }}

## Sintaxis
~~~java
public class PasswordCallback extends Object implements Callback, Serializable
~~~

## Constructores
* [PasswordCallback()](/Java/PasswordCallback/PasswordCallback/)

## Métodos
* [clearPassword()](/Java/PasswordCallback/clearPassword)
* [getPassword()](/Java/PasswordCallback/getPassword)
* [getPrompt()](/Java/PasswordCallback/getPrompt)
* [isEchoOn()](/Java/PasswordCallback/isEchoOn)
* [setPassword()](/Java/PasswordCallback/setPassword)

## Ejemplo
~~~java
{{ site.data.Java.P.PasswordCallback.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PasswordCallback.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
