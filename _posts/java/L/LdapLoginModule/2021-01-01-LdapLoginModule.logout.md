---
title: LdapLoginModule.logout()
permalink: /Java/LdapLoginModule/logout/
date: 2021-01-11
key: Java.L.LdapLoginModule
category: Java
tags: ['java se', 'com.sun.security.auth.module', 'jdk.security.auth', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LdapLoginModule.metodos valor="logout" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean logout() throws LoginException
~~~

## Excepciones
[LoginException](/Java/LoginException/)

## Clase Padre
[LdapLoginModule](/Java/LdapLoginModule/)

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
