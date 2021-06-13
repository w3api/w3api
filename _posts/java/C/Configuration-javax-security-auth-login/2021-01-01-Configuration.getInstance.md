---
title: Configuration.getInstance()
permalink: /Java/Configuration-javax-security-auth-login/getInstance/
date: 2021-01-11
key: Java.C.Configuration-javax-security-auth-login
category: Java
tags: ['java se', 'javax.security.auth.login', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Configuration-javax-security-auth-login.metodos valor="getInstance" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static Configuration getInstance(String type, Configuration.Parameters params) throws NoSuchAlgorithmException
public static Configuration getInstance(String type, Configuration.Parameters params, String provider) throws NoSuchProviderException, NoSuchAlgorithmException
public static Configuration getInstance(String type, Configuration.Parameters params, Provider provider) throws NoSuchAlgorithmException
~~~

## Parámetros
* **Provider provider**,  {% include w3api/param_description.html metodo=_dato parametro="Provider provider" %}
* **String provider**,  {% include w3api/param_description.html metodo=_dato parametro="String provider" %}
* **Configuration.Parameters params**,  {% include w3api/param_description.html metodo=_dato parametro="Configuration.Parameters params" %}
* **String type**,  {% include w3api/param_description.html metodo=_dato parametro="String type" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NoSuchProviderException](/Java/NoSuchProviderException/), [SecurityException](/Java/SecurityException/), [NoSuchAlgorithmException](/Java/NoSuchAlgorithmException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[Configuration](/Java/Configuration-javax-security-auth-login/)

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
