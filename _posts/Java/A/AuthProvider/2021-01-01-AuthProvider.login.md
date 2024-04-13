---
title: AuthProvider.login()
permalink: /Java/AuthProvider/login/
date: 2021-01-11
key: Java.A.AuthProvider
category: Java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AuthProvider.metodos valor="login" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void login(Subject subject, CallbackHandler handler) throws LoginException
~~~

## Parámetros
* **CallbackHandler handler**,  {% include w3api/param_description.html metodo=_dato parametro="CallbackHandler handler" %}
* **Subject subject**,  {% include w3api/param_description.html metodo=_dato parametro="Subject subject" %}

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
