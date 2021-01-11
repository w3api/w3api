---
title: LoginContext.LoginContext()
permalink: Java/LoginContext/LoginContext
date: 2021-01-11
key: JavaJava.L.LoginContext
category: java
tags: ['java se', 'javax.security.auth.login', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LoginContext.constructores valor="LoginContext" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public LoginContext(String name) throws LoginException
public LoginContext(String name, CallbackHandler callbackHandler) throws LoginException
public LoginContext(String name, Subject subject) throws LoginException
public LoginContext(String name, Subject subject, CallbackHandler callbackHandler) throws LoginException
public LoginContext(String name, Subject subject, CallbackHandler callbackHandler, Configuration config) throws LoginException
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **CallbackHandler callbackHandler**,  {% include w3api/param_description.html metodo=_dato parametro="CallbackHandler callbackHandler" %}
* **Configuration config**,  {% include w3api/param_description.html metodo=_dato parametro="Configuration config" %}
* **Subject subject**,  {% include w3api/param_description.html metodo=_dato parametro="Subject subject" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [LoginException](/Java/LoginException/)

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
