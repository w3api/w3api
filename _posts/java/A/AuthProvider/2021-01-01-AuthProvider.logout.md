---
title: AuthProvider.logout()
permalink: Java/AuthProvider/logout
date: 2021-01-11
key: JavaJava.A.AuthProvider
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AuthProvider.metodos valor="logout" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void logout() throws LoginException
~~~

## Excepciones
[LoginException](/Java/LoginException/), [SecurityException](/Java/SecurityException/), [IllegalStateException](/Java/IllegalStateException/)

## Clase Padre
[AuthProvider](/Java/AuthProvider/)

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
