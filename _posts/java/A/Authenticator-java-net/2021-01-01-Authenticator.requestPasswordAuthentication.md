---
title: Authenticator.requestPasswordAuthentication()
permalink: Java/Authenticator-java-net/requestPasswordAuthentication
date: 2021-01-11
key: JavaJava.A.Authenticator-java-net
category: java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.Authenticator-java-net.metodos valor="requestPasswordAuthentication" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static PasswordAuthentication requestPasswordAuthentication(String host, InetAddress addr, int port, String protocol, String prompt, String scheme)
public static PasswordAuthentication requestPasswordAuthentication(String host, InetAddress addr, int port, String protocol, String prompt, String scheme, URL url, Authenticator.RequestorType reqType)
public static PasswordAuthentication requestPasswordAuthentication(Authenticator authenticator, String host, InetAddress addr, int port, String protocol, String prompt, String scheme, URL url, Authenticator.RequestorType reqType)
public static PasswordAuthentication requestPasswordAuthentication(InetAddress addr, int port, String protocol, String prompt, String scheme)
~~~

## Parámetros
* **URL url**,  {% include w3api/param_description.html metodo=_dato parametro="URL url" %}
* **String host**,  {% include w3api/param_description.html metodo=_dato parametro="String host" %}
* **String prompt**,  {% include w3api/param_description.html metodo=_dato parametro="String prompt" %}
* **Authenticator.RequestorType reqType**,  {% include w3api/param_description.html metodo=_dato parametro="Authenticator.RequestorType reqType" %}
* **String scheme**,  {% include w3api/param_description.html metodo=_dato parametro="String scheme" %}
* **int port**,  {% include w3api/param_description.html metodo=_dato parametro="int port" %}
* **Authenticator authenticator**,  {% include w3api/param_description.html metodo=_dato parametro="Authenticator authenticator" %}
* **String protocol**,  {% include w3api/param_description.html metodo=_dato parametro="String protocol" %}
* **InetAddress addr**,  {% include w3api/param_description.html metodo=_dato parametro="InetAddress addr" %}

## Excepciones
[SecurityException](/Java/SecurityException/)

## Clase Padre
[Authenticator](/Java/Authenticator-java-net/)

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
