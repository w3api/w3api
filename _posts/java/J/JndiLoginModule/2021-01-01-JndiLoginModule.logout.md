---
title: JndiLoginModule.logout()
permalink: /Java/JndiLoginModule/logout/
date: 2021-01-11
key: Java.J.JndiLoginModule
category: Java
tags: ['java se', 'com.sun.security.auth.module', 'jdk.security.auth', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JndiLoginModule.metodos valor="logout" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean logout() throws LoginException
~~~

## Excepciones
[LoginException](/Java/LoginException/)

## Clase Padre
[JndiLoginModule](/Java/JndiLoginModule/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
