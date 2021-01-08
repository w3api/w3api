---
title: Authenticator.requestPasswordAuthenticationInstance()
permalink: Java/Authenticator-java-net/requestPasswordAuthenticationInstance
date: 2021-01-04
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
* **String host**,  {% include w3api/param_description.html metodo=_data parametro="String host" %}
* **String protocol**,  {% include w3api/param_description.html metodo=_data parametro="String protocol" %}
* **String scheme**,  {% include w3api/param_description.html metodo=_data parametro="String scheme" %}
* **String prompt**,  {% include w3api/param_description.html metodo=_data parametro="String prompt" %}
* **URL url**,  {% include w3api/param_description.html metodo=_data parametro="URL url" %}
* **int port**,  {% include w3api/param_description.html metodo=_data parametro="int port" %}
* **Authenticator.RequestorType reqType**,  {% include w3api/param_description.html metodo=_data parametro="Authenticator.RequestorType reqType" %}
* **InetAddress addr**,  {% include w3api/param_description.html metodo=_data parametro="InetAddress addr" %}

## Clase Padre
[Authenticator](/Java/Authenticator-java-net/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.Authenticator-java-net.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
