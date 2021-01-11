---
title: Authenticator.requestPasswordAuthenticationInstance()
permalink: Java/Authenticator-java-net/requestPasswordAuthenticationInstance
date: 2021-01-11
key: JavaJava.A.Authenticator-java-net
category: java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.Authenticator-java-net.metodos valor="requestPasswordAuthenticationInstance" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public PasswordAuthentication requestPasswordAuthenticationInstance(String host, InetAddress addr, int port, String protocol, String prompt, String scheme, URL url, Authenticator.RequestorType reqType)
~~~

## Parámetros
* **URL url**,  {% include w3api/param_description.html metodo=_dato parametro="URL url" %}
* **String host**,  {% include w3api/param_description.html metodo=_dato parametro="String host" %}
* **String prompt**,  {% include w3api/param_description.html metodo=_dato parametro="String prompt" %}
* **Authenticator.RequestorType reqType**,  {% include w3api/param_description.html metodo=_dato parametro="Authenticator.RequestorType reqType" %}
* **String scheme**,  {% include w3api/param_description.html metodo=_dato parametro="String scheme" %}
* **int port**,  {% include w3api/param_description.html metodo=_dato parametro="int port" %}
* **String protocol**,  {% include w3api/param_description.html metodo=_dato parametro="String protocol" %}
* **InetAddress addr**,  {% include w3api/param_description.html metodo=_dato parametro="InetAddress addr" %}

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
