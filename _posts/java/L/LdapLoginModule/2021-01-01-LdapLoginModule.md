---
title: LdapLoginModule
permalink: Java/LdapLoginModule
date: 2021-01-11
key: Java.L.LdapLoginModule
category: java
tags: ['java se', 'com.sun.security.auth.module', 'jdk.security.auth', 'clase java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.L.LdapLoginModule.description }}

## Sintaxis
~~~java
public class LdapLoginModule extends Object implements LoginModule
~~~

## Constructores
* [LdapLoginModule()](/Java/LdapLoginModule/LdapLoginModule/)

## Métodos
* [abort()](/Java/LdapLoginModule/abort)
* [commit()](/Java/LdapLoginModule/commit)
* [initialize()](/Java/LdapLoginModule/initialize)
* [login()](/Java/LdapLoginModule/login)
* [logout()](/Java/LdapLoginModule/logout)

## Ejemplo
~~~java
{{ site.data.Java.L.LdapLoginModule.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.L.LdapLoginModule.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
