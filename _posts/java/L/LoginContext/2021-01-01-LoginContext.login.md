---
title: LoginContext.login()
permalink: /Java/LoginContext/login/
date: 2021-01-11
key: Java.L.LoginContext
category: Java
tags: ['java se', 'javax.security.auth.login', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LoginContext.metodos valor="login" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void login() throws LoginException
~~~

## Excepciones
[LoginException](/Java/LoginException/)

## Clase Padre
[LoginContext](/Java/LoginContext/)

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
