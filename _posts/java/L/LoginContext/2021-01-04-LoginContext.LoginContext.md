---
title: LoginContext.LoginContext()
permalink: Java/LoginContext/LoginContext
date: 2021-01-04
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
* **Configuration config**,  {% include w3api/param_description.html metodo=_data parametro="Configuration config" %}
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}
* **Subject subject**,  {% include w3api/param_description.html metodo=_data parametro="Subject subject" %}
* **CallbackHandler callbackHandler**,  {% include w3api/param_description.html metodo=_data parametro="CallbackHandler callbackHandler" %}

## Excepciones
[LoginException](/Java/LoginException/), [SecurityException](/Java/SecurityException/)

## Clase Padre
[LoginContext](/Java/LoginContext/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.L.LoginContext.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
