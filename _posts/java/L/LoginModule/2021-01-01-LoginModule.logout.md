---
title: LoginModule.logout()
permalink: /Java/LoginModule/logout/
date: 2021-01-11
key: Java.L.LoginModule
category: Java
tags: ['java se', 'javax.security.auth.spi', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LoginModule.metodos valor="logout" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean logout() throws LoginException
~~~

## Excepciones
[LoginException](/Java/LoginException/)

## Clase Padre
[LoginModule](/Java/LoginModule/)

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
