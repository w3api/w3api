---
title: LoginModule
permalink: Java/LoginModule
date: 2021-01-11
key: Java.L.LoginModule
category: java
tags: ['java se', 'javax.security.auth.spi', 'java.base', 'interface java', 'Java 1.4']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.L.LoginModule.description }}

## Sintaxis
~~~java
public interface LoginModule
~~~

## Métodos
* [abort()](/Java/LoginModule/abort)
* [commit()](/Java/LoginModule/commit)
* [initialize()](/Java/LoginModule/initialize)
* [login()](/Java/LoginModule/login)
* [logout()](/Java/LoginModule/logout)

## Ejemplo
~~~java
{{ site.data.Java.L.LoginModule.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.L.LoginModule.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
