---
title: JndiLoginModule
permalink: /Java/JndiLoginModule/
date: 2021-01-11
key: Java.J.JndiLoginModule
category: Java
tags: ['java se', 'com.sun.security.auth.module', 'jdk.security.auth', 'clase java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.J.JndiLoginModule.description }}

## Sintaxis
~~~java
public class JndiLoginModule extends Object implements LoginModule
~~~

## Constructores
* [JndiLoginModule()](/Java/JndiLoginModule/JndiLoginModule/)

## Campos
* [GROUP_PROVIDER](/Java/JndiLoginModule/GROUP_PROVIDER)
* [USER_PROVIDER](/Java/JndiLoginModule/USER_PROVIDER)

## Métodos
* [abort()](/Java/JndiLoginModule/abort)
* [commit()](/Java/JndiLoginModule/commit)
* [initialize()](/Java/JndiLoginModule/initialize)
* [login()](/Java/JndiLoginModule/login)
* [logout()](/Java/JndiLoginModule/logout)

## Ejemplo
~~~java
{{ site.data.Java.J.JndiLoginModule.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.J.JndiLoginModule.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
