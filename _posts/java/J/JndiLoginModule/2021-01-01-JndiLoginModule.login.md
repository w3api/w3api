---
title: JndiLoginModule.login()
permalink: /Java/JndiLoginModule/login/
date: 2021-01-11
key: Java.J.JndiLoginModule
category: Java
tags: ['java se', 'com.sun.security.auth.module', 'jdk.security.auth', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JndiLoginModule.metodos valor="login" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean login() throws LoginException
~~~

## Excepciones
[LoginException](/Java/LoginException/), [FailedLoginException](/Java/FailedLoginException/)

## Clase Padre
[JndiLoginModule](/Java/JndiLoginModule/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
